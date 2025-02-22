import json
import requests
from urllib.parse import urlparse

def get_domains(pastebin_url):
    """
    Recupera il contenuto del Pastebin con i domini.
    :param pastebin_url: URL del Pastebin da cui recuperare i domini.
    :return: Lista dei domini dal file Pastebin.
    """
    try:
        response = requests.get(pastebin_url)
        response.raise_for_status()
        # Estrai i domini dalla risposta e rimuovi eventuali caratteri di ritorno a capo
        domains = response.text.strip().split('\n')
        domains = [domain.strip().replace('\r', '') for domain in domains]  # Rimuove i caratteri \r
        return domains
    except requests.RequestException as e:
        print(f"Errore durante il recupero dei domini: {e}")
        return []

def extract_final_domain(domain):
    """
    Estrae solo la parte finale del dominio, come 'paris' da 'www.streamingcommunity.paris'.
    
    :param domain: Dominio da cui estrarre la parte finale.
    :return: Parte finale del dominio (es. 'paris').
    """
    parsed_url = urlparse(domain)
    netloc = parsed_url.netloc or parsed_url.path  # Nel caso in cui non ci sia il protocollo
    
    # Ottieni l'ultima parte del dominio
    parts = netloc.split('.')
    
    # Restituisce l'ultima parte (es. 'paris' da 'streamingcommunity.paris')
    if len(parts) > 1:
        final_domain = parts[-1]  # Estrae solo la parte finale (ad esempio 'paris' da 'streamingcommunity.paris')
        return final_domain
    else:
        return netloc  # Nel caso di un dominio non valido

def check_redirect(domain):
    """
    Verifica se un dominio fa un redirect e restituisce il dominio finale (parte finale).
    
    :param domain: Dominio da verificare.
    :return: Tuple con l'URL originale e il dominio finale (parte finale).
    """
    if not domain.startswith(('http://', 'https://')):
        domain = 'http://' + domain

    try:
        response = requests.get(domain, allow_redirects=True)
        final_url = response.url
        final_domain = extract_final_domain(final_url)  # Estrai solo la parte finale del dominio
        return domain, final_domain
    except requests.RequestException as e:
        return domain, f"Error: {str(e)}"

def update_json_file():
    """
    Aggiorna il file JSON con i domini finali (post-redirect) recuperati da Pastebin.
    """
    # Carica il file JSON che vuoi aggiornare
    try:
        with open('config.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Errore: Il file config.json non è stato trovato.")
        return
    except json.JSONDecodeError:
        print("Errore: Il file config.json non è un JSON valido.")
        return
    
    # Ottieni i domini per StreamingCommunity da un Pastebin specifico
    streamingcommunity_url = 'https://pastebin.com/raw/KgQ4jTy6'
    streamingcommunity_domains = get_domains(streamingcommunity_url)

    # Ottieni i domini per gli altri siti dal Pastebin generale
    general_pastebin_url = 'https://pastebin.com/raw/E8WAhekV'
    general_domains = get_domains(general_pastebin_url)

    if not general_domains or not streamingcommunity_domains:
        print("Lista dei domini vuota. Controlla i link di Pastebin.")
        return

    # Mappatura dei siti da aggiornare
    site_mapping = {
        'StreamingCommunity': streamingcommunity_domains[0],  # Dominio specifico per StreamingCommunity
        'Filmpertutti': general_domains[1],                  # Secondo dominio
        'Tantifilm': general_domains[2],                     # Terzo dominio
        'LordChannel': general_domains[3],                   # Quarto dominio
        'StreamingWatch': general_domains[4],                # Quinto dominio
        'CB01': general_domains[5],                          # Sesto dominio
        'DDLStream': general_domains[6],                     # Settimo dominio
        'Guardaserie': general_domains[7],                   # Ottavo dominio
        'GuardaHD': general_domains[8],                      # Nono dominio
        'AnimeWorld': general_domains[9],                    # Decimo dominio
        'SkyStreaming': general_domains[10],                 # Undicesimo dominio
       # 'DaddyLiveHD': general_domains[11],                  # Dodicesimo dominio
    }

    # Aggiorna il file JSON con gli URL finali (post-redirect)
    for site_key, domain_url in site_mapping.items():
        if site_key in data['Siti']:
            original, final_domain = check_redirect(domain_url)  # Verifica il redirect
            if "Error" in final_domain:
                print(f"Errore nel redirect di {original}: {final_domain}")
                continue
            data['Siti'][site_key]['domain'] = final_domain
            print(f"Aggiornato {site_key}: {final_domain}")  # Messaggio di debug

    # Scrivi il file JSON aggiornato
    try:
        with open('config.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("File config.json aggiornato con successo!")
    except Exception as e:
        print(f"Errore durante il salvataggio del file JSON: {e}")

if __name__ == '__main__':
    update_json_file()

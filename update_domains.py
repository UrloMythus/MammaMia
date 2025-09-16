import json
import requests
from urllib.parse import urlparse

def get_domains(pastebin_url):
    try:
        response = requests.get(pastebin_url)
        response.raise_for_status()
        domains = response.text.strip().split('\n')
        domains = [domain.strip().replace('\r', '') for domain in domains]
        return domains
    except requests.RequestException as e:
        print(f"❌ Errore durante il recupero dei domini: {e}")
        return []

def extract_full_domain(domain, site_key):
    parsed_url = urlparse(domain)
    scheme = parsed_url.scheme if parsed_url.scheme else 'https'
    netloc = parsed_url.netloc or parsed_url.path

    if site_key in ['Tantifilm', 'StreamingWatch']:
        if not netloc.startswith('www.'):
            netloc = 'www.' + netloc
        return f"{scheme}://{netloc}"
    else:
        return f"{scheme}://{netloc}"

def extract_tld(domain_url):
    parsed = urlparse(domain_url)
    netloc = parsed.netloc or parsed.path
    if '.' in netloc:
        return netloc.split('.')[-1]
    return ''

def check_redirect(domain, site_key):
    if not domain.startswith(('http://', 'https://')):
        domain = 'http://' + domain

    try:
        response = requests.get(domain, allow_redirects=True)
        final_url = response.url
        final_domain = extract_full_domain(final_url, site_key)
        return domain, final_domain
    except requests.RequestException as e:
        return domain, f"Error: {str(e)}"

def update_json_file():
    try:
        with open('config.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("❌ Errore: Il file config.json non è stato trovato.")
        return
    except json.JSONDecodeError:
        print("❌ Errore: Il file config.json non è un JSON valido.")
        return

    pastebin_url = 'https://pastebin.com/raw/HFx8qvKF'
    domain_list = get_domains(pastebin_url)

    if len(domain_list) < 13:
        print("❌ Lista dei domini troppo corta. Controlla il Pastebin, fratm.")
        return

    site_mapping = {
        'StreamingCommunity': domain_list[0],
        'StreamingWatch': domain_list[1],
        'CB01': domain_list[2],
        'Guardaserie': domain_list[3],
        'GuardaHD': domain_list[4],
        'Eurostreaming': domain_list[5],
        'Guardaflix': domain_list[6],
        'Guardoserie': domain_list[7],
        'AnimeWorld': domain_list[8],
    }

    for site_key, domain_url in site_mapping.items():
        if site_key in data['Siti']:
            original, final_domain = check_redirect(domain_url, site_key)
            if "Error" in final_domain:
                print(f"❌ Errore nel redirect di {original}: {final_domain}")
                continue

            # Aggiorna l'URL del sito
            data['Siti'][site_key]['url'] = final_domain
            print(f"✅ Aggiornato {site_key}: {final_domain}")

    try:
        with open('config.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("💾 File config.json aggiornato con successo! Alleluja!")
    except Exception as e:
        print(f"❌ Errore durante il salvataggio del file JSON: {e}")

if __name__ == '__main__':
    update_json_file()

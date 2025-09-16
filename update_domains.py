import json
import requests
from urllib.parse import urlparse
import urllib3

# Disabilita i warning SSL (solo per siti con certificati invalidi)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; DomainUpdater/1.0)"}


def get_domains(pastebin_url):
    try:
        response = requests.get(pastebin_url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        domains = response.text.strip().split('\n')
        domains = [domain.strip().replace('\r', '') for domain in domains if domain.strip()]
        return domains
    except requests.RequestException as e:
        print(f"❌ Errore durante il recupero dei domini: {e}")
        return []


def extract_full_domain(domain, site_key):
    parsed_url = urlparse(domain)
    scheme = parsed_url.scheme if parsed_url.scheme else 'https'
    netloc = parsed_url.netloc or parsed_url.path

    # Alcuni siti preferiscono "www." → controlla prima che risponda
    if site_key in ['Tantifilm', 'StreamingWatch'] and not netloc.startswith('www.'):
        test_url = f"{scheme}://www.{netloc}"
        try:
            r = requests.head(test_url, headers=HEADERS, timeout=5, verify=False)
            if r.status_code < 400:
                netloc = 'www.' + netloc
        except requests.RequestException:
            pass  # se www non risponde, tieni quello base

    return f"{scheme}://{netloc}"


def check_redirect(domain, site_key):
    if not domain.startswith(('http://', 'https://')):
        domain = 'http://' + domain

    try:
        # Ignora SSL per tutti i domini (così anche quelli con certificato rotto vengono aggiornati)
        response = requests.get(domain, allow_redirects=True, headers=HEADERS, timeout=10, verify=False)
        final_url = response.url
        final_domain = extract_full_domain(final_url, site_key)
        return final_domain
    except requests.RequestException as e:
        print(f"❌ Redirect fallito per {domain}: {e}")
        return None


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

    if len(domain_list) < 9:
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
            final_domain = check_redirect(domain_url, site_key)
            if final_domain:
                data['Siti'][site_key]['url'] = final_domain
                print(f"✅ Aggiornato {site_key}: {final_domain}")
            else:
                print(f"⚠️ Nessun aggiornamento per {site_key}, mantengo il vecchio URL.")

    try:
        with open('config.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("💾 File config.json aggiornato con successo! Alleluja!")
    except Exception as e:
        print(f"❌ Errore durante il salvataggio del file JSON: {e}")


if __name__ == '__main__':
    update_json_file()

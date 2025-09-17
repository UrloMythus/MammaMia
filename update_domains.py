import json
import requests
from urllib.parse import urlparse
import urllib3

# Disabilita i warning SSL (per certificati invalidi o scaduti)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; DomainUpdater/3.0)"}


def load_config():
    """Carica il file config.json locale."""
    try:
        with open('config.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("❌ Errore: config.json non trovato.")
        return None
    except json.JSONDecodeError:
        print("❌ Errore: config.json non è un JSON valido.")
        return None


def extract_full_domain(domain, site_key):
    """Normalizza dominio con schema + eventuale www."""
    parsed_url = urlparse(domain)
    scheme = parsed_url.scheme if parsed_url.scheme else 'https'
    netloc = parsed_url.netloc or parsed_url.path

    # Alcuni siti vogliono "www."
    if site_key in ['Tantifilm', 'StreamingWatch'] and not netloc.startswith('www.'):
        test_url = f"{scheme}://www.{netloc}"
        try:
            r = requests.head(test_url, headers=HEADERS, timeout=5, verify=False)
            if r.status_code < 400:
                netloc = 'www.' + netloc
        except requests.RequestException:
            pass

    return f"{scheme}://{netloc}"


def check_redirect(domain, site_key):
    """Controlla redirect e restituisce l'URL finale valido."""
    if not domain.startswith(('http://', 'https://')):
        domain = 'http://' + domain

    try:
        response = requests.get(domain, allow_redirects=True, headers=HEADERS, timeout=10, verify=False)
        final_url = response.url
        final_domain = extract_full_domain(final_url, site_key)
        return final_domain
    except requests.RequestException as e:
        print(f"❌ Redirect fallito per {domain}: {e}")
        return None


def update_json_file():
    data = load_config()
    if not data:
        return

    sites = data.get("Siti", {})

    for site_key, site_info in sites.items():
        domain_url = site_info.get("url")  # 👈 legge solo il campo "url"
        if not domain_url:
            print(f"⚠️ Nessun URL trovato per {site_key}, salto…")
            continue

        final_domain = check_redirect(domain_url, site_key)
        if final_domain:
            data['Siti'][site_key]['url'] = final_domain
            print(f"✅ Aggiornato {site_key}: {final_domain}")
        else:
            print(f"⚠️ Nessun aggiornamento per {site_key}, mantengo {domain_url}")

    try:
        with open('config.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("💾 File config.json aggiornato con successo!")
    except Exception as e:
        print(f"❌ Errore durante il salvataggio del file JSON: {e}")


if __name__ == '__main__':
    update_json_file()

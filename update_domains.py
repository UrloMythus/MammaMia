import re
import requests
import urllib3
from urllib.parse import urlparse

# Disabilita i warning SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; DomainUpdater/3.1)"}

# Link RAW del config.json su GitHub
CONFIG_URL = "https://raw.githubusercontent.com/UrloMythus/MammaMia/main/config.json"


def extract_full_domain(domain, site_key):
    """Normalizza dominio con schema + eventuale www."""
    parsed_url = urlparse(domain)
    scheme = parsed_url.scheme if parsed_url.scheme else 'https'
    netloc = parsed_url.netloc or parsed_url.path

    # Alcuni siti preferiscono "www."
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
    """Segue i redirect e restituisce l'URL finale valido."""
    if not domain.startswith(('http://', 'https://')):
        domain = 'http://' + domain

    try:
        response = requests.get(domain, allow_redirects=True, headers=HEADERS, timeout=10, verify=False)
        final_url = response.url
        return extract_full_domain(final_url, site_key)
    except requests.RequestException as e:
        print(f"❌ Redirect fallito per {domain}: {e}")
        return None


def update_config_file():
    try:
        # Scarica il file config.json da GitHub
        response = requests.get(CONFIG_URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        config_text = response.text
    except requests.RequestException as e:
        print(f"❌ Errore durante il download del file config.json: {e}")
        return

    updated_lines = []
    current_site = None

    # Regex per intercettare le righe con "url"
    url_pattern = re.compile(r'("url"\s*:\s*")([^"]+)(")')

    for line in config_text.splitlines():
        match = url_pattern.search(line)
        if match:
            old_url = match.group(2)
            # Ricava la "chiave sito" leggendo la riga precedente col nome del sito
            if current_site:
                site_key = current_site
            else:
                site_key = "Sito"

            new_url = check_redirect(old_url, site_key)
            if new_url:
                print(f"✅ Aggiornato {site_key}: {old_url} → {new_url}")
                line = url_pattern.sub(rf'\1{new_url}\3', line)
            else:
                print(f"⚠️ Nessun aggiornamento per {site_key}, mantengo {old_url}")
        # Se la riga contiene il nome del sito, lo memorizzo
        elif line.strip().endswith("{") and '"' in line:
            current_site = line.strip().split('"')[1]
        updated_lines.append(line)

    # Scrive il nuovo config.json in locale
    with open("config.json", "w", encoding="utf-8") as f:
        f.write("\n".join(updated_lines))

    print("💾 File config.json aggiornato: solo le righe 'url' sono state modificate.")


if __name__ == "__main__":
    update_config_file()

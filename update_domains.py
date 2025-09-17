import re
import requests
import urllib3
from urllib.parse import urlparse

# Disabilita i warning SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; DomainUpdater/3.3)"}

# Link RAW del config.json su GitHub
CONFIG_URL = "https://raw.githubusercontent.com/UrloMythus/MammaMia/main/config.json"


def extract_full_domain(domain):
    """Normalizza dominio con schema."""
    parsed_url = urlparse(domain)
    scheme = parsed_url.scheme if parsed_url.scheme else 'https'
    netloc = parsed_url.netloc or parsed_url.path
    return f"{scheme}://{netloc}"


def check_redirect(domain):
    """Segue i redirect e restituisce l'URL finale valido."""
    if not domain.startswith(('http://', 'https://')):
        domain = 'http://' + domain

    try:
        response = requests.get(domain, allow_redirects=True, headers=HEADERS, timeout=10, verify=False)
        final_url = response.url
        return extract_full_domain(final_url)
    except requests.RequestException as e:
        print(f"❌ Redirect fallito per {domain}: {e}")
        return None


def update_config_file():
    try:
        response = requests.get(CONFIG_URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        config_text = response.text
    except requests.RequestException as e:
        print(f"❌ Errore durante il download del file config.json: {e}")
        return

    updated_lines = []
    url_pattern = re.compile(r'("url"\s*:\s*")([^"]+)(")')

    for line in config_text.splitlines():
        match = url_pattern.search(line)
        if match:
            old_url = match.group(2)
            new_url = check_redirect(old_url)
            if new_url:
                print(f"✅ Aggiornato: {old_url} → {new_url}")
                # sostituisce solo l'URL, lascia tutto il resto invariato
                line = url_pattern.sub(rf'\1{new_url}\3', line)
            else:
                print(f"⚠️ Nessun aggiornamento per {old_url}, mantengo invariato")
        updated_lines.append(line)

    with open("config.json", "w", encoding="utf-8") as f:
        f.write("\n".join(updated_lines))

    print("💾 File config.json aggiornato: SOLO le righe 'url' sono state modificate.")


if __name__ == "__main__":
    update_config_file()

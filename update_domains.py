#!/usr/bin/env python3
"""
Merge remote URLs into local config.json, replacing ONLY the "url" lines.
- Scarica config.json remoto (raw GitHub).
- Per ogni sito in "Siti", segue i redirect e trova l'URL finale.
- Apre il config.json locale come testo, trova le righe "url" relative ai siti
  e sostituisce SOLO il valore dentro le virgolette, preservando tutto il resto.
- Crea un backup del config.json locale prima di sovrascriverlo.
"""
from pathlib import Path
from datetime import datetime
import shutil
import re
import requests
import urllib3
from urllib.parse import urlparse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- CONFIGURAZIONE ---
REMOTE_RAW_URL = "https://raw.githubusercontent.com/UrloMythus/MammaMia/main/config.json"
LOCAL_CONFIG_PATH = Path("config.json")
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; DomainMerger/1.0)"}
REQUEST_TIMEOUT = 12
# -----------------------

def backup_file(path: Path) -> Path | None:
    if not path.exists():
        return None
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    bak = path.with_name(f"{path.name}.bak_{ts}")
    shutil.copy2(path, bak)
    return bak

def normalize_url(u: str) -> str:
    parsed = urlparse(u)
    scheme = parsed.scheme if parsed.scheme else "https"
    netloc = parsed.netloc or parsed.path
    return f"{scheme}://{netloc}"

def follow_redirect(url: str) -> str | None:
    if not url.startswith(("http://", "https://")):
        test = "http://" + url
    else:
        test = url
    try:
        r = requests.get(test, allow_redirects=True, headers=HEADERS,
                         timeout=REQUEST_TIMEOUT, verify=False)
        return normalize_url(r.url)
    except requests.RequestException as e:
        print(f"⚠️ Redirect fallito per '{url}': {e}")
        return None

def load_remote_urls(remote_raw_url: str) -> dict:
    """Scarica il JSON remoto e ritorna mappa site_key -> url (o None se mancante)."""
    try:
        r = requests.get(remote_raw_url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        r.raise_for_status()
        remote_json = r.json()
    except Exception as e:
        raise RuntimeError(f"Impossibile scaricare/parsing remote config: {e}")

    siti = remote_json.get("Siti", {})
    result = {}
    for site_key, site_info in siti.items():
        url = site_info.get("url")
        if url:
            result[site_key] = url
    return result

def merge_remote_into_local(remote_map: dict, local_path: Path):
    if not local_path.exists():
        raise FileNotFoundError(f"File locale non trovato: {local_path}")

    # backup
    bak = backup_file(local_path)
    if bak:
        print(f"📦 Backup creato: {bak.name}")

    text = local_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # regex: match apertura blocco sito es.     "CB01":{
    site_open_re = re.compile(r'^\s*"(?P<site>[^"]+)"\s*:\s*\{\s*$')

    # regex per trovare esattamente la riga "url": "valore" preservando indentazione e virgola finale
    url_line_re = re.compile(r'^(\s*)"url"\s*:\s*"([^"]*)"( *)(,?)\s*$')

    current_site = None
    updated_lines = []
    changes = []

    for idx, line in enumerate(lines):
        site_match = site_open_re.match(line)
        if site_match:
            current_site = site_match.group("site")
            updated_lines.append(line)
            continue

        url_match = url_line_re.match(line)
        if url_match:
            indent = url_match.group(1)
            old_value = url_match.group(2)
            trailing_space = url_match.group(3) or ""
            trailing_comma = url_match.group(4) or ""
            site_key = current_site or "unknown"

            # se il sito esiste nella mappa remota, proviamo ad aggiornare
            remote_url = remote_map.get(site_key)
            if remote_url:
                final_url = follow_redirect(remote_url)
                if final_url and final_url != normalize_url(old_value):
                    # sostituisco solo la parte tra virgolette
                    new_line = f'{indent}"url": "{final_url}"{trailing_space}{trailing_comma}'
                    updated_lines.append(new_line)
                    changes.append((site_key, old_value, final_url))
                    print(f"✅ {site_key}: {old_value}  →  {final_url}")
                else:
                    # nessuna modifica (redirect fallito o identico)
                    updated_lines.append(line)
                    print(f"ℹ️ {site_key}: nessuna modifica per '{old_value}'")
            else:
                # il sito non è nella lista remota: non tocchiamo la riga
                updated_lines.append(line)
                print(f"ℹ️ {site_key}: nessun URL remoto per questo sito, riga lasciata invariata")
            continue

        # linea normale
        updated_lines.append(line)

    # Scrivo solo se ci sono cambiamenti (ma anche se non ci sono, sovrascrivo per coerenza)
    new_text = "\n".join(updated_lines)
    # preserva newline finale se il file originale ce l'aveva
    if text.endswith("\n") and not new_text.endswith("\n"):
        new_text += "\n"

    local_path.write_text(new_text, encoding="utf-8")
    print("💾 Merge completato: solo le righe 'url' del file locale sono state eventualmente aggiornate.")
    if not changes:
        print("🔎 Nessun cambiamento effettuato.")
    else:
        print("📄 Riepilogo modifiche:")
        for s, old, new in changes:
            print(f" - {s}: {old}  →  {new}")

def main():
    try:
        remote_map = load_remote_urls(REMOTE_RAW_URL)
    except Exception as e:
        print(f"❌ Errore: {e}")
        return

    try:
        merge_remote_into_local(remote_map, LOCAL_CONFIG_PATH)
    except Exception as e:
        print(f"❌ Errore durante il merge: {e}")

if __name__ == "__main__":
    main()

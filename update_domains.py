#!/usr/bin/env python3
# Domain-only updater: modifica SOLO le righe "url" nel config.json locale
import re
import requests
import urllib3
from urllib.parse import urlparse
from datetime import datetime
import shutil
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; DomainUpdater/4.0)"}
CONFIG_PATH = Path("config.json")


def backup_file(path: Path):
    if not path.exists():
        return None
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    bak = path.with_suffix(f".json.bak_{ts}")
    shutil.copy2(path, bak)
    return bak


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    scheme = parsed.scheme if parsed.scheme else "https"
    netloc = parsed.netloc or parsed.path
    return f"{scheme}://{netloc}"


def check_redirect(url: str, timeout=10) -> str | None:
    """Segui redirect e restituisci URL finale normalizzato oppure None."""
    if not url.startswith(("http://", "https://")):
        test = "http://" + url
    else:
        test = url
    try:
        r = requests.get(test, allow_redirects=True, headers=HEADERS, timeout=timeout, verify=False)
        final = r.url
        return normalize_url(final)
    except requests.RequestException as e:
        print(f"⚠️ Redirect fallito per '{url}': {e}")
        return None


def update_only_url_lines(config_path: Path):
    if not config_path.exists():
        print("❌ Errore: config.json locale non trovato.")
        return

    bak = backup_file(config_path)
    if bak:
        print(f"📦 Backup creato: {bak.name}")

    text = config_path.read_text(encoding="utf-8")

    # regex che cattura SOLO la parte "url": "valore"
    url_pattern = re.compile(r'(^\s*"url"\s*:\s*")([^"]+)(")', re.MULTILINE)

    # per sapere il "site key" a scopo di log, identifichiamo l'apertura del blocco sito:
    # es.     "CB01":{
    site_open_re = re.compile(r'^\s*"([^"]+)"\s*:\s*\{\s*$', re.MULTILINE)

    # costruisco una mappa posizione_linea -> site_key scorrendo il file linea per linea
    lines = text.splitlines()
    site_key_for_line = {}
    current_site = None
    for i, line in enumerate(lines):
        m = site_open_re.match(line)
        if m:
            current_site = m.group(1)
        # assegno l'ultimo site visto alla riga corrente (così la riga "url" successiva avrà il site associato)
        site_key_for_line[i] = current_site

    # ora ricreo il testo riga per riga sostituendo SOLO url quando trova redirect valido
    updated_lines = []
    for i, line in enumerate(lines):
        m = url_pattern.search(line)
        if m:
            old_url = m.group(2)
            site_key = site_key_for_line.get(i, "unknown")
            new_url = check_redirect(old_url)
            if new_url and new_url != normalize_url(old_url):
                # sostituisco solo il valore dentro le virgolette, preservando spazi/indentazione
                new_line = url_pattern.sub(rf'\1{new_url}\3', line)
                updated_lines.append(new_line)
                print(f"✅ {site_key}: {old_url}  →  {new_url}")
            else:
                # se redirect non valido o identico, mantengo la riga originale
                updated_lines.append(line)
                print(f"ℹ️ {site_key}: nessuna modifica per '{old_url}'")
        else:
            updated_lines.append(line)

    # scrivo il file (sovrascrivo)
    config_path.write_text("\n".join(updated_lines) + ("\n" if text.endswith("\n") else ""), encoding="utf-8")
    print("💾 Operazione completata: solo le righe 'url' sono state eventualmente aggiornate.")


if __name__ == "__main__":
    update_only_url_lines(CONFIG_PATH)

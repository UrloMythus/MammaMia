import urllib.parse
import Src.Utilities.config as config
import requests
from bs4 import BeautifulSoup

BASE_URL_CALCIO = config.CALCIONEW_DOMAIN
HEADER_CALCIO_PARAMS = "&h_user-agent=Mozilla%2F5.0+%28iPhone%3B+CPU+iPhone+OS+17_7+like+Mac+OS+X%29+AppleWebKit%2F605.1.15+%28KHTML%2C+like+Gecko%29+Version%2F18.0+Mobile%2F15E148+Safari%2F604.1&h_referer=https%3A%2F%2Fcalcionew.newkso.ru%2F&h_origin=https%3A%2F%2Fcalcionew.newkso.ru"

EXTRA_CHANNELS_CALCIO = [("Sky Sport F1 Extra", "calcioXskysportf1/mono.m3u8")]

def _format_channel_name_calcio(raw_name):
    name_part = raw_name.rstrip("/")
    
    server_label = ""
    processed_name_part = name_part

    if name_part.startswith("calcioX1"):
        server_label = " (CT1)"
        processed_name_part = name_part[len("calcioX1"):]
    elif name_part.startswith("calcioX2"):
        server_label = " (CT2)"
        processed_name_part = name_part[len("calcioX2"):]
    elif name_part.startswith("calcioX3"):
        server_label = " (CT3)"
        processed_name_part = name_part[len("calcioX3"):]
    elif name_part.startswith("calcioX"):
        server_label = " (CTX)"
        processed_name_part = name_part[len("calcioX"):]

    name_map = {
        "ac": "Sky Cinema Action",
        "comedycentral": "Comedy Central", "dazn1": "DAZN 1",
        "eurosport1": "Eurosport 1", "eurosport2": "Eurosport 2", "formula": "Formula 1",
        "formula1": "Formula 1", "history": "History", "juve": "Juventus", "laliga": "LaLiga",
        "ligue1": "Ligue 1", "pisa": "Pisa", "porto": "Porto", "portugal": "Portugal", "saler": "Salernitana",
        "samp": "Sampdoria", "sass": "Sassuolo", "serie": "Serie A", "serie1": "Serie A 1",
        "seriesi": "Sky Serie", "sky258": "Sky 258", "sky259": "Sky 259",
        "skyarte": "Sky Arte", "skyatlantic": "Sky Atlantic", "skycinemacollection": "Sky Cinema Collection",
        "skycinemacomedy": "Sky Cinema Comedy", "skycinemadrama": "Sky Cinema Drama",
        "skycinemadue": "Sky Cinema Due", "skycinemafamily": "Sky Cinema Family",
        "skycinemaromance": "Sky Cinema Romance", "skycinemasuspense": "Sky Cinema Suspense",
        "skycinemauno": "Sky Cinema Uno", "skycrime": "Sky Crime", "skydocumentaries": "Sky Documentaries",
        "skyinvestigation": "Sky Investigation", "skynature": "Sky Nature", "skyserie": "Sky Serie",
        "skysport24": "Sky Sport 24", "skysport251": "Sky Sport 251", "skysport252": "Sky Sport 252",
        "skysport253": "Sky Sport 253", "skysport254": "Sky Sport 254", "skysport255": "Sky Sport 255",
        "skysport256": "Sky Sport 256", "skysport257": "Sky Sport 257", "skysportarena": "Sky Sport Arena",
        "skysportcalcio": "Sky Sport Calcio", "skysportgolf": "Sky Sport Golf", "skysportmax": "Sky Sport Max",
        "skysportmotogp": "Sky Sport MotoGP", "skysportnba": "Sky Sport NBA", "skysporttennis": "Sky Sport Tennis",
        "skysportuno": "Sky Sport Uno", "skyuno": "Sky Uno", "solocalcio": "Solo Calcio", "sportitalia": "Sportitalia",
        "zona": "Zona DAZN", "zonab": "Zona B", "dazn1": "Dazn 1"
    }
    
    channel_display_name = name_map.get(processed_name_part.lower(), processed_name_part.capitalize())
    return channel_display_name, server_label

def _fetch_html_content_calcio(url):
    """Scarica il contenuto HTML da un URL specifico per CalcioNew."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        # print(f"Contenuto HTML per CalcioNew scaricato con successo da {url}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Errore durante il download dell'HTML per CalcioNew da {url}: {e}")
        return None

def _parse_channels_from_html_calcio(html_content):
    """Estrae i percorsi dei canali da una stringa HTML per CalcioNew."""
    if not html_content:
        return []
    soup = BeautifulSoup(html_content, 'html.parser')
    channel_paths = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.endswith('/') and href != '../' and '?' not in href:
            channel_paths.append(href)
    return channel_paths

async def get_calcio_streams(client):
    streams = []
    
    # URL da cui scaricare l'HTML (BASE_URL_CALCIO dovrebbe essere "https://calcionew.newkso.ru/calcio/")
    scrape_url = BASE_URL_CALCIO 
    html_content = _fetch_html_content_calcio(scrape_url)
    dynamic_channel_paths = _parse_channels_from_html_calcio(html_content)

    if not dynamic_channel_paths and not EXTRA_CHANNELS_CALCIO:
        print("Nessun canale dinamico trovato e nessun canale extra definito per CalcioNew.")
        return []

    # Processa i canali ottenuti dinamicamente
    for raw_path_part in dynamic_channel_paths:
        try:
            channel_display_name, server_tag_suffix = _format_channel_name_calcio(raw_path_part)
            original_stream_url = f"{BASE_URL_CALCIO}{raw_path_part}mono.m3u8"
            final_url = original_stream_url + HEADER_CALCIO_PARAMS
            
            # Crea un ID univoco per il canale
            # Rimuove "calcio" e lo slash finale, converte in minuscolo
            unique_id_part = raw_path_part.rstrip('/').lower()
            if unique_id_part.startswith("calcio"):
                 unique_id_suffix = unique_id_part[len("calcio"):].lstrip('x123') # Rimuove calcio, calcioX, calcioX1, calcioX2, calcioX3
            else:
                 unique_id_suffix = unique_id_part

            stream_data = {
                'id': f"calcionew-{unique_id_suffix}", 
                'title': f"{channel_display_name}{server_tag_suffix}", 
                'url': final_url,
                'group': "Calcio"
            }
            streams.append(stream_data)
        except Exception as e:
            print(f"Errore nel processare il canale dinamico {raw_path_part} da CalcioNew: {e}")
            continue
    
    # Processa i canali extra
    for extra_name, extra_path_suffix_with_mono in EXTRA_CHANNELS_CALCIO:
        try:
            raw_path_part_for_extra = extra_path_suffix_with_mono.split('/mono.m3u8')[0] + '/'
            _, server_tag_suffix = _format_channel_name_calcio(raw_path_part_for_extra) # Otteniamo il server_tag
            original_stream_url = f"{BASE_URL_CALCIO}{extra_path_suffix_with_mono}"
            final_url = original_stream_url + HEADER_CALCIO_PARAMS
            unique_id_part_extra = raw_path_part_for_extra.rstrip('/').lower()
            if unique_id_part_extra.startswith("calcio"):
                 unique_id_suffix_extra = unique_id_part_extra[len("calcio"):].lstrip('x123')
            else:
                 unique_id_suffix_extra = unique_id_part_extra
            
            stream_data_extra = {
                'id': f"calcionew-{unique_id_suffix_extra}",
                'title': f"{extra_name}{server_tag_suffix}", # Usiamo il nome fornito in EXTRA_CHANNELS_CALCIO
                'url': final_url,
                'group': "Calcio"
            }
            # Evita duplicati se un canale extra è anche trovato dinamicamente con lo stesso ID
            if not any(s['id'] == stream_data_extra['id'] for s in streams):
                streams.append(stream_data_extra)
            # else:
                # print(f"Canale extra CalcioNew {extra_name} (ID: {stream_data_extra['id']}) già presente, saltato.")
        except Exception as e:
            print(f"Errore nel processare il canale extra CalcioNew {extra_name}: {e}")
            continue

    return streams

async def get_calcionew_streams_for_channel_id(channel_id_full: str, client):
    """
    Recupera stream specifici da CalcioNew basati sull'ID completo.
    """
    if not channel_id_full.startswith("calcionew-"):
        return []
    
    channel_name_query = channel_id_full.replace("calcionew-", "").replace("-", " ")
    all_calcio_streams = await get_calcio_streams(client)
    collected_calcio_streams = []
    
    for stream in all_calcio_streams:
        base_title_from_stream = stream['title'].split(' (CT')[0].lower()
        if channel_name_query == base_title_from_stream:
            collected_calcio_streams.append(stream)
    
    return collected_calcio_streams

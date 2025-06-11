import requests # Considera di sostituirlo con client.get() di MammaMia per consistenza
from bs4 import BeautifulSoup
import re
import urllib.parse
import asyncio
import aiohttp

# --- Costanti e Helper da 247ita.py ---
HEADERS_REQUESTS_247ITA = {
    "Accept": "*/*",
    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6,ru;q=0.5",
    "Priority": "u=1, i",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    "Sec-Ch-UA-Mobile": "?0",
    "Sec-Ch-UA-Platform": "Windows",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Storage-Access": "active",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
}
DADDYLIVECHANNELSURL_247ITA = 'https://daddylive.dad/24-7-channels.php'

# Mappa parziale per l'esempio, dovresti completarla come nello script originale
STATIC_LOGOS_247ITA = {
    "sky uno": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-uno-it.png",
    "sky cinema uno": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-cinema-uno-it.png",
    "rai 1": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/rai-1-it.png",
    "rai 2": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/rai-2-it.png",
    "rai 3": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/rai-3-it.png",
    "italia 1": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/italia1-it.png",
    "rete 4": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/rete4-it.png",
    "canale 5": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/canale5-it.png",
    "la7": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/la7-it.png",
    "tv8": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/tv8-it.png",
    "nove": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/nove-it.png",
    "dmax": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/dmax-it.png",
    "real time": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/real-time-it.png",
    "focus": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/focus-it.png",
    "cielo": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/cielo-it.png",
    "sky sport uno": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-sport-uno-it.png",
    "sky sport calcio": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-sport-calcio-it.png",
    "sky sport f1": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-sport-f1-it.png",
    "sky sport motogp": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-sport-motogp-it.png",
    "eurosport 1": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/eurosport-1-it.png",
    "eurosport 2": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/eurosport-2-it.png",
    "dazn 1": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/DAZN_1_Logo.svg/774px-DAZN_1_Logo.svg.png"
    # ... altri loghi
}

def get_247ita_channel_numeric_id(channel_name_query, html_content):
    """
    Cerca l'ID numerico di un canale specifico nell'HTML fornito.
    Restituisce l'ID numerico come stringa, o None se non trovato.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a', href=True)

    # Gestione speciale per DAZN 1
    if "dazn 1" in channel_name_query.lower():
        return "877"

    for link in links:
        link_text_normalized = link.text.strip().lower().replace("italy", "").replace("hd+", "").replace("(251)", "").replace("(252)", "").replace("(253)", "").replace("(254)", "").replace("(255)", "").replace("(256)", "").replace("(257)", "").strip()
        # Potrebbe essere necessario un matching più flessibile qui
        if channel_name_query.lower() in link_text_normalized:
            href = link['href']
            stream_number = href.split('-')[-1].replace('.php', '')
            return stream_number
    return None

async def fetch_247ita_channel_list_html(client):
    """Scarica l'HTML della lista dei canali 247ita."""
    try:
        # Usa il client AsyncSession di MammaMia per coerenza
        response = await client.get(DADDYLIVECHANNELSURL_247ITA, headers=HEADERS_REQUESTS_247ITA)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Errore durante il fetch dell'HTML da 247ita: {e}")
        return None

async def get_247ita_streams(client, mfp_url=None, mfp_password=None):
    """
    Recupera tutti gli stream da 247ita.
    """
    html_content = await fetch_247ita_channel_list_html(client)
    if not html_content:
        return []

    streams = []
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a', href=True)

    # Aggiungi DAZN 1 manualmente se non già presente o per assicurare l'ID corretto
    processed_dazn1 = False

    for link in links:
        if "Italy".lower() in link.text.lower(): # Filtra per canali italiani
            channel_name_original = link.text.strip()
            channel_name_clean = channel_name_original.replace("Italy", "").replace("8", "").replace("(251)", "").replace("(252)", "").replace("(253)", "").replace("(254)", "").replace("(255)", "").replace("(256)", "").replace("(257)", "").replace("HD+", "").strip()
            
            href = link['href']
            stream_number = href.split('-')[-1].replace('.php', '')

            if "dazn 1" in channel_name_clean.lower():
                stream_number = "877" # ID corretto per DAZN 1
                processed_dazn1 = True

            stream_url_dynamic = f"https://daddylive.dad/stream/stream-{stream_number}.php"
            final_url = stream_url_dynamic
            if mfp_url and mfp_password:
                final_url = f"{mfp_url}/extractor/video?host=DLHD&d=&redirect_stream=true&api_password={mfp_password}&d={urllib.parse.quote(stream_url_dynamic)}"
            
            streams.append({
                'id': f"omgtv-247ita-{channel_name_clean.lower().replace(' ', '-')}", # ID per MammaMia
                'title': f"{channel_name_clean} (D)",
                'url': final_url,
                'logo': STATIC_LOGOS_247ITA.get(channel_name_clean.lower(), "https://raw.githubusercontent.com/cribbiox/eventi/refs/heads/main/ddlive.png"),
                'group': "247ita" # Per raggruppamento in MammaMia
            })

    if not processed_dazn1: # Aggiungi DAZN 1 se non trovato nel loop (improbabile ma per sicurezza)
        stream_number_dazn = "877"
        stream_url_dynamic_dazn = f"https://daddylive.dad/stream/stream-{stream_number_dazn}.php"
        final_url_dazn = stream_url_dynamic_dazn
        if mfp_url and mfp_password:
            final_url_dazn = f"{mfp_url}/extractor/video?host=DLHD&d=&redirect_stream=true&api_password={mfp_password}&d={urllib.parse.quote(stream_url_dynamic_dazn)}"
        streams.append({
            'id': "omgtv-247ita-dazn-1",
            'title': "DAZN 1 (D)",
            'url': final_url_dazn,
            'logo': STATIC_LOGOS_247ITA.get("dazn 1"),
            'group': "247ita"
        })
    return streams


async def get_omgtv_streams_for_channel_id(channel_id_full: str, client, mfp_url=None, mfp_password=None):
    """
    Funzione orchestratrice per recuperare uno stream specifico da OMGTV basato sull'ID completo.
    Esempio channel_id_full: "omgtv-247ita-sky-sport-uno"
    """
    parts = channel_id_full.split('-')
    if len(parts) < 3 or parts[0] != "omgtv":
        return [] # ID non valido

    source = parts[1] # es. "247ita"
    channel_name_query = " ".join(parts[2:]) # es. "sky sport uno"

    if source == "247ita":
        # La funzione get_247ita_streams ora restituisce tutti i canali, quindi filtriamo qui.
        all_247ita_streams = await get_247ita_streams(client, mfp_url, mfp_password)
        for stream in all_247ita_streams:
            # Confronto più robusto dell'ID o del titolo
            if channel_name_query.replace("-", " ") in stream['id'].replace("omgtv-247ita-", "").replace("-", " "):
                return [stream] # Restituisce una lista con lo stream trovato
    elif source == "calcio":
        all_calcio_streams = await get_calcio_streams(client, mfp_url, mfp_password)
        for stream in all_calcio_streams:
            if channel_name_query.replace("-", " ") in stream['id'].replace(f"omgtv-{source}-", "").replace("-", " "):
                return [stream]
    elif source == "skystreaming":
        all_skystreaming_streams = await get_skystreaming_streams(client, mfp_url, mfp_password) # client qui è aiohttp session
        for stream in all_skystreaming_streams:
            if channel_name_query.replace("-", " ") in stream['id'].replace(f"omgtv-{source}-", "").replace("-", " "):
                return [stream]
    elif source == "sportstreaming":
        all_sportstreaming_streams = await get_sportstreaming_streams(client, mfp_url, mfp_password)
        for stream in all_sportstreaming_streams:
            if channel_name_query.replace("-", " ") in stream['id'].replace(f"omgtv-{source}-", "").replace("-", " "):
                return [stream]
    elif source == "vavoo":
        all_vavoo_streams = await get_vavoo_streams(client, mfp_url, mfp_password)
        for stream in all_vavoo_streams:
            if channel_name_query.replace("-", " ") in stream['id'].replace(f"omgtv-{source}-", "").replace("-", " "):
                return [stream]
    return []
# --- Logica Calcio ---
BASE_URL_CALCIO = "https://calcionew.newkso.ru/calcio/"
LOGO_URL_CALCIO = "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
HEADER_CALCIO_PARAMS = "&h_user-agent=Mozilla%2F5.0+%28iPhone%3B+CPU+iPhone+OS+17_7+like+Mac+OS+X%29+AppleWebKit%2F605.1.15+%28KHTML%2C+like+Gecko%29+Version%2F18.0+Mobile%2F15E148+Safari%2F604.1&h_referer=https%3A%2F%2Fcalcionew.newkso.ru%2F&h_origin=https%3A%2F%2Fcalcionew.newkso.ru"

CHANNELS_RAW_CALCIO = [
    "Dazn1/", "calcioX1eurosport1/", "calcioX1eurosport2/", "calcioX1formula1/",
    "calcioX1skycinemacollection/", "calcioX1skycinemauno/", "calcioX1skysport24/",
    "calcioX1skysportcalcio/", "calcioX1skysportf1/", "calcioX1skysportmotogp/",
    "calcioX1skysportuno/", "calcioX1skyuno/",
] # Lista ridotta per esempio
EXTRA_CHANNELS_CALCIO = [("Sky Sport F1 Extra", "calcioXskysportf1/mono.m3u8")] # Esempio

def _format_channel_name_calcio(raw_name):
    name = raw_name.rstrip("/")
    for prefix in ["calcioX1", "calcioX2", "calcioX"]:
        if name.startswith(prefix): name = name[len(prefix):]
    name_map = {
        "dazn1": "DAZN 1", "eurosport1": "Eurosport 1", "eurosport2": "Eurosport 2",
        "formula1": "Formula 1", "skycinemacollection": "Sky Cinema Collection",
        "skycinemauno": "Sky Cinema Uno", "skysport24": "Sky Sport 24",
        "skysportcalcio": "Sky Sport Calcio", "skysportf1": "Sky Sport F1",
        "skysportmotogp": "Sky Sport MotoGP", "skysportuno": "Sky Sport Uno", "skyuno": "Sky Uno",
    }
    return name_map.get(name.lower(), name.capitalize())

async def get_calcio_streams(client, mfp_url=None, mfp_password=None):
    streams = []
    raw_channel_list = CHANNELS_RAW_CALCIO + [item[1].split('/mono.m3u8')[0] + '/' for item in EXTRA_CHANNELS_CALCIO]

    for raw_path_part in raw_channel_list:
        channel_name_formatted = _format_channel_name_calcio(raw_path_part)
        original_stream_url = f"{BASE_URL_CALCIO}{raw_path_part}mono.m3u8"
        
        final_url = original_stream_url
        if mfp_url and mfp_password:
            final_url = f"{mfp_url}/proxy/hls/manifest.m3u8?api_password={mfp_password}&d={urllib.parse.quote(original_stream_url)}"
        final_url += HEADER_CALCIO_PARAMS

        channel_id_safe = channel_name_formatted.lower().replace(' ', '-').replace('+', '')
        streams.append({
            'id': f"omgtv-calcio-{channel_id_safe}",
            'title': f"{channel_name_formatted} (CT1)",
            'url': final_url,
            'logo': LOGO_URL_CALCIO,
            'group': "Calcio"
        })
    return streams

# --- Logica SkyStreaming ---
# Nota: SkyStreaming usa aiohttp. MammaMia usa curl_cffi.requests.AsyncSession.
# Per ora, passiamo il client di MammaMia, ma la logica interna di skystreaming
# potrebbe necessitare di adattamenti se usa funzionalità specifiche di aiohttp non presenti in AsyncSession.
# Per semplicità, creo una nuova sessione aiohttp qui, ma l'ideale sarebbe adattare le chiamate.

SKYSTR_SKYSTR = "yoga" # Dovrebbe venire da config o env

BASE_URL_SKYSTREAMING = f"https://skystreaming.{SKYSTR_SKYSTR}"
HEADERS_SKYSTREAMING_AIO = { # Headers per aiohttp
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
   "Accept": "*/*", "Accept-Language": "it-IT,it;q=0.9", "Connection": "keep-alive"
}
SKYSTR_TVG_ID_MAP_SKYSTREAMING = {
   "Eurosport 1": "eurosport1.it", "Sky Sport Tennis": "skysporttennis.it",
} # Mappa ridotta

async def _get_skystreaming_url_details_aio(skystreaming_link, session_aio): # Usa sessione aiohttp
    channel_name_fallback = skystreaming_link.split('/')[-1].split('.')[0].replace('-', ' ')
    try:
        async with session_aio.get(skystreaming_link, headers=HEADERS_SKYSTREAMING_AIO, allow_redirects=True) as response:
            origin_page = urllib.parse.urlparse(str(response.url)).scheme + "://" + urllib.parse.urlparse(str(response.url)).netloc
            html_content = await response.text()
        soup = BeautifulSoup(html_content, 'html.parser')
        h2_tag = soup.find('h2', {'itemprop': 'name'})
        channel_name = h2_tag.get_text(strip=True) if h2_tag else channel_name_fallback
        iframe = soup.find('iframe', src=True)
        if iframe:
            iframe_src = iframe['src']
            if not iframe_src.startswith('http'): iframe_src = urllib.parse.urljoin(BASE_URL_SKYSTREAMING, iframe_src)
            async with session_aio.get(iframe_src, headers=HEADERS_SKYSTREAMING_AIO) as iframe_response:
                iframe_html = await iframe_response.text()
            iframe_soup = BeautifulSoup(iframe_html, 'html.parser')
            source_tag = iframe_soup.find('source', {'type':'application/x-mpegURL'}, src=True)
            if source_tag:
                m3u8_url = source_tag['src']
                return m3u8_url, origin_page, channel_name
        return None, None, channel_name
    except Exception:
        return None, None, channel_name_fallback

async def get_skystreaming_streams(client_mammamia, mfp_url=None, mfp_password=None): # client_mammamia non usato direttamente qui
    streams = []
    # Per SkyStreaming, lo script originale usa aiohttp. Manteniamo questa logica per ora.
    async with aiohttp.ClientSession() as session_aio:
        # Logica semplificata per ottenere alcuni link di canali (dovrebbe essere più robusta)
        # Questa parte dovrebbe replicare extract_category_links e extract_channel_links_from_category
        # Per esempio, hardcodiamo alcuni link per dimostrazione:
        example_channel_pages = [f"{BASE_URL_SKYSTREAMING}/channel/video/eurosport-1", f"{BASE_URL_SKYSTREAMING}/channel/video/sky-sport-tennis"]
        
        tasks = [_get_skystreaming_url_details_aio(url, session_aio) for url in example_channel_pages]
        results = await asyncio.gather(*tasks)

        for m3u8_url, origin_page, channel_name in results:
            if m3u8_url and origin_page:
                final_url = m3u8_url
                if mfp_url and mfp_password:
                    encoded_link = urllib.parse.quote(m3u8_url)
                    user_agent = urllib.parse.quote(HEADERS_SKYSTREAMING_AIO["User-Agent"])
                    referer = urllib.parse.quote(f"{BASE_URL_SKYSTREAMING}/")
                    origin_header_val = urllib.parse.quote(BASE_URL_SKYSTREAMING)
                    final_url = f"{mfp_url}/proxy/hls/manifest.m3u8?api_password={mfp_password}&d={encoded_link}&h_user-agent={user_agent}&h_referer={referer}&h_origin={origin_header_val}"

                channel_id_safe = channel_name.lower().replace(' ', '-').replace('+', '')
                streams.append({
                    'id': f"omgtv-skystreaming-{channel_id_safe}",
                    'title': f"{channel_name} (SS)",
                    'url': final_url,
                    'logo': f"{BASE_URL_SKYSTREAMING}/content/auto_site_logo.png", # Logo generico
                    'group': "SkyStreaming"
                })
    return streams

# --- Logica SportStreaming ---
BASE_URL_SPORTSTREAMING = "https://www.sportstreaming.net/"
HEADERS_SPORTSTREAMING = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1",
    "Origin": "https://www.sportstreaming.net", "Referer": "https://www.sportstreaming.net/"
}
TEMP_CHANNEL_LOGO_SPORTSTREAMING = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"

async def _get_event_details_sportstreaming(event_url, client): # Usa client MammaMia
    try:
        response = await client.get(event_url, headers=HEADERS_SPORTSTREAMING) # Adattato per client
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        stream_url = None
        for iframe in soup.find_all('iframe', src=True):
            src = iframe.get('src')
            if src and ("stream" in src.lower() or re.search(r'\.(m3u8|mp4|ts|html|php)', src, re.IGNORECASE)):
                stream_url = src; break
        # ... (logica di fallback per embed, video come nell'originale) ...
        title_tag = soup.find('title')
        event_title = title_tag.get_text(strip=True).replace("| Sport Streaming", "").strip() if title_tag else "Unknown Event"
        return stream_url, event_title
    except Exception:
        return None, "Unknown Event"

async def get_sportstreaming_streams(client, mfp_url=None, mfp_password=None):
    streams = []
    # Logica semplificata per ottenere pagine evento (dovrebbe essere più robusta)
    example_event_pages = [f"{BASE_URL_SPORTSTREAMING}/live-perma-1", f"{BASE_URL_SPORTSTREAMING}/live-temp-1"]

    for event_page_url in example_event_pages:
        original_stream_url, event_title = await _get_event_details_sportstreaming(event_page_url, client)
        if original_stream_url:
            final_url = original_stream_url
            if mfp_url and mfp_password:
                encoded_ua = urllib.parse.quote_plus(HEADERS_SPORTSTREAMING["User-Agent"])
                encoded_referer = urllib.parse.quote_plus(HEADERS_SPORTSTREAMING["Referer"])
                encoded_origin = urllib.parse.quote_plus(HEADERS_SPORTSTREAMING["Origin"])
                final_url = f"{mfp_url}/proxy/hls/manifest.m3u8?api_password={mfp_password}&d={urllib.parse.quote(original_stream_url)}&h_user-agent={encoded_ua}&h_referer={encoded_referer}&h_origin={encoded_origin}"

            channel_id_safe = event_title.lower().replace(' ', '-').replace('+', '')
            logo = TEMP_CHANNEL_LOGO_SPORTSTREAMING if "live-temp" in event_page_url else "https://sportstreaming.net/assets/img/live/standard/live1.png"
            streams.append({
                'id': f"omgtv-sportstreaming-{channel_id_safe}",
                'title': f"{event_title} (SpS)",
                'url': final_url,
                'logo': logo,
                'group': "SportStreaming"
            })
    return streams

# --- Logica Vavoo ---
BASE_URL_VAVOO = "https://vavoo.to"
HEADER_VAVOO_PARAMS = "&h_user-agent=VAVOO/2.6&h_referer=https://vavoo.to/"
CHANNEL_LOGOS_VAVOO = { "sky uno": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-uno-it.png", "rai 1": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/rai-1-it.png" } # Mappa ridotta

def _clean_channel_name_vavoo(name):
    name = re.sub(r"\s*(\|E|\|H|\(6\)|\(7\)|\.c|\.s)\s*", "", name)
    return f"{name}" # (V) aggiunto al titolo

async def get_vavoo_streams(client, mfp_url=None, mfp_password=None):
    streams = []
    try:
        response = await client.get(f"{BASE_URL_VAVOO}/channels", timeout=10) # Adattato per client
        response.raise_for_status()
        channels_list = response.json()
    except Exception:
        return []

    for ch_data in channels_list:
        if ch_data.get("country") == "Italy": # Filtro base
            original_name = _clean_channel_name_vavoo(ch_data["name"])
            original_stream_url = f"{BASE_URL_VAVOO}/play/{ch_data['id']}/index.m3u8"
            
            final_url = original_stream_url
            if mfp_url and mfp_password:
                final_url = f"{mfp_url}/proxy/hls/manifest.m3u8?api_password={mfp_password}&d={urllib.parse.quote(original_stream_url)}"
            final_url += HEADER_VAVOO_PARAMS
            
            channel_id_safe = original_name.lower().replace(' ', '-').replace('+', '')
            logo_key = original_name.lower().split(' (v)')[0].strip() # Per cercare nel dizionario loghi
            streams.append({
                'id': f"omgtv-vavoo-{channel_id_safe}",
                'title': f"{original_name} (V)",
                'url': final_url,
                'logo': CHANNEL_LOGOS_VAVOO.get(logo_key, "https://www.vavoo.tv/software/images/logo.png"), # Fallback logo Vavoo
                'group': "Vavoo"
            })
    return streams
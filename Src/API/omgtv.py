from bs4 import BeautifulSoup
import re
import urllib.parse
import asyncio

import Src.Utilities.config as config # Added to use SKY_DOMAIN

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
    "sky sport f1": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-sport-f1-it.png", # Keep existing
    "sky sport motogp": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-sport-motogp-it.png",
    "eurosport 1": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/eurosport-1-it.png",
    "eurosport 2": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/eurosport-2-it.png",
    "dazn 1": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/DAZN_1_Logo.svg/774px-DAZN_1_Logo.svg.png",
    "sky sport 251": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png",
    "sky sport 252": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png",
    "sky sport 253": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png",
    "sky sport 254": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png",
    "sky sport 255": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png",
    "sky sport 256": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png",
    "sky sport 257": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png",
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

DADDYLIVE_CHANNEL_NAME_MAP = {
    "sky calcio 1": "Sky Sport 251",
    "skycalcio1": "Sky Sport 251",
    "sky calcio1": "Sky Sport 251",
    "sky sport calcio 1": "Sky Sport 251",
    "sky calcio 2": "Sky Sport 252",
    "skycalcio2": "Sky Sport 252",
    "sky calcio2": "Sky Sport 252",
    "sky sport calcio 2": "Sky Sport 252",
    "sky calcio 3": "Sky Sport 253",
    "skycalcio3": "Sky Sport 253",
    "sky calcio3": "Sky Sport 253",
    "sky sport calcio 3": "Sky Sport 253",
    "sky calcio 4": "Sky Sport 254",
    "skycalcio4": "Sky Sport 254",
    "sky calcio 5": "Sky Sport 255",
    "skycalcio5": "Sky Sport 255",
    "sky calcio 6": "Sky Sport 256",
    "skycalcio6": "Sky Sport 256",
    "sky calcio 7": "Sky Sport 257",
    "skycalcio7": "Sky Sport 257",
    # Aggiungere altre varianti se DaddyLive usa nomi come "sky sport calcio 1", ecc.
}

async def fetch_247ita_channel_list_html(client):
    """Scarica l'HTML della lista dei canali 247ita."""
    try:
        # Usa il client AsyncSession di MammaMia per coerenza
        response = await client.get(DADDYLIVECHANNELSURL_247ITA, headers=HEADERS_REQUESTS_247ITA, impersonate="chrome120")
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
            channel_name_original_from_link = link.text.strip() # Es. "Sky Calcio 1 Italy HD+"
            # print(f"DEBUG: DaddyLive Original Name: {channel_name_original_from_link}") # LOG

            # Nome da usare per il lookup nella mappa DADDYLIVE_CHANNEL_NAME_MAP.
            # Rimuoviamo "Italy", "HD+", numeri tra parentesi e convertiamo in lowercase per un matching più flessibile.
            name_for_map_lookup = channel_name_original_from_link.replace("Italy", "") \
                                                                .replace("HD+", "") \
                                                                .replace("(251)", "").replace("(252)", "").replace("(253)", "") \
                                                                .replace("(254)", "").replace("(255)", "").replace("(256)", "") \
                                                                .replace("(257)", "") \
                                                                .strip().lower()
            # print(f"DEBUG: DaddyLive Name for Map Lookup: {name_for_map_lookup}") # LOG

            mapped_name = DADDYLIVE_CHANNEL_NAME_MAP.get(name_for_map_lookup)

            if mapped_name:
                # Se abbiamo una mappatura (es. "sky calcio 1" -> "Sky Sport 251"), usiamo quella.
                channel_name_final_display = mapped_name
            else:
                # Altrimenti, applichiamo la pulizia più generale.
                channel_name_final_display = channel_name_original_from_link.replace("Italy", "") \
                                                                        .replace("8", "") \
                                                                        .replace("(251)", "").replace("(252)", "").replace("(253)", "") \
                                                                        .replace("(254)", "").replace("(255)", "").replace("(256)", "") \
                                                                        .replace("(257)", "") \
                                                                        .replace("HD+", "").strip()

            href = link['href']
            stream_number = href.split('-')[-1].replace('.php', '')

            if "dazn 1" in channel_name_final_display.lower(): # Usa il nome finale per il check
                stream_number = "877" # ID corretto per DAZN 1
                processed_dazn1 = True

            stream_url_dynamic = f"https://daddylive.dad/stream/stream-{stream_number}.php"
            final_url = stream_url_dynamic
            if mfp_url and mfp_password:
                final_url = f"{mfp_url}/extractor/video?host=DLHD&redirect_stream=true&api_password={mfp_password}&d={urllib.parse.quote(stream_url_dynamic)}"
            
            streams.append({
                'id': f"omgtv-247ita-{channel_name_final_display.lower().replace(' ', '-')}",
                'title': f"{channel_name_final_display} (D)",
                'url': final_url,
                'logo': STATIC_LOGOS_247ITA.get(channel_name_final_display.lower(), "https://raw.githubusercontent.com/cribbiox/eventi/refs/heads/main/ddlive.png"),
                'group': "247ita" # Per raggruppamento in MammaMia
            })

    if not processed_dazn1: # Aggiungi DAZN 1 se non trovato nel loop (improbabile ma per sicurezza)
        stream_number_dazn = "877"
        stream_url_dynamic_dazn = f"https://daddylive.dad/stream/stream-{stream_number_dazn}.php"
        final_url_dazn = stream_url_dynamic_dazn
        if mfp_url and mfp_password:
            final_url_dazn = f"{mfp_url}/extractor/video?host=DLHD&redirect_stream=true&api_password={mfp_password}&d={urllib.parse.quote(stream_url_dynamic_dazn)}"
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

        # channel_name_query è il nome richiesto, es. "sky calcio 1" o "sky sport 251"
        query_normalized_for_map_lookup = channel_name_query.lower() # es. "sky calcio 1"
        
        # Controlla se il nome richiesto è una chiave nella mappa di DaddyLive.
        # Se sì, usa il nome mappato per il confronto. Altrimenti, usa il nome originale.
        # es. se query_normalized_for_map_lookup è "sky calcio 1", target_channel_name_for_id_match diventa "sky sport 251"
        # es. se query_normalized_for_map_lookup è "sky sport 251", target_channel_name_for_id_match rimane "sky sport 251"
        target_channel_name_for_id_match = DADDYLIVE_CHANNEL_NAME_MAP.get(query_normalized_for_map_lookup, channel_name_query).lower()
        target_id_part_to_match = target_channel_name_for_id_match.replace(" ", "-")

        for stream in all_247ita_streams:
            # stream['id'] è es. "omgtv-247ita-sky-sport-251"
            # Estrai la parte del nome dall'ID dello stream: es. "sky-sport-251"
            stream_id_name_part = stream['id'].replace("omgtv-247ita-", "")
            if target_id_part_to_match == stream_id_name_part:
                return [stream] # Restituisce una lista con lo stream trovato

    elif source == "calcio":
        all_calcio_streams = await get_calcio_streams(client, mfp_url, mfp_password)
        collected_calcio_streams = []
        # channel_name_query è es. "sky nature" (dall'ID "omgtv-calcio-sky-nature")
        for stream in all_calcio_streams:
            # stream['title'] è es. "Sky Nature (CT1)"
            # Estrai il nome base del canale dal titolo dello stream generato per il confronto
            base_title_from_stream = stream['title'].split(' (CT')[0].lower()
            if channel_name_query == base_title_from_stream:
                collected_calcio_streams.append(stream)
        return collected_calcio_streams # Restituisce la lista di tutti gli stream calcio corrispondenti

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

 "calcioX1ac/", "calcioX1comedycentral/",
    "calcioX1eurosport1/", "calcioX1eurosport2/", "calcioX1formula1/", "calcioX1history/",
    "calcioX1seriesi/", "calcioX1sky258/", "calcioX1sky259/", "calcioX1skyatlantic/",
    "calcioX1skycinemacollection/", "calcioX1skycinemacomedy/", "calcioX1skycinemadrama/",
    "calcioX1skycinemadue/", "calcioX1skycinemafamily/", "calcioX1skycinemaromance/",
    "calcioX1skycinemasuspence/", "calcioX1skycinemauno/", "calcioX1skycrime/",
    "calcioX1skydocumentaries/", "calcioX1skyinvestigation/", "calcioX1skynature/",
    "calcioX1skyserie/", "calcioX1skysport24/", "calcioX1skysport251/",
    "calcioX1skysport252/", "calcioX1skysport253/", "calcioX1skysport254/",
    "calcioX1skysport255/", "calcioX1skysport257/", "calcioX1skysportarena/",
    "calcioX1skysportcalcio/", "calcioX1skysportgolf/", "calcioX1skysportmax/",
    "calcioX1skysportmotogp/", "calcioX1skysportnba/", "calcioX1skysporttennis/",
    "calcioX1skysportuno/", "calcioX1skyuno/", "calcioX2ac/", "calcioX2comedycentral/",
    "calcioX2eurosport1/", "calcioX2eurosport2/", "calcioX2formula/", "calcioX2formula1/",
    "calcioX2history/", "calcioX2laliga/", "calcioX2porto/", "calcioX2portugal/",
    "calcioX2serie/", "calcioX2serie1/", "calcioX2seriesi/", "calcioX2sky258/",
    "calcioX2sky259/", "calcioX2skyarte/", "calcioX2skyatlantic/", "calcioX2skycinemacollection/",
    "calcioX2skycinemacomedy/", "calcioX2skycinemadrama/", "calcioX2skycinemadue/",
    "calcioX2skycinemafamily/", "calcioX2skycinemaromance/", "calcioX2skycinemasuspence/",
    "calcioX2skycinemauno/", "calcioX2skycrime/", "calcioX2skydocumentaries/",
    "calcioX2skyinvestigation/", "calcioX2skynature/", "calcioX2skyserie/",
    "calcioX2skysport24/", "calcioX2skysport251/", "calcioX2skysport252/",
    "calcioX2skysport253/", "calcioX2skysport254/", "calcioX2skysport255/",
    "calcioX2skysport256/", "calcioX2skysport257/", "calcioX2skysportarena/",
    "calcioX2skysportcalcio/", "calcioX2skysportgolf/", "calcioX2skysportmax/",
    "calcioX2skysportmotogp/", "calcioX2skysportnba/", "calcioX2skysporttennis/",
    "calcioX2skysportuno/", "calcioX2skyuno/", "calcioX2solocalcio/", "calcioX2sportitalia/",
    "calcioX2zona/", "calcioX2zonab/", "calcioXac/", "calcioXcomedycentral/",
    "calcioXeurosport1/", "calcioXeurosport2/", "calcioXformula1/", "calcioXhistory/",
    "calcioXseriesi/", "calcioXsky258/", "calcioXsky259/", "calcioXskyarte/",
    "calcioXskyatlantic/", "calcioXskycinemacollection/", "calcioXskycinemacomedy/",
    "calcioXskycinemadrama/", "calcioXskycinemadue/", "calcioXskycinemafamily/",
    "calcioXskycinemaromance/", "calcioXskycinemasuspence/", "calcioXskycinemauno/",
    "calcioXskycrime/", "calcioXskydocumentaries/", "calcioXskyinvestigation/",
    "calcioXskynature/", "calcioXskyserie/", "calcioXskysport24/", "calcioXskysport251/",
    "calcioXskysport252/", "calcioXskysport253/", "calcioXskysport254/",
    "calcioXskysport255/", "calcioXskysport256/", "calcioXskysport257/",
    "calcioXskysportarena/", "calcioXskysportcalcio/", "calcioXskysportgolf/",
    "calcioXskysportmax/", "calcioXskysportmotogp/", "calcioXskysportnba/",
    "calcioXskysporttennis/", "calcioXskysportuno/", "calcioXskyuno/"
] # Lista ridotta per esempio
EXTRA_CHANNELS_CALCIO = [("Sky Sport F1 Extra", "calcioXskysportf1/mono.m3u8")] # Esempio

def _format_channel_name_calcio(raw_name):
    name_part = raw_name.rstrip("/") # e.g. "calcioX1skynature"
    
    server_label = ""
    processed_name_part = name_part

    if name_part.startswith("calcioX1"):
        server_label = " (CT1)"
        processed_name_part = name_part[len("calcioX1"):] # e.g. "skynature"
    elif name_part.startswith("calcioX2"):
        server_label = " (CT2)"
        processed_name_part = name_part[len("calcioX2"):]
    elif name_part.startswith("calcioX3"): # Must be after X1 and X2 checks
        server_label = " (CT3)"
        processed_name_part = name_part[len("calcioX3"):]
    elif name_part.startswith("calcioX"): # Must be after X1 and X2 checks
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
        "zona": "Zona DAZN", "zonab": "Zona B"
    }
    channel_display_name = name_map.get(processed_name_part.lower(), processed_name_part.capitalize())
    return channel_display_name, server_label

async def get_calcio_streams(client, mfp_url=None, mfp_password=None):
    # print("DEBUG: Entrando in get_calcio_streams") # LOG
    streams = []
    raw_channel_list = CHANNELS_RAW_CALCIO + [item[1].split('/mono.m3u8')[0] + '/' for item in EXTRA_CHANNELS_CALCIO]

    if not raw_channel_list:
        # print("DEBUG: raw_channel_list è vuota in get_calcio_streams") # LOG
        return []

    # print(f"DEBUG: raw_channel_list ha {len(raw_channel_list)} elementi.") # LOG

    for raw_path_part in raw_channel_list:
        try:
            channel_display_name, server_tag_suffix = _format_channel_name_calcio(raw_path_part)
            original_stream_url = f"{BASE_URL_CALCIO}{raw_path_part}mono.m3u8"
            
            final_url = original_stream_url
            if mfp_url and mfp_password:
                final_url = f"{mfp_url}/proxy/hls/manifest.m3u8?api_password={mfp_password}&d={urllib.parse.quote(original_stream_url)}"
            final_url += HEADER_CALCIO_PARAMS
            
            unique_id_suffix = raw_path_part.rstrip('/').replace("calcio", "").lower()

            stream_data = {
                'id': f"omgtv-calcio-{unique_id_suffix}", 
                'title': f"{channel_display_name}{server_tag_suffix}", 
                'url': final_url,
                'logo': LOGO_URL_CALCIO,
                'group': "Calcio"
            }
            streams.append(stream_data)
            # print(f"DEBUG: Aggiunto stream calcio: {stream_data['id']} - {stream_data['title']}") # LOG
        except Exception as e:
            # print(f"DEBUG: Errore durante il processamento di {raw_path_part} in get_calcio_streams: {e}") # LOG
            continue # Continua con il prossimo canale
            
    # print(f"DEBUG: Uscendo da get_calcio_streams, {len(streams)} streams generati.") # LOG
    return streams


# --- Logica Vavoo ---
BASE_URL_VAVOO = "https://vavoo.to"
HEADER_VAVOO_PARAMS = "&h_user-agent=VAVOO/2.6&h_referer=https://vavoo.to/"

VAVOO_CHANNEL_NAME_MAP = {
    "sky calcio 1": "Sky Sport 251",
    "sky calcio 2": "Sky Sport 252",
    "sky calcio 3": "Sky Sport 253",
    "sky calcio 4": "Sky Sport 254",
    "sky calcio 5": "Sky Sport 255",
    "sky calcio 6": "Sky Sport 256",
    "sky calcio 7": "Sky Sport 257",
    # Aggiungere altre mappature specifiche di Vavoo se necessario
}

CHANNEL_LOGOS_VAVOO = {
    "sky uno": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-uno-it.png",
    "rai 1": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/rai-1-it.png",
    "sky sport 251": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png",
    "sky sport 252": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png",
    "sky sport 253": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png",
    "sky sport 254": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png",
    "sky sport 255": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png",
    "sky sport 256": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png",
    "sky sport 257": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png",
    "sky cinema uno": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-cinema-uno-it.png",
    "rai 2": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/rai-2-it.png",
    "rai 3": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/rai-3-it.png",
    "italia 1": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/italia1-it.png",
    "rete 4": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/rete4-it.png",
    "canale 5": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/canale5-it.png",
    "la7": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/la7-it.png",
    "tv8": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/tv8-it.png",
    "nove": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/nove-it.png",
    "sky sport uno": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-sport-uno-it.png",
    "sky sport calcio": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-sport-calcio-it.png",
    # Aggiungere altri loghi necessari
}

def _clean_channel_name_vavoo(name):
    name = re.sub(r"\s*(\|E|\|H|\(6\)|\(7\)|\.c|\.s)\s*", "", name)
    return f"{name}" # (V) aggiunto al titolo

async def get_vavoo_streams(client, mfp_url=None, mfp_password=None):
    streams = []
    try:
        response = await client.get(f"{BASE_URL_VAVOO}/channels", timeout=10, impersonate="chrome120")
        response.raise_for_status()
        channels_list = response.json()
    except Exception as e:
        print(f"Error fetching Vavoo channel list: {e}")

        return []

    for ch_data in channels_list:
        if ch_data.get("country") == "Italy": # Filtro base
            raw_name_from_vavoo = ch_data["name"].strip()

            # Applica la mappatura specifica di Vavoo se il nome grezzo (lowercase) è nel map
            # Il nome per il display e per la logica interna sarà quello mappato (es. "Sky Sport 251")
            # o quello originale se non c'è mappatura.
            effective_channel_name = VAVOO_CHANNEL_NAME_MAP.get(raw_name_from_vavoo.lower(), raw_name_from_vavoo)

            # Pulisci ulteriormente l'effective_channel_name e preparalo per il display
            cleaned_effective_name = _clean_channel_name_vavoo(effective_channel_name)

            original_stream_url = f"{BASE_URL_VAVOO}/play/{ch_data['id']}/index.m3u8"
            
            final_url = original_stream_url
            if mfp_url and mfp_password:
                final_url = f"{mfp_url}/proxy/hls/manifest.m3u8?api_password={mfp_password}&d={urllib.parse.quote(original_stream_url)}"
            final_url += HEADER_VAVOO_PARAMS

            channel_id_safe = cleaned_effective_name.lower().replace(' ', '-').replace('+', '')
            logo_key_for_dict = cleaned_effective_name.lower()

            streams.append({
                'id': f"omgtv-vavoo-{channel_id_safe}",
                'title': f"{cleaned_effective_name} (V)",
                'url': final_url,
                'logo': CHANNEL_LOGOS_VAVOO.get(logo_key_for_dict, "https://www.vavoo.tv/software/images/logo.png"), # Fallback logo Vavoo
                'group': "Vavoo"
            })
    return streams

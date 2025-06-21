from bs4 import BeautifulSoup
import urllib.parse
import Src.Utilities.config as config

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

DADDYLIVECHANNELSURL_247ITA = f'{config.DLHD_DOMAIN}/24-7-channels.php'


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
}

async def fetch_247ita_channel_list_html(client):
    """Scarica l'HTML della lista dei canali 247ita."""
    try:
        response = await client.get(DADDYLIVECHANNELSURL_247ITA, headers=HEADERS_REQUESTS_247ITA, impersonate="chrome120")
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Errore durante il fetch dell'HTML da 247ita: {e}")
        return None

async def get_247ita_streams(client):
    """
    Recupera tutti gli stream da 247ita senza MFP.
    """
    html_content = await fetch_247ita_channel_list_html(client)
    if not html_content:
        return []

    streams = []
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a', href=True)

    processed_dazn1 = False

    for link in links:
        if "Italy".lower() in link.text.lower():
            channel_name_original_from_link = link.text.strip()
            
            name_for_map_lookup = channel_name_original_from_link.replace("Italy", "") \
                                                                .replace("HD+", "") \
                                                                .replace("(251)", "").replace("(252)", "").replace("(253)", "") \
                                                                .replace("(254)", "").replace("(255)", "").replace("(256)", "") \
                                                                .replace("(257)", "") \
                                                                .strip().lower()

            mapped_name = DADDYLIVE_CHANNEL_NAME_MAP.get(name_for_map_lookup)

            if mapped_name:
                channel_name_final_display = mapped_name
            else:
                channel_name_final_display = channel_name_original_from_link.replace("Italy", "") \
                                                                        .replace("8", "") \
                                                                        .replace("(251)", "").replace("(252)", "").replace("(253)", "") \
                                                                        .replace("(254)", "").replace("(255)", "").replace("(256)", "") \
                                                                        .replace("(257)", "") \
                                                                        .replace("HD+", "").strip()

            href = link['href']
            stream_number = href.split('-')[-1].replace('.php', '')

            if "dazn 1" in channel_name_final_display.lower():
                stream_number = "877"
                processed_dazn1 = True

            stream_url_dynamic = f"{config.DLHD_DOMAIN}/stream/stream-{stream_number}.php"
            
            streams.append({
                'id': f"{channel_name_final_display.lower().replace(' ', '-')}",
                'title': f"{channel_name_final_display} (D)",
                'url': stream_url_dynamic,
                'group': "247ita"
            })

    if not processed_dazn1:
        stream_number_dazn = "877"
        stream_url_dynamic_dazn = f"{config.DLHD_DOMAIN}/stream/stream-{stream_number_dazn}.php"
        streams.append({
            'id': "dazn-1",
            'title': "DAZN 1 (D)",
            'url': stream_url_dynamic_dazn,
            'group': "247ita"
        })
    return streams

async def get_daddy_streams_for_channel_id(channel_id_full: str, client):
    """
    Recupera uno stream specifico da Daddy basato sull'ID completo.
    """
    if not channel_id_full.startswith("dlhd-"):
        return []
    
    channel_name_query = channel_id_full.replace("dlhd-", "").replace("-", " ")
    all_247ita_streams = await get_247ita_streams(client)
    
    query_normalized_for_map_lookup = channel_name_query.lower()
    target_channel_name_for_id_match = DADDYLIVE_CHANNEL_NAME_MAP.get(query_normalized_for_map_lookup, channel_name_query).lower()
    target_id_part_to_match = target_channel_name_for_id_match.replace(" ", "-")

    for stream in all_247ita_streams:
        stream_id_name_part = stream['id']
        if target_id_part_to_match == stream_id_name_part:
            return [stream]
    
    return []

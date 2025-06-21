import re
import urllib.parse
import Src.Utilities.config as config

BASE_URL_VAVOO = config.VAVOO_DOMAIN
HEADER_VAVOO_PARAMS = "&h_user-agent=VAVOO/2.6&h_referer=https://vavoo.to/"

VAVOO_CHANNEL_NAME_MAP = {
    "sky calcio 1": "Sky Sport 251",
    "sky calcio 2": "Sky Sport 252",
    "sky calcio 3": "Sky Sport 253",
    "sky calcio 4": "Sky Sport 254",
    "sky calcio 5": "Sky Sport 255",
    "sky calcio 6": "Sky Sport 256",
    "sky calcio 7": "Sky Sport 257",
}


def _clean_channel_name_vavoo(name):
    name = re.sub(r"\s*(\|E|\|H|\(6\)|\(7\)|\.c|\.s)\s*", "", name)
    return f"{name}"

async def get_vavoo_streams(client):
    streams = []
    try:
        response = await client.get(f"{BASE_URL_VAVOO}/channels", timeout=10, impersonate="chrome120")
        response.raise_for_status()
        channels_list = response.json()
    except Exception as e:
        print(f"Error fetching Vavoo channel list: {e}")
        return []

    for ch_data in channels_list:
        if ch_data.get("country") == "Italy":
            raw_name_from_vavoo = ch_data["name"].strip()
            effective_channel_name = VAVOO_CHANNEL_NAME_MAP.get(raw_name_from_vavoo.lower(), raw_name_from_vavoo)
            cleaned_effective_name = _clean_channel_name_vavoo(effective_channel_name)

            original_stream_url = f"{BASE_URL_VAVOO}/play/{ch_data['id']}/index.m3u8"
            final_url = original_stream_url + HEADER_VAVOO_PARAMS

            channel_id_safe = cleaned_effective_name.lower().replace(' ', '-').replace('+', '')

            streams.append({
                'id': f"{channel_id_safe}",
                'title': f"{cleaned_effective_name} (V)",
                'url': final_url,
                'group': "Vavoo"
            })

    return streams

async def get_vavoo_streams_for_channel_id(channel_id_full: str, client):
    """
    Recupera uno stream specifico da Vavoo basato sull'ID completo.
    """
    if not channel_id_full.startswith("vavoo-"):
        return []
    
    channel_name_query = channel_id_full.replace("vavoo-", "").replace("-", " ")
    all_vavoo_streams = await get_vavoo_streams(client)
    
    for stream in all_vavoo_streams:
        stream_id_normalized_for_match = stream['id'].replace("-", " ")
        
        # Usiamo '==' per un match esatto dopo la normalizzazione
        if channel_name_query == stream_id_normalized_for_match:
            return [stream]
        
    return []

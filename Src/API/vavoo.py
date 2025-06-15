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
            logo_key_for_dict = cleaned_effective_name.lower()

            streams.append({
                'id': f"vavoo-{channel_id_safe}",
                'title': f"{cleaned_effective_name} (V)",
                'url': final_url,
                'logo': CHANNEL_LOGOS_VAVOO.get(logo_key_for_dict, "https://vavoo.to/favicon.ico"),
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
        if channel_name_query in stream['id'].replace("vavoo-", "").replace("-", " "):
            return [stream]
    
    return []
import urllib.parse
import Src.Utilities.config as config

BASE_URL_CALCIO = config.CALCIONEW_DOMAIN
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
]

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
        "zona": "Zona DAZN", "zonab": "Zona B"
    }
    
    channel_display_name = name_map.get(processed_name_part.lower(), processed_name_part.capitalize())
    return channel_display_name, server_label

async def get_calcio_streams(client):
    streams = []
    raw_channel_list = CHANNELS_RAW_CALCIO + [item[1].split('/mono.m3u8')[0] + '/' for item in EXTRA_CHANNELS_CALCIO]

    if not raw_channel_list:
        return []

    for raw_path_part in raw_channel_list:
        try:
            channel_display_name, server_tag_suffix = _format_channel_name_calcio(raw_path_part)
            original_stream_url = f"{BASE_URL_CALCIO}{raw_path_part}mono.m3u8"
            final_url = original_stream_url + HEADER_CALCIO_PARAMS
            
            unique_id_suffix = raw_path_part.rstrip('/').replace("calcio", "").lower()

            stream_data = {
                'id': f"calcionew-{unique_id_suffix}", 
                'title': f"{channel_display_name}{server_tag_suffix}", 
                'url': final_url,
                'logo': LOGO_URL_CALCIO,
                'group': "Calcio"
            }
            streams.append(stream_data)
        except Exception as e:
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
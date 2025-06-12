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

# --- Definizione Canali Statici Interni ---
STATIC_CHANNELS_DATA = [
    {
        "id": "sky-uno", # ID originale del canale
        "title": "Sky Uno",
        "url": "https://linear313-it-dash1-prd.selector.skycdn.it/016a/32477/FHD/skyuno/master.mpd&key_id=003610b8556000936e48061cdb4ee11a&key=2cd6bcc2160aa6ec048e5a5f7a0f73c8",
        "group": "MPD"
    },
    {
        "id": "sky-atlantic",
        "title": "Sky Atlantic",
        "url": "https://linear315-it-dash1-prd-akp2.cdn13.skycdp.com/016a/31226/FHD/skyatlantic/master.mpd&key_id=0036d37875a7307fd4551bcd6e466882&key=a8cdc74a5d05c7a45c551af45aa5549c",
        "group": "MPD"
    },
    {
        "id": "sky-sport-24",
        "title": "Sky Sport 24",
        "url": "https://linear303-it-dash1-prd.selector.skycdn.it/016a/31035/FHD/skysport24/master.mpd&key_id=003663ddf1acb25ea88a7cf973afc0d5&key=35ea91b4151d6975007998c328daee6c",
        "group": "MPD"
    },
    {
        "id": "sky-sport-uno",
        "title": "Sky Sport Uno",
        "url": "https://linear301-it-dash1-prd.selector.skycdn.it/016a/31023/FHD/skysportuno/master.mpd&key_id=0036aaa1d68c6b487e29a5cb080a8a28&key=a3e8db3ff3c876f7b43a961b64a63474",
        "group": "MPD"
    },
    {
        "id": "sky-sport-calcio",
        "title": "Sky Sport Calcio",
        "url": "https://linear302-it-dash1-prd.selector.skycdn.it/016a/31209/FHD/skysportseriea/master.mpd&key_id=00362f95db61eba0e6f14acee3f71e01&key=fb74cd84b53c7557e18424a3356c4665",
        "group": "MPD"
    },
    {
        "id": "sky-sport-f1",
        "title": "Sky Sport F1",
        "url": "https://linear307-it-dash1-prd.selector.skycdn.it/016a/31478/FHD/skysportf1/master.mpd&key_id=0036a96b6bbbf1828488f90e6b2ca1f4&key=d24e6ae926e88f8303b6926271ff8155",
        "group": "MPD"
    },
    {
        "id": "sky-sport-motogp",
        "title": "Sky Sport MotoGP",
        "url": "https://linear306-it-dash1-prd.selector.skycdn.it/016a/31483/FHD/skysportmotogp/master.mpd&key_id=00362e9181eaa0c5f91761ade3515eb8&key=52cf3c27885d58ad76aaf36d4217a984",
        "group": "MPD"
    },
    {
        "id": "sky-sport-arena",
        "title": "Sky Sport Arena",
        "url": "https://linear304-it-dash1-prd-akp2.cdn13.skycdp.com/016a/31024/FHD/skysportarena/master.mpd&key_id=00368f2bf10736c9c2c02ab0fa694d00&key=92eec9d841ac0c1ff16b90a0db82c792",
        "group": "MPD"
    },
    {
        "id": "sky-sport-tennis",
        "title": "Sky Sport Tennis",
        "url": "https://linear310-it-dash1-prd.selector.skycdn.it/016a/32559/FHD/skysporttennis/master.mpd&key_id=0036fb7c564c4eb99e310f5fa82ab2f2&key=647f07b6858a669456e73ca103b4c2c0",
        "group": "MPD"
    },
    {
        "id": "sky-sport-nba",
        "title": "Sky Sport NBA",
        "url": "https://linear308-it-dash1-prd-akp2.cdn13.skycdp.com/016a/31764/FHD/skysportnba/master.mpd&key_id=00364eac2ffee337640e39682439b540&key=0960172d9000c470ade0658bd36c1d53",
        "group": "MPD"
    },
    {
        "id": "sky-sport-max",
        "title": "Sky Sport Max",
        "url": "https://linear305-it-dash1-prd-akp2.cdn13.skycdp.com/016a/31248/FHD/skysportmax/master.mpd&key_id=0036f13bca1c5603b9f3bb28ec28fa80&key=f01403bcb5a02c61153d297fb0c4395f",
        "group": "MPD"
    },
    {
        "id": "sky-sport-golf",
        "title": "Sky Sport Golf",
        "url": "https://linear309-it-dash1-prd-akp2.cdn13.skycdp.com/016a/32768/FHD/skysportgolf/master.mpd&key_id=00360b7729f74bf56a0a4eb0eda15ec5&key=f8a5f4723c71ac84c2f1ff6f55939a63",
        "group": "MPD"
    },
    {
        "id": "eurosport-1",
        "title": "Eurosport 1",
        "url": "https://linear311-it-dash1-prd.selector.skycdn.it/016a/313073/FHD/eurosport/master.mpd&key_id=0036bb3fa7e6f2c334d7cba5c28b6caf&key=217fa35739cd68e90b2cd23322c01312",
        "group": "MPD"
    },
    {
        "id": "eurosport-2",
        "title": "Eurosport 2",
        "url": "https://linear312-it-dash1-prd-akp2.cdn13.skycdp.com/016a/31150/FHD/eurosport2/master.mpd&key_id=003670a7034342a4a07c91173818c61c&key=7b90055c1a1ea34d9090e9ebf6c4db8a",
        "group": "MPD"
    },
    {
        "id": "sky-sport-251",
        "title": "Sky Sport Calcio 1",
        "url": "https://linear311-it-dash1-prd.selector.skycdn.it/016a/31917/FHD/skysport251/master.mpd&key_id=0036384f59a2b80ed142f82250c79f77&key=2e6507cb779a28739b0bb1564f418823",
        "group": "MPD"
    },
    {
        "id": "sky-sport-252",
        "title": "Sky Sport Calcio 2",
        "url": "https://linear312-it-dash1-prd.selector.skycdn.it/016a/32951/FHD/skysport252/master.mpd&key_id=003610b4ce44ba838c199b6636cf7431&key=8369cbbccf0c1ff6bdbacbdae9252a04",
        "group": "MPD"
    },
    {
        "id": "sky-sport-253",
        "title": "Sky Sport Calcio 3",
        "url": "https://linear311-it-dash1-prd.selector.skycdn.it/016a/32233/FHD/skysport253/master.mpd&key_id=0036d3b63b421abd69d9f0d3b6bdcf19&key=0725c3162d5aefbf9c6d144f06ea0c92",
        "group": "MPD"
    },
    {
        "id": "sky-sport-254",
        "title": "Sky Sport Calcio 4",
        "url": "https://linear312-it-dash1-prd.selector.skycdn.it/016a/31234/FHD/skysport254/master.mpd&key_id=00369c14c20b78aadb1ec0e3c0e74979&key=e768767e2c7238d8069887bb36aed7fa",
        "group": "MPD"
    },
    {
        "id": "sky-sport-255",
        "title": "Sky Sport Calcio 5",
        "url": "https://linear311-it-dash1-prd.selector.skycdn.it/016a/32910/FHD/skysport255/master.mpd&key_id=0036b781a22ebb0c20c16ac27d5d1448&key=f309b94acfda720bf1ed5741489f8967",
        "group": "MPD"
    },
    {
        "id": "sky-sport-256",
        "title": "Sky Sport Calcio 6",
        "url": "https://linear312-it-dash1-prd.selector.skycdn.it/016a/31912/FHD/skysport256/master.mpd&key_id=00366f263859fc1cc82d2c4da6a66ef6&key=754ae922d113c54349002cd9a88694a4",
        "group": "MPD"
    },
    {
        "id": "sky-sport-257",
        "title": "Sky Sport Calcio 7",
        "url": "https://linear311-it-dash1-prd-akp2.cdn13.skycdp.com/016a/31775/FHD/skysport257/master.mpd&key_id=0036faeace9872d3ceeb8b1b63f0baa3&key=dbd41ee944243307d39b7b27f16615a8",
        "group": "MPD"
    },
    {
        "id": "sky-sport-258",
        "title": "Sky Sport Calcio 8",
        "url": "https://linear312-it-dash1-prd-akp2.cdn13.skycdp.com/016a/32772/skysport258/master.mpd&key_id=0036fd8ccfddba47c8b40aeff63a797c&key=dfd5c9d0f4ac6f3a1bd89803399e7026",
        "group": "MPD"
    },
    {
        "id": "sky-sport-259",
        "title": "Sky Sport Calcio 9",
        "url": "https://linear311-it-dash1-prd-akp1.cdn13.skycdp.com/016a/31613/skysport259/master.mpd&key_id=0036644f7699f43e401f88d920dc385c&key=e5b0cebdc3edd7996d283041535fce9c",
        "group": "MPD"
    },
    {
        "id": "sky-cinema-uno",
        "title": "Sky Cinema Uno",
        "url": "https://linear314-it-dash1-prd.selector.skycdn.it/016a/32202/FHD/cinemauno/master.mpd&key_id=0036211ccb7bd9cfd99fb8591e67d772&key=a10923293396f30380ce411a3504ddc3",
        "group": "MPD"
    },
    {
        "id": "sky-cinema-due",
        "title": "Sky Cinema Due",
        "url": "https://linear308-it-dash1-prd-akp2.cdn13.skycdp.com/016a/32564/FHD/cinemadue/master.mpd&key_id=003629d4c6efbd39a2808a85a286b783&key=41c463cc4bf6da4dec7935eb01a7155e",
        "group": "MPD"
    },
    {
        "id": "sky-cinema-comedy",
        "title": "Sky Cinema Comedy",
        "url": "https://linear303-it-dash1-prd-akp2.cdn13.skycdp.com/016a/32030/FHD/cinemacomedy/master.mpd&key_id=003638a93ac06c9df7de5d8f349f56fd&key=45c7c2ba5a3cdfd03e90ff16e6ac15d8",
        "group": "MPD"
    },
    {
        "id": "sky-cinema-action",
        "title": "Sky Cinema Action",
        "url": "https://linear306-it-dash1-prd-akp2.cdn13.skycdp.com/016a/31206/FHD/cinemaaction/master.mpd&key_id=00368fc53eab9498463dadfc60e0f818&key=0a70fe8d3b90360035982deaa8c83a6d",
        "group": "MPD"
    },
    {
        "id": "sky-cinema-family",
        "title": "Sky Cinema Family",
        "url": "https://linear305-it-dash1-prd-akp2.cdn13.skycdp.com/016a/31255/FHD/cinemafamily/master.mpd&key_id=0036012604394c43b063c4f513ee431d&key=2c665092aa45cbae824bf7ad4e69d767",
        "group": "MPD"
    },
    {
        "id": "sky-cinema-collection",
        "title": "Sky Cinema Collection",
        "url": "https://linear302-it-dash1-prd.selector.skycdn.it/016a/31204/FHD/cinemacollection/master.mpd&key_id=003699aeb8e998fe0afed0c7302ce51f&key=4583daf5ec387c310633cdc922dd3130",
        "group": "MPD"
    },
    {
        "id": "sky-cinema-drama",
        "title": "Sky Cinema Drama",
        "url": "https://linear304-it-dash1-prd-akp2.cdn13.skycdp.com/016a/31769/FHD/cinemadrama/master.mpd&key_id=0036a5270d8f1d1a2f573864aed26225&key=df0e826d2eeb78051f5dcf6f166e6056",
        "group": "MPD"
    },
    {
        "id": "sky-cinema-suspense",
        "title": "Sky Cinema Suspense",
        "url": "https://linear307-it-dash1-prd-akp2.cdn13.skycdp.com/016a/32047/FHD/cinemasuspense/master.mpd&key_id=00365eb692a3fd6907192a4a3f0958b2&key=9f86ea0417e3458186f8ada1a2003fa5",
        "group": "MPD"
    },
    {
        "id": "sky-cinema-romance",
        "title": "Sky Cinema Romance",
        "url": "https://linear301-it-dash1-prd.selector.skycdn.it/016a/32231/FHD/cinemaromance/master.mpd&key_id=00362d0a5efbd10ab56a3f502f2be023&key=61c8c429f412ea52e06d9663c48ee9b7",
        "group": "MPD"
    },
    {
        "id": "sky-serie",
        "title": "Sky Serie",
        "url": "https://linear315-it-dash1-prd-akp2.cdn13.skycdp.com/016a/31684/FHD/skyserie/master.mpd&key_id=00366cd68acfb019e5d302f452c96ed7&key=fbb59d554722277be85b0728c13051ab",
        "group": "MPD"
    },
    {
        "id": "sky-crime",
        "title": "Sky Crime",
        "url": "https://linear315-it-dash1-prd.selector.skycdn.it/016a/32249/FHD/skycrime/master.mpd&key_id=0036de91177ccee5fdfd4929c099854f&key=f40263272212aacdcf7e405cfb4b4a91",
        "group": "MPD"
    },
    {
        "id": "sky-investigation",
        "title": "Sky Investigation",
        "url": "https://linear315-it-dash1-prd.selector.skycdn.it/016a/32686/FHD/skyinvestigation/master.mpd&key_id=003689703a245806508e9d332ed323ee&key=ef229589d2f7afa40904b6d62c852acf",
        "group": "MPD"
    },
    {
        "id": "sky-documentaries",
        "title": "Sky Documentaries",
        "url": "https://linear313-it-dash1-prd.selector.skycdn.it/016a/31697/FHD/skydocumentaries/master.mpd&key_id=0036de0a1c44a2c972fcf64c9b7f4302&key=0ade9234f6c56636ad6bb1b3560ddb31",
        "group": "MPD"
    },
    {
        "id": "sky-nature",
        "title": "Sky Nature",
        "url": "https://linear313-it-dash1-prd.selector.skycdn.it/016a/32695/FHD/skynature/master.mpd&key_id=0036dd4a767d1d1e6faa72be9b2edde3&key=60250673f0f5c54deac7c8f6d883c329",
        "group": "MPD"
    },
    {
        "id": "history",
        "title": "History Channel",
        "url": "https://linear313-it-dash1-prd.selector.skycdn.it/016a/31513/FHD/history/master.mpd&key_id=00362ec3497a383021f1db77c8556614&key=8820fb9b2afd6e1a3f4f5ab1ba4a73ad",
        "group": "MPD"
    },
    {
        "id": "sky-arte",
        "title": "Sky Arte",
        "url": "https://linear313-it-dash1-prd-akp2.cdn13.skycdp.com/016a/32074/FHD/skyarte/master.mpd&key_id=0036798d4dc4ce189b2f029a4b4aa06c&key=4f668ba0ef796d807c90613b9e2e61bf",
        "group": "MPD"
    },
    {
        "id": "mtv",
        "title": "MTV",
        "url": "https://linear315-it-dash1-prd-akg0.cdn13.skycdp.com/016a/32763/FHD/mtvnext/master.mpd&key_id=00364d417e7aab8e6a92c963f2d24549&key=a875a90e31b98eab8430e894ee5a853e",
        "group": "MPD"
    },
    {
        "id": "comedy-central",
        "title": "Comedy Central",
        "url": "https://linear309-it-dash1-prd-akp1.cdn13.skycdp.com/016a/32404/comedycentral/master.mpd&key_id=0036f3ec4ac7d836b5bf9fa79f3041b6&key=c02271563d97b1e7e755484279f2b55c",
        "group": "MPD"
    },
    {
        "id": "dazn-1",
        "title": "DAZN 1",
        "url": "https://dcf-fs-live-dazn-cdn.dazn.com/dash/dazn-linear-024/stream.mpd&key_id=8ab47741930c476780515f9a00decb0a&key=7ab4b9ae5a48aa526e511a913b832769",
        "group": "MPD"
    }
]



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

# --- Logica Canali Statici Interni ---
async def get_static_channel_streams(client, mfp_url=None, mfp_password=None):
    """
    Recupera i canali statici definiti localmente in STATIC_CHANNELS_DATA
    e applica la logica MFP se fornita.
    """
    streams = []
    for channel_data in STATIC_CHANNELS_DATA:
        original_channel_id = channel_data.get('id')
        original_channel_title = channel_data.get('title')
        original_channel_url = channel_data.get('url')
        original_channel_logo = channel_data.get('logo')
        group_name = channel_data.get('group', "Statici")

        # Salta i canali se mancano informazioni essenziali, specialmente l'URL
        # Modificato per non richiedere 'original_channel_logo'
        if not all([original_channel_id, original_channel_title, original_channel_url]):
            # print(f"DEBUG OMGTV (static): Canale statico saltato per dati mancanti (ID, Titolo o URL): {channel_data}")
            continue
        # print(f"DEBUG OMGTV (static): Processando canale statico: {original_channel_title}")

        final_url = original_channel_url # Default to original URL

        if mfp_url and mfp_password:
            # print(f"DEBUG OMGTV (static): MFP abilitato per {original_channel_title}. URL originale: {original_channel_url}")
            is_mpd_processed_for_mfp = False
            mpd_marker = ".mpd"
            try:
                # Cerca ".mpd" nell'URL originale
                mpd_index = original_channel_url.lower().index(mpd_marker)
                
                # Estrai l'URL base fino a ".mpd" incluso
                base_mpd_url = original_channel_url[:mpd_index + len(mpd_marker)]
                
                # Estrai la parte della query string che segue ".mpd"
                query_string_part = ""
                if len(original_channel_url) > mpd_index + len(mpd_marker):
                    potential_query_part = original_channel_url[mpd_index + len(mpd_marker):]
                    if potential_query_part.startswith("&"): # Assumiamo che i parametri inizino con &
                        query_string_part = potential_query_part[1:] # Rimuovi il primo &
                
                if query_string_part: # Se ci sono parametri come key_id e key
                    final_url = f"{mfp_url}/proxy/mpd/manifest.m3u8?api_password={mfp_password}&d={urllib.parse.quote(base_mpd_url)}&{query_string_part}"
                else: # MPD senza parametri di chiave esterni
                    final_url = f"{mfp_url}/proxy/mpd/manifest.m3u8?api_password={mfp_password}&d={urllib.parse.quote(base_mpd_url)}"
                is_mpd_processed_for_mfp = True
                # print(f"DEBUG OMGTV (static): {original_channel_title} è MPD. Applicando proxy MFP MPD. URL finale: {final_url}")

            except ValueError: # ".mpd" non trovato nell'URL
                pass # Verrà gestito come HLS sotto

            if not is_mpd_processed_for_mfp: # Se non è stato processato come MPD (es. è HLS)
                final_url = f"{mfp_url}/proxy/hls/manifest.m3u8?api_password={mfp_password}&d={urllib.parse.quote(original_channel_url)}"
                # print(f"DEBUG OMGTV (static): {original_channel_title} non è MPD (o marker non trovato). Applicando proxy MFP HLS. URL finale: {final_url}")

        streams.append({
            'id': f"omgtv-static-{original_channel_id}",
            'title': f"{original_channel_title} (MPD)",
            'url': final_url, # 'logo': original_channel_logo, # Rimosso perché non più garantito
            'group': group_name
        })
        # Aggiungi il logo solo se esiste
        if original_channel_logo:
            streams[-1]['logo'] = original_channel_logo
        # print(f"DEBUG OMGTV (static): Aggiunto stream: {streams[-1]}")
    return streams

async def get_omgtv_streams_for_channel_id(channel_id_full: str, client, mfp_url=None, mfp_password=None):
    """
    Funzione orchestratrice per recuperare uno stream specifico da OMGTV basato sull'ID completo.
    Esempio channel_id_full: "omgtv-247ita-sky-sport-uno"
    """
    parts = channel_id_full.split('-')
    # print(f"DEBUG OMGTV: get_omgtv_streams_for_channel_id chiamato con: {channel_id_full}")
    if len(parts) < 3 or parts[0] != "omgtv":
        return [] # ID non valido

    source = parts[1] # es. "247ita"
    channel_name_query = " ".join(parts[2:]) # es. "sky sport uno"

    # print(f"DEBUG OMGTV: Source: {source}, Channel Name Query: {channel_name_query}")
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
                # print(f"DEBUG OMGTV (247ita): Trovato stream corrispondente: {stream}")
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
        # print(f"DEBUG OMGTV (calcio): Trovati {len(collected_calcio_streams)} streams per '{channel_name_query}'")
        return collected_calcio_streams # Restituisce la lista di tutti gli stream calcio corrispondenti

    elif source == "vavoo":
        all_vavoo_streams = await get_vavoo_streams(client, mfp_url, mfp_password)
        for stream in all_vavoo_streams:
            if channel_name_query.replace("-", " ") in stream['id'].replace(f"omgtv-{source}-", "").replace("-", " "):
                # print(f"DEBUG OMGTV (vavoo): Trovato stream corrispondente: {stream}")
                return [stream]

    elif source == "static":
        # print(f"DEBUG OMGTV (static): Entrando nel blocco static.")
        all_static_streams = await get_static_channel_streams(client, mfp_url, mfp_password)
        # channel_name_query è come "sky atlantic". Convertilo in "sky-atlantic" per il match.
        channel_name_query = channel_name_query.replace(" ", "-")
        target_static_id = f"omgtv-static-{channel_name_query}"
        # print(f"DEBUG OMGTV (static): Cerco target_static_id: {target_static_id}")
        for stream in all_static_streams:
            # print(f"DEBUG OMGTV (static): Controllo stream con ID: {stream['id']}")
            if stream['id'] == target_static_id:
                # print(f"DEBUG OMGTV (static): Trovato stream statico corrispondente: {stream}")
                return [stream] # Restituisce una lista con lo stream trovato
    return []
# --- Logica Calcio (CT) ---
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

import random
from bs4 import BeautifulSoup,SoupStrainer
import Src.Utilities.config as config
from Src.Utilities.dictionaries import webru_vary,webru_dlhd,skystreaming
from Src.Utilities.loadenv import load_env
env_vars = load_env()
MEDIAFLOW_PASS = env_vars.get('MEDIAFLOW_PASS')
Referer = "https://ilovetoplay.xyz/"
Origin = "https://ilovetoplay.xyz"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Origin": Origin,
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Referer": Referer,
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
}
medialink = config.MediaProxy
async def get_stream_link(id,site,client):
    try:
        if site == "dlhd":
            m3u8_url = webru_dlhd[id]
        elif site == "vary":
            m3u8_url = webru_vary[id]
        response = await client.get(m3u8_url, headers=headers, allow_redirects=False, impersonate = "chrome120")
        if response.status_code == 301:
            stream_url = response.headers.get("Location", "")
            return stream_url,Referer,Origin
    except Exception as e:
        return None
async def webru(id,site,client):
    try:
        stream_url, Referer,Origin = await get_stream_link(id,site,client)
        mediaproxy = config.MediaProxy
        medialink = random.choice(mediaproxy)
        new_stream_url = f'{medialink}proxy/hls?key_url=https%3A%2F%2Fkey.mizhls.ru%2F&api_password={MEDIAFLOW_PASS}&d={stream_url}&h_Referer={Referer}&h_Origin={Origin}&h_User-Agent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F58.0.3029.110%20Safari%2F537.3'
        return new_stream_url
    except Exception as e:
        print("WebRu failed",e)
        return None
    


async def get_skystreaming(id,client):
    skystreaming_link =  skystreaming[id]
    response =  await client.get(skystreaming_link, headers=headers, allow_redirects=True, impersonate = "chrome120")
    soup = BeautifulSoup(response.text, 'lxml', parse_only=SoupStrainer('source'))
    source_tag = soup.find('source')
    m3u8_url = source_tag.get('src')
    Host = m3u8_url.replace("https://","").split("/")[0]
    print(Host)
    return m3u8_url,Host
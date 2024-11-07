import random
from bs4 import BeautifulSoup,SoupStrainer
import Src.Utilities.config as config
from Src.Utilities.dictionaries import webru_vary,webru_dlhd,skystreaming
from Src.Utilities.loadenv import load_env
env_vars = load_env()
MEDIAFLOW_PASS = env_vars.get('MEDIAFLOW_PASS')
Referer = "https://ilovetoplay.xyz/"
Origin = "https://ilovetoplay.xyz"
key_url = "https%3A%2F%2Fkey2.keylocking.ru%2F"  
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
async def get_stream_link(id,site):
    try:
        if site == "dlhd":
            stream_url = "https://xyzdddd.mizhls.ru/lb/" + webru_dlhd[id] + "/index.m3u8"
        elif site == "vary":
            stream_url = "https://webuit.mizhls.ru/lb/"+ webru_vary[id] + "/index.m3u8"
        mediaproxy = config.MediaProxy
        medialink = random.choice(mediaproxy)
        new_stream_url = f'{medialink}proxy/hls/manifest.m3u8?api_password={MEDIAFLOW_PASS}&d={stream_url}&h_Referer={Referer}&h_Origin={Origin}&h_User-Agent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F58.0.3029.110%20Safari%2F537.3'

        return stream_url,Referer,Origin
    except Exception as e:
        return None
async def webru(id,site,client):
    try:
        new_stream_url = await get_stream_link(id,site,client)
        
        return new_stream_url
    except Exception as e:
        print("WebRu failed",e)
        return None
    


async def get_skystreaming(id,client):
    try:
        skystreaming_link =  skystreaming[id]
        m3u8_urls = {}
        if type(skystreaming_link) == list:
            
            for link in skystreaming_link:
                m3u8_url,Host = await get_skystreaming_url(link,client)
                m3u8_urls[m3u8_url] = Host
                print(m3u8_urls)
        else:
            m3u8_url,Host = await get_skystreaming_url(skystreaming_link,client)
            m3u8_urls[m3u8_url] = Host
        return m3u8_urls

    except Exception as e:
        print("SkyStreaming failed",e)
        return None,None 
                    
    



async def get_skystreaming_url(skystreaming_link,client):
    try:
        if "hls" in skystreaming_link:
            m3u8_url = skystreaming_link
            Host = m3u8_url.replace("https://","").split("/")[0]
            return m3u8_url,Host
        response =  await client.get(skystreaming_link, headers=headers, allow_redirects=True, impersonate = "chrome120")
        soup = BeautifulSoup(response.text, 'lxml', parse_only=SoupStrainer('source'))
        source_tag = soup.find('source')
        m3u8_url = source_tag.get('src')
        Host = m3u8_url.replace("https://","").split("/")[0]
        print(Host)
        return m3u8_url,Host
    except Exception as e: 
        print("SkyStreaming failed",e)
        return None,None
    




    '''
    async def webru(id,site,client):
    try:
        stream_url, Referer,Origin = await get_stream_link(id,site,client)
        mediaproxy = config.MediaProxy
        medialink = random.choice(mediaproxy)
        new_stream_url = f'{medialink}proxy/hls/manifest.m3u8?api_password={MEDIAFLOW_PASS}&d={stream_url}&h_Referer={Referer}&h_Origin={Origin}&h_User-Agent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F58.0.3029.110%20Safari%2F537.3'
        return new_stream_url
    except Exception as e:
        print("WebRu failed",e)
        return None
    '''



async def webru(id,site,client):
    try:
        print(id)
        if site == "vary":
            print("1")
            url = await get_stream_link(id,site)
        if any(keyword in id for keyword in ["cinema", "arte", "nature", "investigation", "sky-uno", "sky-serie"]):
            print("2")
            url = await get_stream_link(id,site)
        else:
            print("3")
            response = await client.get(f"https://848b3516657c-worldwide-sports-tv.baby-beamup.club/stream/tv/wwstv-it-{id}.json", impersonate = "chrome120", headers = headers)
            data = response.json()
            url = data['streams'][0]['url']
            print(url)
            return url
    except Exception as e:
        print("WorldSport failed",e)
        return None
    

    '''
    if id in skystreaming:
                        i = i+1
                        url,Host = await get_skystreaming(id,client)
                        streams['streams'].append({'title': f'{HF}Server {i}', 'url': url, "behaviorHints": {"notWebReady": True, "proxyHeaders": {"request": {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Origin": "https://skystreaming.guru", "DNT": "1", "Sec-GPC": "1", "Connection": "keep-alive", "Referer": "https://skystreaming.guru/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site", "Pragma": "no-cache", "Cache-Control": "no-cache", "TE": "trailers","Host": Host}}}})

    '''
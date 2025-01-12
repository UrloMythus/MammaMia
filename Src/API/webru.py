import random
from bs4 import BeautifulSoup,SoupStrainer
import Src.Utilities.config as config
from Src.Utilities.dictionaries import webru_vary,webru_dlhd,skystreaming
from Src.Utilities.loadenv import load_env
from urllib.parse import urlparse
import re
TF_DOMAIN = config.TF_DOMAIN
DLHD_DOMAIN = config.DLHD_DOMAIN
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

async def get_stream_link(id,site,MFP_CREDENTIALS,client):
    try:
        if site == "dlhd":
            response = await client.get(f"https://thedaddy.{DLHD_DOMAIN}/embed/stream-853.php", impersonate = "chrome124", headers = headers)
            soup = BeautifulSoup(response.text, 'lxml', parse_only=SoupStrainer('iframe'))
            iframe = soup.find('iframe', id='thatframe')
            real_link = iframe.get('src')
            response = await client.get(real_link, allow_redirects = False) 
            pattern = r"source:\s*'([^']*\.m3u8)'"
            match = re.search(pattern, response.text)
            if match:
                m3u8_url = match.group(1)  # The URL is captured in the first capturing group
                parsed_url = urlparse(m3u8_url)
                domain = parsed_url.netloc

            else:
                print("No .m3u8 URL found.")
            stream_url = f"https://{domain}/lb/" + webru_dlhd[id] + "/index.m3u8"
        elif site == "vary":
            response = await client.get(f"https://www.tanti.{TF_DOMAIN}/tv-channel/sky-cinema-action-2", impersonate = "chrome124", headers = headers, timeout = 10)
            soup = BeautifulSoup(response.text, 'lxml', parse_only=SoupStrainer('iframe'))
            iframe = soup.find('iframe', class_='embed-responsive-item') 
            real_link = iframe.get('src')
            response = await client.get(real_link, allow_redirects = False) 
            pattern = r"source:\s*'([^']*\.m3u8)'"
            match = re.search(pattern, response.text)
            if match:
                m3u8_url = match.group(1)  # The URL is captured in the first capturing group
                parsed_url = urlparse(m3u8_url)
                domain = parsed_url.netloc

            else:
                print("No .m3u8 URL found.")
            stream_url = f"https://{domain}/lb/"+ webru_vary[id] + "/index.m3u8"
        mfp_url = MFP_CREDENTIALS[0]
        mfp_pass = MFP_CREDENTIALS[1]
        new_stream_url = f'{mfp_url}/proxy/hls/manifest.m3u8?api_password={mfp_pass}&d={stream_url}&h_Referer={Referer}&h_Origin={Origin}&h_User-Agent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F58.0.3029.110%20Safari%2F537.3'

        return new_stream_url
    except Exception as e:
        return None
async def webru(id,site,client,MFP_CREDENTIALS):
    try:
        new_stream_url = await get_stream_link(id,site,MFP_CREDENTIALS,client)
        
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
async def webru(id,site,client,MFP_CREDENTIALS):
    try:
        stream_url, Referer,Origin = await get_stream_link(id,site,client)
        mfp_url = MFP_CREDENTIALS[0]
        mfp_pass = MFP_CREDENTIALS[1]
        new_stream_url = f'{mfp_url}/proxy/hls/manifest.m3u8?api_password={mfp_pass}&d={stream_url}&h_Referer={Referer}&h_Origin={Origin}&h_User-Agent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F58.0.3029.110%20Safari%2F537.3'
        return new_stream_url
    except Exception as e:
        print("WebRu failed",e)
        return None
'''
'''
async def webru2(id,site,client):
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
'''
    if id in skystreaming:
                        i = i+1
                        url,Host = await get_skystreaming(id,client)
                        streams['streams'].append({'title': f'{HF}Server {i}', 'url': url, "behaviorHints": {"notWebReady": True, "proxyHeaders": {"request": {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Origin": "https://skystreaming.guru", "DNT": "1", "Sec-GPC": "1", "Connection": "keep-alive", "Referer": "https://skystreaming.guru/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site", "Pragma": "no-cache", "Cache-Control": "no-cache", "TE": "trailers","Host": Host}}}})

    '''
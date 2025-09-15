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

async def get_stream_link(id,site,client):
    try:
        if site == "dlhd":
            dlhd_id = webru_dlhd[id]
            response = await client.get(f"{DLHD_DOMAIN}/embed/stream-853.php", impersonate = "chrome124", headers = headers)
            soup = BeautifulSoup(response.text, 'lxml', parse_only=SoupStrainer('iframe'))
            iframe = soup.find('iframe', id='thatframe')
            real_link = iframe.get('src')
            parent_site_domain = real_link.split('/premiumtv')[0]
            server_key_link = (f'{parent_site_domain}/server_lookup.php?channel_id={dlhd_id}')
            response = await client.get(server_key_link, allow_redirects = False)
            server_key = response.json()['server_key']
            '''
            response = await client.get(real_link, allow_redirects = False) 
            print(response.text)
            pattern = r"source:\s*'([^']*\.m3u8)'"
            match = re.search(pattern, response.text)
            if match:
                m3u8_url = match.group(1)  # The URL is captured in the first capturing group
                parsed_url = urlparse(m3u8_url)
                domain = parsed_url.netloc

            else:
                print("No .m3u8 URL found.")
            '''
            stream_url = f"https://{server_key}new.iosplayer.ru/{server_key}/{dlhd_id}" + "/mono.m3u8"
            return stream_url,Referer,Origin
        elif site == "vary":
            response = await client.get("https://calcio.monster/streaming-gratis-calcio-1.php", impersonate = "chrome124", headers = headers)
            soup = BeautifulSoup(response.text, 'lxml', parse_only=SoupStrainer('div', class_='ticket_btn'))
            href = soup.find('a').get('href')
            response = await client.get(href)
            soup = BeautifulSoup(response.text, 'lxml', parse_only=SoupStrainer('button'))
            webru_iframe = soup.find_all('button', {"data-type": "embed"})
            for i in webru_iframe:
                webru_iframe = i.get('data-url')
                if "php" not in webru_iframe:
                    continue
                else:
                    break
            webru_iframe = "https://" + webru_iframe.split("/")[2]
            vary_id = webru_vary[id]
            vary_link = f"{webru_iframe}/server_lookup.php?channel_id={vary_id}"
            response = await client.get(vary_link, headers=headers, allow_redirects=True, impersonate = "chrome124")
            server_key = response.json()['server_key']
            stream_url = f"https://{server_key}new.iosplayer.ru/{server_key}/{vary_id}" + "/mono.m3u8"
            return stream_url,Referer,Origin
    except Exception as e:
        print("WebRu failed",e)
        return None,None,None
async def webru(id,site,client):
    try:
        new_stream_url,Referer,Origin = await get_stream_link(id,site,client)
        if new_stream_url == None:
            raise Exception("No stream URL found")
        return new_stream_url,Referer,Origin
    except Exception as e:
        print("WebRu failed",e)
        return None,None,None
    


async def get_skystreaming(id,client):
    try:
        skystreaming_link =  skystreaming[id]
        if type(skystreaming_link) == list:
            
            for link in skystreaming_link:
                m3u8_url,Host,Origin = await get_skystreaming_url(link,client)
        else:
            m3u8_url,Host,Origin = await get_skystreaming_url(skystreaming_link,client)
        return m3u8_url,Host,Origin
    except Exception as e:
        print("SkyStreaming failed",e)
        return None,None,None 
                    
    



async def get_skystreaming_url(skystreaming_link,client):
    try:
        if "hls" in skystreaming_link:
            m3u8_url = skystreaming_link
            Host = m3u8_url.replace("https://","").split("/")[0]
            response =  await client.get(skystreaming_link, headers=headers, allow_redirects=True, impersonate = "chrome120")
            Origin = response.url.split('/embed')[0]
            return m3u8_url,Host,Origin 
        response =  await client.get(skystreaming_link, headers=headers, allow_redirects=True, impersonate = "chrome120")
        Origin = response.url.split('/embed')[0]
        soup = BeautifulSoup(response.text, 'lxml', parse_only=SoupStrainer('source'))
        source_tag = soup.find('source')
        m3u8_url = source_tag.get('src')
        Host = m3u8_url.replace("https://","").split("/")[0]
        return m3u8_url,Host,Origin
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
async def test_webru():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        # Replace with actual id, for example 'anime_id:episode' format
        test_id = "sky-sport-uno"  # This is an example ID format
        results = await get_skystreaming(test_id,client)
        print(results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_webru())
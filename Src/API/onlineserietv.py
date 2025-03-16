from Src.Utilities.info import get_info_imdb, is_movie, get_info_tmdb
from bs4 import BeautifulSoup,SoupStrainer
import Src.Utilities.config as config
from fake_headers import Headers  
from Src.Utilities.loadenv import load_env  
import json, random
import re
from Src.Utilities.eval import eval_solver
OST_DOMAIN = config.OST_DOMAIN
OST_PROXY = config.OST_PROXY
env_vars = load_env()
proxies = {}
if OST_PROXY == "1":
    PROXY_CREDENTIALS = env_vars.get('PROXY_CREDENTIALS')
    proxy_list = json.loads(PROXY_CREDENTIALS)
    proxy = random.choice(proxy_list)
    if proxy == "":
        proxies = {}
    else:
        proxies = {
            "http": proxy,
            "https": proxy
        }   
OST_ForwardProxy = config.OST_ForwardProxy
if OST_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
else:
    ForwardProxy = ""
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.71 Mobile Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'X-Requested-With': 'XMLHttpRequest',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Referer': f'https://onlineserietv.{OST_DOMAIN}/',
    # 'Cookie': 'player_opt=fx',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

async def search(showname,date,client,ismovie,episode,season):
    cookies = {
    'player_opt': 'fx',
    }
    params = {
    's': showname,
    'action': 'searchwp_live_search',
    'swpengine': 'default',
    'swpquery': showname,
    'origin_id': '50141',
    'searchwp_live_search_client_nonce': 'undefined',
    }
    response = await client.get(ForwardProxy + f"https://onlineserietv.{OST_DOMAIN}/wp-admin/admin-ajax.php?s={showname.replace(' ','%20')}&action=searchwp_live_search&swpengine=default&swpquery={showname.replace(' ', '%20')}&origin_id=50141&searchwp_live_search_client_nonce=undefined", headers=headers, cookies=cookies, impersonate = "chrome124", proxies = proxies)
    if response.status_code != 200:
        print("IP Blocked by OnlineserieTV",response)
    soup = BeautifulSoup(response.text, 'lxml', parse_only=SoupStrainer('a'))
    a_tags_with_href = soup.find_all("a", href=True)
    for a_tag in a_tags_with_href:
        href = a_tag.get("href")
        if ismovie == 1:
            if "film" in href:
                response = await client.get(ForwardProxy + href, headers=headers, impersonate = "chrome124", proxies = proxies)
                if response.status_code != 200:
                    print("IP Blocked by OnlineserieTV",response)
                year_match = re.search(r'Anno: <i>(\d{4})</i>', response.text)
                year = year_match.group(1) if year_match else None
                if year == date:
                    pattern = r'https://uprot\.net/fxf/[^\s"<>]+'
                    match = re.search(pattern, response.text)
                    if match:
                        name = a_tag.text.replace("\t","").replace("\n","")
                        flexy_link = match.group()
                        return flexy_link,name
                    else:
                        print("No flexy link found.")
            else:
                continue
        elif ismovie == 0:
            if "serietv" in href:
                response = await client.get(ForwardProxy + href, headers=headers, impersonate = "chrome124", proxies = proxies)
                if response.status_code != 200:
                    print("IP Blocked by OnlineserieTV",response)
                year_match = re.search(r'Anno: <i>(\d{4})</i>', response.text)
                year = year_match.group(1) if year_match else None
                if year == date:
                    season = season.zfill(2)
                    episode = episode.zfill(2)
                    pattern = rf'{season}x{episode}.*?<a href=[\'"](https://uprot\.net/fxf/[^\'"]+)'
                    match = re.search(pattern, response.text, re.DOTALL)
                    if match:
                        name = a_tag.text.replace("\t","").replace("\n","")
                        flexy_link = match.group(1)
                        return flexy_link,name
                    else:
                        print("No flexy link found.")
            else:
                continue 



async def onlineserietv(id,client):
    try:
        general = await is_movie(id)
        ismovie = general[0]
        clean_id = general[1]
        if ismovie == 0:
            season = general[2]
            episode = general[3]
        elif ismovie == 1:
            season = None
            episode = None
        type = "Onlineserietv"
        if "tt" in id:
                showname,date = await get_info_imdb(clean_id,ismovie,type,client)
        else:
            showname,date = get_info_tmdb(clean_id,ismovie,type)
        flexy_link,name = await search(showname,date,client,ismovie,episode,season)
        flexy_link = flexy_link.replace("fxf","fxe")
        real_url = await client.head(ForwardProxy + flexy_link, headers=headers, impersonate = "chrome124", proxies = proxies)
        real_url = real_url.url
        final_url = await eval_solver(real_url,proxies, ForwardProxy, client)
        return final_url,name
    except Exception as e:
        print("MammaMia: Onlineserietv Failed",e)
        return None,None
    

async def test_animeworld():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        test_id = "tt9218128"  # This is an example ID format
        results = await onlineserietv(test_id, client)
        print(results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_animeworld())


    #python3 -m Src.API.onlineserietv

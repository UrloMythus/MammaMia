from Src.Utilities.info import  is_movie
from bs4 import BeautifulSoup,SoupStrainer
import re
import Src.Utilities.config as config
from fake_headers import Headers  
from Src.Utilities.loadenv import load_env  
import json, random
from Src.Utilities.info import get_info_imdb,get_info_tmdb
import urllib.parse
from Src.Utilities.convert import get_IMDB_id_from_TMDb_id
from Src.API.extractors.supervideo import supervideo
import logging
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)

env_vars = load_env()
GS_PROXY = config.GS_PROXY
proxies = {}
if GS_PROXY == "1":
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
GS_ForwardProxy = config.GS_ForwardProxy
if GS_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
else:
    ForwardProxy = ""
#Get domain
GS_DOMAIN = config.GS_DOMAIN
random_headers = Headers()

async def search_imdb(clean_id,client):
    try:
        headers = random_headers.generate()
        response = await client.get(ForwardProxy + f'{GS_DOMAIN}/?story={clean_id}&do=search&subaction=search', allow_redirects=True, headers = headers, proxies = proxies)
        if response.status_code != 200:
            logger.warning(f"Guardaserie Failed to fetch search results: {response.status_code}")
        soup = BeautifulSoup(response.text,'lxml',parse_only=SoupStrainer('div',class_="mlnh-2"))
        div_mlnh2 = soup.select_one('div.mlnh-2:nth-of-type(2)')
        a_tag = div_mlnh2.find('h2').find('a')
        href = a_tag['href']
        return href
    except Exception as e:
        logger.warning(f'GS {e}')
        return None

async def search(showname,date,client):
    try:
        headers = random_headers.generate()
        showname = urllib.parse.quote(showname)
        response = await client.get(ForwardProxy + f'{GS_DOMAIN}/?story={showname}&do=search&subaction=search', allow_redirects=True, impersonate = "chrome124", headers = headers, proxies = proxies)        
        if response.status_code != 200:
            logger.warning(f"Guardaserie Failed to fetch search results: {response.status_code}")
        soup = BeautifulSoup(response.text,'lxml',parse_only=SoupStrainer('div'))
        div_mlnew = soup.find_all('div', class_='mlnew')
        for mlnew in div_mlnew:
            div_date = mlnew.find('div', class_='mlnh-3 hdn').text
            div_date = div_date[:4]
            if div_date == date:
                a_tag = mlnew.find('div', class_='mlnh-2').find('h2').find('a')
                href = a_tag['href']
                return href

    except Exception as e:
        return None



async def player_url(page_url, season, episode,client):
    try:
        headers = random_headers.generate()
        response = await client.get(ForwardProxy + page_url, allow_redirects=True, headers = headers, proxies = proxies)
        soup = BeautifulSoup(response.text,'lxml',parse_only=SoupStrainer('a'))
        a_tag = soup.find('a', id = f"serie-{season}_{episode}")
        href = a_tag['data-link']
        return href
    except Exception as e:
        return None





async def guardaserie(streams,id,client):
    try:
        general = await is_movie(id)
        ismovie = general[0]
        clean_id = general[1]
        if ismovie == 1:
            return streams
        if ismovie == 0:
            season = general[2]
            episode = general[3]
        type = "Guardaserie"
        page_url = await search_imdb(clean_id,client)
        supervideo_link =await player_url(page_url,season,episode,client)
        if supervideo_link: 
            streams = await supervideo(supervideo_link, client, streams,"Guardaserie",proxies, ForwardProxy)
            return streams
        else:
            logger.warning(" GS Couldn't find iframe source")
            return streams
    except Exception as e:
        logger.warning(f"MammaMia: Guardaserie Failed{e}")
        return streams


async def test_script():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        # Replace with actual id, for example 'anime_id:episode' format
        test_id = "tt10919420:1:1"  # This is an example ID format tt0460649
        results = await guardaserie({'streams': []},test_id, client)
        print(results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_script())








'''
        if "tt" not in clean_id:
            clean_id = await get_IMDB_id_from_TMDb_id(clean_id,client) 
            print(clean_id)
'''
'''
        if "tt" in id:
            showname,date = await get_info_imdb(clean_id,ismovie,type,client)
        else:
            showname,date = get_info_tmdb(clean_id,ismovie,type)
        showname = showname.replace("'"," ")
        if "Guru" in showname:
            showname = showname.split("-")[0]
'''
'''
        page_url = await search(showname,date,client)
'''
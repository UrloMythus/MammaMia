from Src.Utilities.info import get_info_tmdb, is_movie, get_info_imdb
import Src.Utilities.config as config
from fake_headers import Headers  
from Src.Utilities.loadenv import load_env  
from urllib.parse import quote
from bs4 import BeautifulSoup, SoupStrainer
import re
from Src.API.extractors.uqload import uqload
from Src.API.extractors.loadm import loadm
from Src.API.extractors.dropload import dropload
import logging
from Src.Utilities.config import setup_logging
level = config.LEVEL
import json
import random
logger = setup_logging(level)
env_vars = load_env()
random_headers = Headers()
GO_DOMAIN = config.GO_DOMAIN

GO_PROXY = config.GO_PROXY
proxies = {}
if GO_PROXY == "1":
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
GO_ForwardProxy = config.GO_ForwardProxy
if GO_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
else:
    ForwardProxy = ""



async def get_player(page_link,MFP,MFP_CREDENTIALS,client, headers, streams):
    response = await client.get(ForwardProxy + page_link, headers= headers, proxies = proxies)
    soup = BeautifulSoup(response.text,'lxml', parse_only=SoupStrainer('iframe'))
    iframe = soup.find('iframe')
    player_link = iframe.get('data-src') or iframe.get('src')
    urls = []
    if "loadm" in player_link:
        referer = page_link.split('//')[1].split('/')[0]
        streams = await loadm(player_link,client,streams,referer,"Guardoserie", proxies,ForwardProxy) 
    elif "uqload" in player_link:
        streams = await uqload(player_link,client,MFP,MFP_CREDENTIALS,streams,"Guardoserie",proxies,ForwardProxy)
    elif "dropload" in player_link:
        streams = await dropload(player_link,client,streams,"Guardoserie",proxies,ForwardProxy)
    return streams


async def search(showname,date,season,episode,MFP, MFP_CREDENTIALS,ismovie,client,streams,):
    headers = random_headers.generate()
    headers['Origin'] = f'{GO_DOMAIN}'
    headers['Referer'] = f'{GO_DOMAIN}/'
    headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
    showname = quote(showname)
    data = f's={showname}&action=searchwp_live_search&swpengine=default&swpquery={showname}'
    response = await client.post(ForwardProxy + f'{GO_DOMAIN}/wp-admin/admin-ajax.php', data = data, headers = headers, proxies = proxies)
    if response.status_code != 200:
            logger.warning(f"Guardoserie Failed to fetch search results: {response.status_code}")
    soup = BeautifulSoup(response.text,'lxml', parse_only=  SoupStrainer('a', class_='ss-title'))
    a_tags = soup.find_all('a')
    for a in a_tags:
        href = a['href']
        response = await client.get(ForwardProxy + href, headers = headers, proxies = proxies)
        pattern = r'(?<=/release-year\/)(\d{4})(?=\/" rel="tag">)'
        match = re.search(pattern, response.text)
        if match:
            year = match.group(0)
            if year == date:
                if ismovie == 0:
                    soup = BeautifulSoup(response.text, 'lxml', parse_only= SoupStrainer('div', class_='les-content'))  
                    divs = soup.find_all('div', class_='les-content')
                    actual_div = divs[int(season)-1]
                    episodes_a = actual_div.find_all('a')
                    actual_episode = episodes_a[int(episode)-1]
                    page_link = actual_episode['href']
                    logger.info(page_link)
                elif ismovie == 1:
                    page_link = href
                streams = await get_player(page_link,MFP,MFP_CREDENTIALS,client, headers,streams)
                return streams
    return streams

















async def guardoserie(streams,id,client,MFP,MFP_CREDENTIALS):
    try:
        general = await is_movie(id)
        ismovie = general[0]
        clean_id = general[1]
        type = "Guardoserie"
        if ismovie == 0 : 
            season = str(general[2])
            episode = str(general[3])
        elif ismovie == 1:
            season = None
            episode = None
        if "tmdb" in id:
            showname,date = get_info_tmdb(clean_id,ismovie,type)
        else:
            showname,date = await get_info_imdb(clean_id,ismovie,type,client)
        logger.info(f'GO {showname}')
        streams = await search(showname,date, season,episode,MFP,MFP_CREDENTIALS,ismovie,client,streams)
        return streams
    except Exception as e:
        logger.warning(f'GO {e}')
        return streams




async def test_guardoserie():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        results = await guardoserie({'streams': []},"tt10919420:1:1",client,"1",['test','test'])
        print(results)

        
if __name__ == "__main__":
    import asyncio
    asyncio.run(test_guardoserie()) 
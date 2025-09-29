from Src.Utilities.info import get_info_tmdb, is_movie, get_info_imdb
import Src.Utilities.config as config
from fake_headers import Headers
from Src.Utilities.loadenv import load_env  
from urllib.parse import quote
from bs4 import BeautifulSoup, SoupStrainer
from Src.API.extractors.loadm import loadm
from Src.API.extractors.uqload import uqload
from Src.API.extractors.dropload import dropload
import logging
from Src.Utilities.config import setup_logging
import json
import random
level = config.LEVEL
logger = setup_logging(level)
env_vars = load_env()
random_headers = Headers()
GF_DOMAIN = config.GF_DOMAIN

GF_PROXY = config.GF_PROXY
proxies = {}
if GF_PROXY == "1":
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
GF_ForwardProxy = config.GF_ForwardProxy
if GF_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
else:
    ForwardProxy = ""



async def get_player(page_link,MFP, MFP_CREDENTIALS,client, headers,streams):
    response = await client.get(ForwardProxy + page_link, headers= headers, proxies = proxies)
    soup = BeautifulSoup(response.text,'lxml', parse_only=SoupStrainer('iframe'))
    iframe = soup.find('iframe')
    player_link = iframe.get('data-src') or iframe.get('src')
    if "loadm" in player_link:
        referer = page_link.split('//')[1].split('/')[0]
        streams = await loadm(player_link,client,streams,referer,"Guardaflix", proxies, ForwardProxy) 
    elif "uqload" in player_link:
        streams = await uqload(player_link,client,MFP,MFP_CREDENTIALS,streams,"Guardaflix", proxies, ForwardProxy)
    elif "dropload" in player_link:
        streams = await dropload(player_link,client,streams,"Guardaflix", proxies, ForwardProxy)
    return streams

async def search(showname,date,MFP,MFP_CREDENTIALS,client,streams):
    headers = random_headers.generate()
    headers['Origin'] = f'{GF_DOMAIN}'
    headers['Referer'] = f'{GF_DOMAIN}/'
    headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
    data = {
    'action': 'action_tr_search_suggest',
    'nonce': '20115729b4',
    'term': showname,
    }
    response = await client.post(ForwardProxy + f'{GF_DOMAIN}/wp-admin/admin-ajax.php', headers=headers, data=data, proxies = proxies)
    if response.status_code != 200:
            logger.warning(f"Guardaflix Failed to fetch search results: {response.status_code}")
    soup = BeautifulSoup(response.text,'lxml', parse_only=  SoupStrainer('a'))
    a_tags = soup.find_all('a')
    for a in a_tags:
        href = a['href']
        logger.info(href) 
        response = await client.get(ForwardProxy + href, headers = headers, proxies = proxies)
        soup = BeautifulSoup(response.text,'lxml', parse_only = SoupStrainer(['iframe', 'span']))
        year = soup.find('span',class_='year fa-calendar far').text
        if year == date:
            iframe = soup.find('iframe')
            page_link = iframe.get('data-src') or iframe.get('src')
            streams = await get_player(page_link,MFP,MFP_CREDENTIALS,client, headers,streams)
            return streams
    return streams
        







async def guardaflix(streams,id,client,MFP,MFP_CREDENTIALS):
    try:
        general = await is_movie(id)
        ismovie = general[0]
        clean_id = general[1]
        type = "Guardaflix"
        if ismovie == 0: 
            return streams
        if "tmdb" in id:
            showname,date = get_info_tmdb(clean_id,ismovie,type)
        else:
            showname,date = await get_info_imdb(clean_id,ismovie,type,client)
        logger.info(showname)
        streams = await search(showname,date,MFP,MFP_CREDENTIALS,client,streams)
        return streams
    except Exception as e:
        logger.warning(f'GF {e}')
        return streams




async def test_guardaflix():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        results = await guardaflix({'streams': []},"tt4045450",client,"0",['test','test'])
        print(results)

        
if __name__ == "__main__":
    import asyncio
    asyncio.run(test_guardaflix()) 
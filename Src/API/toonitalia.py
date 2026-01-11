from fake_headers import Headers

random_headers = Headers()

import  Src.Utilities.config as config

from Src.Utilities.info import get_info_imdb,get_info_tmdb
from urllib.parse import quote
from Src.Utilities.convert import get_IMDB_id_from_TMDb_id
from Src.Utilities.info import get_info_tmdb, is_movie, get_info_imdb
from Src.API.extractors.voe import voe
from Src.API.extractors.maxstream import maxstream
import logging
from Src.Utilities.config import setup_logging
level = config.LEVEL
import re
import json

import random
logger = setup_logging(level)
from Src.Utilities.loadenv import load_env  
env_vars = load_env()
TI_DOMAIN = config.TI_DOMAIN

TI_PROXY = config.TI_PROXY
proxies = {}
if TI_PROXY == "1":
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
TI_ForwardProxy = config.TI_ForwardProxy
if TI_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
else:
    ForwardProxy = ""





async def search(showname,date,season,episode,MFP,MFP_CREDENTIALS,ismovie,client,streams):
    headers = random_headers.generate()
    response = await client.get(ForwardProxy + f'{TI_DOMAIN}/wp-json/wp/v2/search?search={quote(showname)}',headers=headers, proxies = proxies)
    data = response.json()
    for item in data:
        response = await client.get(ForwardProxy + item['_links']['self'][0]['href'],headers=headers, proxies = proxies)
        info = response.json()
        html = info['content']['rendered']
        if 'Stagione' in html and ismovie == 1:
            continue
        if 'Stagione' not in html and ismovie == 0:
            continue
        if ismovie == 0:
            episode = episode.zfill(2)
            pattern = rf'{season}&#215;{episode}.*?<a[^>]*href="([^"]*)'
        if ismovie == 1:
            pattern = r'Link.*href="([^"]*)(?=.*VOE)'
        match = re.search(pattern,html)
        if match:
            url = match.group(1)
        if 'maxstream' in url:
            parts = url.split('.video/')
            url = 'https://maxstream.video/emvvv/' + parts[1]
            streams = await maxstream(url,client,streams,'ToonItalia','',proxies,ForwardProxy)
        else:
            streams = await voe(url,streams,'ToonItalia',MFP,MFP_CREDENTIALS,proxies,ForwardProxy,client)
        return streams
    return streams














async def toonitalia(streams,id,client,MFP,MFP_CREDENTIALS):
    try:
        general = await is_movie(id)
        ismovie = general[0]
        clean_id = general[1]
        type = "Toonitalia"
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
        streams = await search(showname,date, season,episode,MFP,MFP_CREDENTIALS,ismovie,client,streams)
        return streams
    except Exception as e:
        logger.warning(f'Toonitalia Error: {e}')
        return streams



async def test_toonitalia():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        results = await toonitalia({'streams': []},"tt1466074:1:1",client,"0",['test','test'])
        print(results)

        
if __name__ == "__main__":
    import asyncio
    asyncio.run(test_toonitalia()) 
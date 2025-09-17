from Src.Utilities.info import  is_movie
from bs4 import BeautifulSoup,SoupStrainer
import re
import Src.Utilities.config as config
from fake_headers import Headers  
from Src.Utilities.loadenv import load_env  
from Src.API.extractors.supervideo import supervideo
import json, random
import logging
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)
env_vars = load_env()
GH_PROXY = config.GH_PROXY
proxies = {}
if GH_PROXY == "1":
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
GH_ForwardProxy = config.GH_ForwardProxy
if GH_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
else:
    ForwardProxy = ""
GHD_DOMAIN = config.GHD_DOMAIN

random_headers = Headers()


async def search(clean_id,client):
    headers = random_headers.generate()
    response = await client.get(ForwardProxy + f"{GHD_DOMAIN}/set-movie-a/{clean_id}", allow_redirects=True, headers = headers, proxies = proxies)
    if response.status_code != 200:
            logger.warning(f"GuardaHD Failed to fetch search results: {response.status_code}")
    soup = BeautifulSoup(response.text,'lxml',parse_only=SoupStrainer('li'))
    li_tag = soup.find('li')
    href = "https:" + li_tag['data-link']
    return href



async def guardahd(streams,id,client):
    try:
        general = await is_movie(id)
        ismovie = general[0]
        clean_id = general[1]
        if ismovie == 0:
            return streams
        supervideo_link = await search(clean_id,client)
        streams = await supervideo(supervideo_link, client,streams,"GuardaHD",proxies, ForwardProxy)
        return streams
    except Exception as e:
        logger.warning(f"MammaMia: GuardaHD Failed {e}")
        return streams
    
async def test_script():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        # Replace with actual id, for example 'anime_id:episode' format
        test_id = "tt16426418"  # This is an example ID format
        results = await guardahd({'streams': []},test_id, client)
        print(results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_script())
    
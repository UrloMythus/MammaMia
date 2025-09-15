from bs4 import BeautifulSoup,SoupStrainer
from Src.Utilities.convert import get_TMDb_id_from_IMDb_id
from Src.Utilities.info import is_movie
import Src.Utilities.config as config
import json
import random
import re
from Src.Utilities.loadenv import load_env  
from Src.API.extractors.vixcloud import vixcloud
import logging
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)
User_Agent= "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0"

env_vars = load_env()
SC_PROXY = config.SC_PROXY
VX_PROXY = config.VX_PROXY
proxies = {}
proxies2 = {}
if VX_PROXY == "1":
    PROXY_CREDENTIALS = env_vars.get('PROXY_CREDENTIALS')
    proxy_list = json.loads(PROXY_CREDENTIALS)
    proxy = random.choice(proxy_list)
    if proxy == "":
        proxies2 = {}
    else:
        proxies2 = {
            "http": proxy,
            "https": proxy
        }      
if SC_PROXY == "1":
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
    if VX_PROXY == "1":
        proxies2 = proxies
 
SC_ForwardProxy = config.SC_ForwardProxy
VX_ForwardProxy = config.VX_ForwardProxy
if SC_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
elif VX_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
else:
    ForwardProxy = ""
#Get domain
SC_DOMAIN = config.SC_DOMAIN
async def vixsrc(streams,id,client,MFP,MFP_CREDENTIALS):
    general = await is_movie(id)
    ismovie = general[0]
    clean_id = general[1]
    if "tt" in id:
        tmdb_id = await get_TMDb_id_from_IMDb_id(clean_id,client)
    else:
        tmdb_id = clean_id
    if ismovie == 0 : 
        season = int(general[2])
        episode = int(general[3])
        site_url = f'{SC_DOMAIN}/tv/{tmdb_id}/{general[2]}/{general[3]}/'
    else:
        site_url = f'{SC_DOMAIN}/movie/{tmdb_id}/' 
    streams = await vixcloud(site_url,client,MFP,MFP_CREDENTIALS,streams,"Vixcloud",proxies,ForwardProxy)
    return streams


async def streaming_community(streams,id,client,MFP,MFP_CREDENTIALS):
    try:
        if "vixsrc" in SC_DOMAIN:
            streams = await vixsrc(streams,id,client,MFP,MFP_CREDENTIALS)
        return streams
    except Exception as e:
        logger.warning(f"StreamingCommunity failed {e}")
        return streams
        


async def test_vixsrc():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        # Replace with actual id, for example 'anime_id:episode' format
        test_id = "tt6468322:1:1"  # This is an example ID format
        results = await streaming_community(test_id, client,"0","0")
        print(results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_vixsrc())










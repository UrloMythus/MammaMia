from Src.Utilities.info import  is_movie
import Src.Utilities.config as config
from Src.Utilities.loadenv import load_env  
from Src.API.extractors.vidxgo import vidxgo
import json, random
import logging
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)
env_vars = load_env()
VD_PROXY = config.VD_PROXY
proxies = {}
if VD_PROXY == "1":
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
VD_ForwardProxy = config.VD_ForwardProxy
if VD_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
else:
    ForwardProxy = ""
VD_DOMAIN = config.VD_DOMAIN



async def vidxgoalta(streams,id,client,instance_url):
    try:
        general = await is_movie(id)
        ismovie = general[0]
        clean_id = general[1]
        type = "Vidxgo"
        if "tmdb" in id:
            clean_id = await get_IMDB_id_from_TMDb_id(clean_id,client)
        if ismovie == 0 : 
            season = str(general[2])
            episode = str(general[3])
            link = f'{VD_DOMAIN}/{clean_id}/{season}/{episode}'
        elif ismovie == 1:
            link = f'{VD_DOMAIN}/{clean_id}'
        streams = await vidxgo(link,client,streams,instance_url)  
        return streams 
    except Exception as e:
        logger.info("Vidxgo failed due to ")
        logger.info(e)
        return streams

async def test_script():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        # Replace with actual id, for example 'anime_id:episode' format
        test_id = "tt7181546"  # This is an example ID format
        results = await vidxgoalta({'streams': []},test_id, client)
        print(results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_script())
    
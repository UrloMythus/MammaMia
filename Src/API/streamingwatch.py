from bs4 import BeautifulSoup,SoupStrainer 
from Src.Utilities.convert import get_TMDb_id_from_IMDb_id
from Src.Utilities.info import get_info_tmdb, is_movie, get_info_imdb
import Src.Utilities.config as config
import re
import json
from Src.API.extractors.hdplayer import hdplayer
from Src.Utilities.loadenv import load_env  
import logging
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)

SW_DOMAIN = config.SW_DOMAIN
env_vars = load_env()
SW_PROXY = config.SW_PROXY
proxies = {}
if SW_PROXY == "1":
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
SW_ForwardProxy = config.SW_ForwardProxy
if SW_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
else:
    ForwardProxy = ""


async def wponce_get(client):
    response = await client.get(ForwardProxy + f"{SW_DOMAIN}/contatto/", proxies = proxies)
    pattern = r'"admin_ajax_nonce":"(\w+)"'
    matches = re.findall(pattern, response.text)
    wponce = matches[1]
    return wponce

async def search(showname,season,episode,date,ismovie,client):
    if ismovie == 1:
        wponce = await wponce_get(client)
        query = f'{SW_DOMAIN}/wp-admin/admin-ajax.php'
        headers = {
            'authority': f'{SW_DOMAIN}',
            'accept': '*/*',
            'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'wordpress_test_cookie=WP%20Cookie%20check',
            'origin': f'{SW_DOMAIN}',
            'referer': f'{SW_DOMAIN}/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        data = {
            'action': 'data_fetch',
            'keyword': showname,
            '_wpnonce': wponce,
        }
        cookies = {
             'wordpress_test_cookie': 'WP%20Cookie%20check',
        }
        response = await client.post(ForwardProxy + query,cookies=cookies, headers=headers, data=data, proxies = proxies)
        soup = BeautifulSoup(response.content,'lxml')
        all_page_dates = soup.find_all(id = 'search-cat-year')
        all_hrefs = soup.find_all('a')
        for temp_data,temp_href in zip(all_page_dates,all_hrefs):
            page_date = temp_data.text.strip()
            if date == page_date:
                href = temp_href['href']
                href = soup.find('a')['href']
                response = await client.get(ForwardProxy + href, allow_redirects=True, proxies = proxies)
                soup = BeautifulSoup(response.text,'lxml',parse_only=SoupStrainer('iframe'))
                iframe = soup.find('iframe')
                hdplayer = iframe.get('data-lazy-src')

                return hdplayer
    elif ismovie == 0:
        #Some series have the name in english so we first search with the categories option and then we use the obtained ID to get all the episodes
        id_response = await client.get(ForwardProxy + f'{SW_DOMAIN}/wp-json/wp/v2/categories?search={showname}&_fields=id', allow_redirects=True, proxies = proxies)
        data = json.loads(id_response.text)
        category_id = data[0]['id']
        query = f'{SW_DOMAIN}/wp-json/wp/v2/posts?categories={category_id}&per_page=100'
        response = await client.get(ForwardProxy + query, allow_redirects=True, impersonate = "chrome120", proxies = proxies)
        data_json = response.text
        data = json.loads(data_json)
        for entry in data:
            if f"stagione-{season}-episodio-{episode}" in entry["slug"] or f"stagione-{season}-episode-{episode}" in entry["slug"]:
                if f"stagione-{season}-episodio-{episode}0" not in entry["slug"]:
                    content = entry["content"]["rendered"]
                #"content":{
#    "rendered":"<p><!--baslik:PRO--><iframe loading=\"lazy\" src=\"https:\/\/hdplayer.gives\/embed\/YErLVq64uNTZRNz\" frameborder=\"0\" width=\"700\" height=\"400\" allowfullscreen><\/iframe><\/p>\n","protected":false}
                    start = content.find('src="') + len('src="') #start of url
                    end = content.find('"', start) #end of url
                    hdplayer = content[start:end]
                    return hdplayer

async def streamingwatch(streams,imdb,client):
    try:
       general = await is_movie(imdb)
       ismovie = general[0]
       imdb_id = general[1]
       type = "StreamingWatch"
       if ismovie == 0:
           season  = int(general[2])
           episode = int(general[3])
           if "tt" in imdb:
               tmdba = await get_TMDb_id_from_IMDb_id(imdb_id,client)
           else:
               tmdba = imdb_id
       else:
           season = None
           episode = None
           if "tt" in imdb:
               tmdba = await get_TMDb_id_from_IMDb_id(imdb_id,client)
           else:
               tmdba = imdb_id
       showname,date = get_info_tmdb(tmdba,ismovie,type)
       showname = showname.replace(" ", "+").replace("–", "+").replace("—","+").replace("&","")
       url_hdplayer = await search(showname,season,episode,date,ismovie,client)
       streams = await hdplayer(url_hdplayer,client,streams,url_hdplayer,"Streamingwatch",proxies,ForwardProxy)
       return streams
    except Exception as e:
          logger.warning(f"MammaMia: StreamingWatch Failed {e}")
          return streams
    

async def test_animeworld():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        # Replace with actual id, for example 'anime_id:episode' format
        test_id = "tt16426418"  # This is an example ID format
        results = await streamingwatch({'streams': []},test_id, client)
        print(results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_animeworld())

from tmdbv3api import TMDb, Movie, TV
import requests
import logging 
from bs4 import BeautifulSoup,SoupStrainer
from datetime import datetime
import dateparser
from convert import get_TMDb_id_from_IMDb_id
from info import get_info_tmdb, is_movie, get_info_imdb
import config
import re
import json
SW_DOMAIN = config.SW_DOMAIN
async def search(showname,season,episode,date,ismovie,client):
    if ismovie == 1:
        query = f'https://www.streamingwatch.{SW_DOMAIN}/wp-admin/admin-ajax.php'
        headers = {
            'authority': f'www.streamingwatch.{SW_DOMAIN}',
            'accept': '*/*',
            'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'wordpress_test_cookie=WP%20Cookie%20check',
            'origin': f'https://www.streamingwatch.{SW_DOMAIN}',
            'referer': f'https://www.streamingwatch.{SW_DOMAIN}',
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
            '_wpnonce': '648328b831',
        }
        cookies = {
             'wordpress_test_cookie': 'WP%20Cookie%20check',
        }
        response = await client.post(query,cookies=cookies, headers=headers, data=data)
        soup = BeautifulSoup(response.content,'lxml')
        page_date = soup.find(id = 'search-cat-year').text.strip()
        if page_date == date:
           href = soup.find('a')['href']
           response = await client.get(href, follow_redirects=True)
           soup = BeautifulSoup(response.text,'lxml',parse_only=SoupStrainer('iframe'))
           iframe = soup.find('iframe')
           hdplayer = iframe.get('data-lazy-src')

           return hdplayer
    elif ismovie == 0:
        #Some series have the name in english so we first search with the categories option and then we use the obtained ID to get all the episodes
        id_response = await client.get(f'https://streamingwatch.{SW_DOMAIN}/wp-json/wp/v2/categories?search={showname}&_fields=id', follow_redirects=True)
        data = json.loads(id_response.text)
        category_id = data[0]['id']
        query = f'https://streamingwatch.{SW_DOMAIN}/wp-json/wp/v2/posts?categories={category_id}&per_page=100'
        response = await client.get(query, follow_redirects=True)
        data_json = response.text
        data = json.loads(data_json)
        for entry in data:
            if f"stagione-{season}-episodio-{episode}" in entry["slug"]:
                content = entry["content"]["rendered"]
                #"content":{
#    "rendered":"<p><!--baslik:PRO--><iframe loading=\"lazy\" src=\"https:\/\/hdplayer.gives\/embed\/YErLVq64uNTZRNz\" frameborder=\"0\" width=\"700\" height=\"400\" allowfullscreen><\/iframe><\/p>\n","protected":false}
                start = content.find('src="') + len('src="') #start of url
                end = content.find('"', start) #end of url
                hdplayer = content[start:end]
                return hdplayer
async def hls_url(hdplayer,client):
    response = await client.get(hdplayer, follow_redirects=True)
    match = re.search(r'sources:\s*\[\s*\{\s*file\s*:\s*"([^"]*)"', response.text)
    url = match.group(1)
    print(url)
    return url
async def streamingwatch(imdb,client):
    try:
       general = is_movie(imdb)
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
       showname = showname.replace(" ", "+").replace("–", "+").replace("—","+")
       hdplayer = await search(showname,season,episode,date,ismovie,client)
       url = await hls_url(hdplayer,client)
       return url
    except:
          print("StreamingWatch Failed")
          return None

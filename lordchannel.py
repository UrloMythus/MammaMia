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
LC_DOMAIN = config.LC_DOMAIN
def search(showname,date,season,episode,ismovie):
    cookies = {
        'csrftoken': '7lvc502CZe8Zbx7iSX1xkZOBA1NbDxJZ',
    }

    headers = {
        'authority': 'lordchannel.com',
        'accept': '*/*',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'csrftoken=7lvc502CZe8Zbx7iSX1xkZOBA1NbDxJZ',
        'referer': 'https://lordchannel.com/anime/anime-ita/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'media': showname,
        '_': '1724421723999',
    }

    response = requests.get('https://lordchannel.com/live_search/', params=params, cookies=cookies, headers=headers)
    data = json.loads(response.text)
    for entry in data['data']:
        if entry is not None:  # check if the a_tag exists
            href = entry['url']
            quality = entry['qualit\u00e0_video']
            link = f'https://lordchannel.{LC_DOMAIN}{href}'
            response = requests.get(link)
            soup2 = BeautifulSoup(response.text,'lxml')
            li_tag = soup2.select_one("ul.card__meta li:nth-of-type(2)")
            if li_tag is not None:  # check if the li_tag exists
                card_date = li_tag.text[-4:]
                if card_date == date:
                    if ismovie == 1:
                        video_url = soup2.find('a', class_="btn-streaming streaming_btn")  
                        video_url = video_url['href']
                        return video_url,quality
                    elif ismovie == 0:
                         div = soup2.find('div', id=f'collapse{season}')
                         episode = episode -1 #Index start from 0 so I need to subtract 1
                         episode = div.select('tr')[2]  # index is 2 because we want the correct  element
                         video_url = href = episode.find('a').get('href')
                         return video_url,quality
                else:
                    print("Sadly date are not equals")
                    continue

def get_m3u8(video_url):
    response = requests.get(video_url)
    pattern = r'const videoData = \[(.*?)\];'
    match = re.search(pattern, response.text)

    if match:
       video_data = match.group(1).strip().split(', ')
       url = video_data[0]
       return url

def lordchannel(imdb):
    try:
        general = is_movie(imdb)
        ismovie = general[0]
        imdb_id = general[1]
        type = "LordChannel"
        if ismovie == 0:
            season  = int(general[2])
            episode = int(general[3])
            if "tt" in imdb:
                tmdba = get_TMDb_id_from_IMDb_id(imdb_id)
            else:
                tmdba = imdb_id
        else:
            season = None
            episode = None
            if "tt" in imdb:
                tmdba = get_TMDb_id_from_IMDb_id(imdb_id)
            else:
                tmdba = imdb_id
        showname,date = get_info_tmdb(tmdba,ismovie,type)
        video_url,quality = search(showname,date,season,episode,ismovie)
        url = get_m3u8(video_url)
        url = url.replace('"','')
        print(url)
        return url,quality
    except:
        print("Lordchannel Failed")
        return None,None

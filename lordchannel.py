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
LC_DOMAIN = config.LC_DOMAIN
print(LC_DOMAIN)
def search(query,date,season,episode,ismovie):
    response = requests.get(query)
    soup = BeautifulSoup(response.text,"lxml")
    cards = soup.find_all('div', class_='col-6 col-sm-4 col-lg-3 col-xl-3')
    for card in cards:
        a_tag = card.find('a', class_='card__play')
        if a_tag is not None:  # check if the a_tag exists
            href = a_tag['href']
            link = f'https://lordchannel.{LC_DOMAIN}{href}'
            response = requests.get(link)
            soup2 = BeautifulSoup(response.text,'lxml')
            li_tag = soup2.select_one("ul.card__meta li:nth-of-type(2)")
            if li_tag is not None:  # check if the li_tag exists
                card_date = li_tag.text[-4:]
                if card_date == date:
                    quality = soup2.select('ul.card__list li')[0].text
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
                print(tmdba)
            else:
                tmdba = imdb_id
                print("HEY")
                print(tmdba)
        else:
            season = None
            episode = None
            if "tt" in imdb:
                tmdba = get_TMDb_id_from_IMDb_id(imdb_id)
            else:
                tmdba = imdb_id
        showname,date = get_info_tmdb(tmdba,ismovie,type)
        showname = showname.replace(" ", "+").replace("–", "+").replace("—","+")
        query = f'https://lordchannel.{LC_DOMAIN}/cerca/?q={showname}'
        print("HERE QUERY",query)
        video_url,quality = search(query,date,season,episode,ismovie)
        url = get_m3u8(video_url)
        url = url.replace('"','')
        print(url)
        return url,quality
    except:
        print("Lordchannel Failed")

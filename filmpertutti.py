
from tmdbv3api import TMDb, Movie, TV
import requests 
from bs4 import BeautifulSoup,SoupStrainer
import string
import re
from datetime import datetime
import dateparser
from convert import get_TMDb_id_from_IMDb_id
from info import get_info, is_movie
from convert_date import convert_US_date
import logging
import config

FT_DOMAIN = config.FT_DOMAIN

#Some basic headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.10; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.5'
}
#Map months to check if date = date
month_mapping = {
    'Jan': 'Gennaio', 'Feb': 'Febbraio', 'Mar': 'Marzo', 'Apr': 'Aprile',
    'May': 'Maggio', 'Jun': 'Giugno', 'Jul': 'Luglio', 'Aug': 'Agosto',
    'Sep': 'Settembre', 'Oct': 'Ottobre', 'Nov': 'Novembre', 'Dec': 'Dicembre'
}

def search(query,date):
    response = requests.get(query).json()
    #Get link tid of every item and then open the link to see if the date = date
    for json in response:
        link = json['link']
        tid = json['id']
        series_response = requests.get(link, headers=headers)
        series_soup = BeautifulSoup(series_response.text, 'lxml')
        release_span = series_soup.find('span', class_='released')
        if release_span:
            if release_span.text != "Data di uscita: N/A":
                date_string = release_span.text.split(': ')[-1]  # Get the date part
            for eng, ita in month_mapping.items():
                date_string = re.sub(rf'\b{eng}\b', ita, date_string)

    # Swap to YY-MM-DD formatting using dateparser
        release_date = dateparser.parse(date_string, languages=['it']).strftime("%Y-%m-%d")
        if release_date == date:
            url = link
            tid = tid
            return url, tid 
        else:
            print("Date are not equals")

def get_episode_link(season,episode,tid,url): 
    #Get the link from where we have to obtain mixdrop link
    tlink = f'{url}?show_video=true&post_id={tid}&season_id={season-1}&episode_id={episode-1}'
    return tlink


def get_film(url):
    #Get the link from where we have to obtain mixdrop link
    tlink = url + "?show_video=true"
    return tlink

def get_real_link(tlink):
    #Some basic code to get the mixdrop link
    page = requests.get(tlink, headers=headers)
    soup = BeautifulSoup(page.content, features="lxml",parse_only=SoupStrainer('iframe'))
    iframe_src = soup.find('iframe')['src']

    iframe_page = requests.get(iframe_src, headers=headers)
    iframe_soup = BeautifulSoup(iframe_page.content, features="lxml")

    mega_button = iframe_soup.find('div', attrs={'class': 'megaButton', 'rel': 'nofollow'}, string='MIXDROP')
    if mega_button:
        real_link = mega_button.get('meta-link')
        return real_link
    
def get_true_link(real_link):
    response = requests.get(real_link, headers=headers)
    [s1, s2] = re.search(r"\}\('(.+)',.+,'(.+)'\.split", response.text).group(1, 2)
    schema = s1.split(";")[2][5:-1]
    terms = s2.split("|")
    charset = string.digits + string.ascii_letters
    d = dict()
    for i in range(len(terms)):
        d[charset[i]] = terms[i] or charset[i]
    s = 'https:'
    for c in schema:
        s += d[c] if c in d else c
    return s

def filmpertutti(imdb):
    general = is_movie(imdb)
    ismovie = general[0]
    imdb_id = general[1]
    if ismovie == 0 : 
        season = int(general[2])
        episode = int(general[3])
    tmdba  = get_TMDb_id_from_IMDb_id(imdb_id)
    type = "Filmpertutti"
    showname,date = get_info(tmdba,ismovie,type)
    showname = showname.replace(" ", "+").replace("–", "+").replace("—","+")
    #Build the query
    query = f'https://filmpertutti.{FT_DOMAIN}/wp-json/wp/v2/posts?search={showname}&page=1&_fields=link,id'
    try:
        url,tid = search(query,date)
    except:
        print("No results found")
        return None
    if ismovie == 0:
        episode_link = get_episode_link(season,episode,tid,url)
        #Let's get mixdrop link 
        real_link = get_real_link(episode_link)
        #let's get delivery link, streaming link
        streaming_link = get_true_link(real_link)
        print(streaming_link)
        return streaming_link
    elif ismovie == 1:
        film_link = get_film(url)
        #Let's get mixdrop link
        real_link = get_real_link(film_link)
        #let's get delivery link, streaming link
        streaming_link = get_true_link(real_link)
        print(streaming_link)
        return streaming_link
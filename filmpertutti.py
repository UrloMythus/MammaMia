
from tmdbv3api import TMDb, Movie, TV
import requests 
from bs4 import BeautifulSoup
import string
import re
from datetime import datetime
import dateparser
import os
from dotenv import load_dotenv

load_dotenv(".env")

TMDB_KEY = os.getenv('TMDB_KEY')
DOMAIN = os.getenv('DOMAIN')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.10; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.5'
}
month_mapping = {
    'Jan': 'Gennaio', 'Feb': 'Febbraio', 'Mar': 'Marzo', 'Apr': 'Aprile',
    'May': 'Maggio', 'Jun': 'Giugno', 'Jul': 'Luglio', 'Aug': 'Agosto',
    'Sep': 'Settembre', 'Oct': 'Ottobre', 'Nov': 'Novembre', 'Dec': 'Dicembre'
}
def convert_US_date(date):
    us_data = next((country_data for country_data in date['results'] if country_data["iso_3166_1"] == "US"), None)
    if us_data:
        us_release_dates_type_3 = [rd for rd in us_data['release_dates'] if rd['type'] == 3]
        # Sort the list of release dates and get the latest
        us_release_dates_type_3.sort(key = lambda x: x['release_date'], reverse=True)
        if len(us_release_dates_type_3) > 0:
            latest_release_date = us_release_dates_type_3[0]['release_date']
            date = latest_release_date.split('T')[0]
            print('Latest US theatrical release date:', date)
            return date
def get_TMDb_id_from_IMDb_id(imdb_id):
    if ":" in imdb_id:
        season = imdb_id.split(":")[1]
        episode = imdb_id[-1]
        ismovie = 0
        imdb_id = imdb_id.split(":")[0]
    else:
        ismovie = 1
    response = requests.get(f'https://api.themoviedb.org/3/find/{imdb_id}', 
                            params={'external_source': 'imdb_id', 'api_key': f'{TMDB_KEY}'})
    tmbda = response.json()
    if tmbda['movie_results']:
        print(tmbda)
        return tmbda['movie_results'][0]['id'], ismovie
    elif tmbda['tv_results']:
        print(tmbda['tv_results'][0]['id'])
        return tmbda['tv_results'][0]['id'], season, episode , ismovie 
    else:
        return None

def get_mamma(tmbda,ismovie):
    tmdb = TMDb()
    tmdb.api_key = f'{TMDB_KEY}'
    tmdb.language = 'it'
    if ismovie == 0:
        tv = TV()
        show= tv.details(tmbda)
        showname = show.name
        date= show.first_air_date
    else:
        movie = Movie()
        show= movie.details(tmbda)
        showname= show.title
        #Get all release dates
        date = show.release_dates
        #GET US RELEASE DATE because filmpertutti somewhy uses US release date
        date = convert_US_date(date)
    if ismovie==0:
        return showname,date
    else:
        return showname,date

def search(query,date):
    response = requests.get(query)
    soup = BeautifulSoup(response.text, 'lxml')
    test= soup.find('div', class_='elementor-posts-container elementor-posts elementor-posts--skin-classic elementor-grid')
    # Find all articles
    articles = test.select('article', class_='elementor-post elementor-grid-item post-629565')

    # Loop through each article
    for article in articles:
        # Find the link inside the article
        link = article.find('a', class_='elementor-post__thumbnail__link')

        # Extract the href attribute from the link
        href = link['href']
        #replace base url for easier scraping
        #Get the correct serie by checking if the date is equals
        series_response = requests.get(href, headers=headers)
        series_soup = BeautifulSoup(series_response.text, 'lxml')
        release_span = series_soup.find('span', class_='released')  
        if release_span:
            if release_span.text != "Data di uscita: N/A":
                date_string = release_span.text.split(': ')[-1]  # Get the date part
            for eng, ita in month_mapping.items():
                date_string = re.sub(rf'\b{eng}\b', ita, date_string)

    # Swap to YY-MM-DD formatting using dateparser
        release_date = dateparser.parse(date_string, languages=['it']).strftime("%Y-%m-%d")
        print(release_date)
        if release_date == date:
            url = href
            break
    return url

def get_episode_link(season,episode,url): 
    response = requests.get(url)
    # Extract the 'link' field from the headers
    link_field = response.headers.get('Link')
    links = link_field.split(',')
    links = [link.split(';')[0].strip('<>') for link in links]
    second_link = links[2]
    #Get the ID of the serie (not tmbd  or imbd)
    tid = second_link.split("=")[1]
    episode = int(episode)
    season = int(season)
    tlink = f'{url}?show_video=true&post_id={tid}&season_id={season-1}&episode_id={episode-1}'
    return tlink


def get_film(url):
    tlink = url + "?show_video=true"
    return tlink

def get_real_link(tlink):
    page = requests.get(tlink, headers=headers)
    soup = BeautifulSoup(page.content, features="lxml")
    iframe_src = soup.find('iframe')['src']

    iframe_page = requests.get(iframe_src, headers=headers)
    iframe_soup = BeautifulSoup(iframe_page.content, features="lxml")

    mega_button = iframe_soup.find('div', attrs={'class': 'megaButton', 'rel': 'nofollow'}, string='MIXDROP')
    if mega_button:
        real_link = mega_button.get('meta-link')
        print(f'Real link: {real_link}')
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
    print(s)
    return s

def get_stream_link(imbd):
    info  = get_TMDb_id_from_IMDb_id(imbd)
    if len(info)==4 : 
        tmdba,season,episode,ismovie = info
    else:
        tmdba,ismovie = info
    showname,date = get_mamma(tmdba,ismovie)
    
    query = f'https://filmpertutti.{DOMAIN}/?s=+{showname}'
    query = query.replace(" ", "+").replace("–", "+").replace("—","+")
    print(query)
    url = search(query,date)
    print(ismovie)
    print(url)
    if ismovie == 0:
        episode_link = get_episode_link(season,episode,url)
        print(episode_link)
        #Let's get mixdrop link 
        real_link = get_real_link(episode_link)
        #let's get delivery link, streaming link
        streaming_link = get_true_link(real_link)
        return streaming_link
    elif ismovie == 1:
        film_link = get_film(url)
        print(film_link)
        #Let's get mixdrop link
        real_link = get_real_link(film_link)
        #let's get delivery link, streaming link
        streaming_link = get_true_link(real_link)
        return streaming_link

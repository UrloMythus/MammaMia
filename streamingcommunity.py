from tmdbv3api import TMDb, Movie, TV
import requests 
from bs4 import BeautifulSoup,SoupStrainer
from datetime import datetime
import dateparser
from convert import get_TMDb_id_from_IMDb_id
from loadenv import load_env
from info import get_info
TMDB_KEY= load_env()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.10; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.5'
}
def streaming_community(imbd):
    print(load_env)
    general  = get_TMDb_id_from_IMDb_id(imbd)
    if len(general)==4 : 
        tmdba,season,episode,ismovie = general
    else:
        tmdba,ismovie = general
    type = "StreamingCommunity"
    showname,date = get_info(tmdba,ismovie,type)
    showname = showname.replace(" ", "+").replace("–", "+").replace("—","+")
    query = f'https://streamingcommunity.boston/api/search?q={showname}'
    date,tid,slug = search(query,date)
    if ismovie == 0:
        url = get_film(tid)
    return "NOT IMPLEMENTED YET"

    

def search(query,date):
    response = requests.get(query).json()
    for json in response:
        release_date = json['last_air_date']
        tid = json['id']
        slug = json['slug']
        if date == release_date:
            return date,tid,slug
def get_film(tid):
    url = f'https://streamingcommunity.boston/watch/{tid}'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml', parse_only=SoupStrainer('iframe'))
    vixid = soup['src']
    vixid = vixid.split("/embed/")[1].split("?")[0]
    print (vixid)

streaming_community("tt16426418")
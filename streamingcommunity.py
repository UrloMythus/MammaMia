from tmdbv3api import TMDb, Movie, TV
import logging 
from bs4 import BeautifulSoup,SoupStrainer
from datetime import datetime
import dateparser
from convert import get_TMDb_id_from_IMDb_id
from info import get_info_tmdb, is_movie, get_info_imdb
import config
import json
import re
from urllib.parse import urlparse, parse_qs

#Get domain
SC_DOMAIN= config.SC_DOMAIN
SC_FAST_SEARCH = config.SC_FAST_SEARCH

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.10; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.5'
}

#GET VERSION OF STREAMING COMMUNITY:
async def get_version(client):
    #Extract the version from the main page of the site


    try:
        base_url = f'https://streamingcommunity.{SC_DOMAIN}/richiedi-un-titolo'
        response = await client.get(base_url, headers=headers, follow_redirects=True)
        #Soup the response
        soup = BeautifulSoup(response.text, "lxml")

        # Extract version
        version = json.loads(soup.find("div", {"id": "app"}).get("data-page"))['version']
        return version
    except:
        print("Couldn't find the version")
        version = "65e52dcf34d64173542cd2dc6b8bb75b"
        return version

async def search(query,date,ismovie, client):
    #Do a request to get the ID of serie/move and it's slug in the URL
    response = await client.get(query, follow_redirects=True)
    response = response.json()

    for item in response['data']:
        tid = item['id']
        slug = item['slug']
        type = item['type']
        if type == "tv":
            type = 0
        elif type == "movie":
            type = 1
        if type == ismovie: 
            #Added a Check to see if the result is what it is supposed to be
            if SC_FAST_SEARCH == "0":
                if ismovie == 0:
                    response = await client.get ( f'https://streamingcommunity.{SC_DOMAIN}/titles/{tid}-{slug}', follow_redirects=True)
                    pattern = r'<div[^>]*class="features"[^>]*>.*?<span[^>]*>(.*?)<\/span>'
                    match = re.search(pattern, response.text)
                    print(match.group(1).split("-")[0])
                    first_air_year = match.group(1).split("-")[0]
                    date = int(date)
                    first_air_year = int(first_air_year)
                    if first_air_year == date:
                        return tid,slug
                elif ismovie == 1:
                    return tid,slug
            elif SC_FAST_SEARCH == "1":
                 return tid,slug
        else:
            print("Couldn't find anything")

        
async def get_film(tid,version,client):  
    headers = {
            'user-agent': "Mozilla/5.0 (Windows NT 10.10; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537",
            'x-inertia': 'true',
            #Version of streaming community
            'x-inertia-version': version
        }
    #Access the iframe
    url = f'https://streamingcommunity.{SC_DOMAIN}/iframe/{tid}'
    response = await client.get(url, headers=headers, follow_redirects=True)
    iframe = BeautifulSoup(response.text, 'lxml')
    #Get the link of iframe
    iframe = iframe.find('iframe').get("src")
    #Get the ID containted in the src of iframe
    vixid = iframe.split("/embed/")[1].split("?")[0]
    parsed_url = urlparse(iframe)
    query_params = parse_qs(parsed_url.query)
    #Get real token and expires by looking at the page in the iframe, vixcloud/embed
    resp = await client.get(iframe, headers = headers, follow_redirects=True)
    soup=  BeautifulSoup(resp.text, "lxml")
    script = soup.find("body").find("script").text
    token = re.search(r"'token':\s*'(\w+)'", script).group(1)
    expires = re.search(r"'expires':\s*'(\d+)'", script).group(1)
    quality = re.search(r'"quality":(\d+)', script).group(1)
    #Example url  https://vixcloud.co/playlist/231315?b=1&token=bce060eec3dc9d1965a5d258dc78c964&expires=1728995040&rendition=1080p
    url = f'https://vixcloud.co/playlist/{vixid}?token={token}&expires={expires}'
    if 'canPlayFHD' in query_params:
       canPlayFHD = 'h=1'
       url += "&h=1"
    if 'b' in query_params:
       b = 'b=1'
       url += "&b=1"
    url720 = f'https://vixcloud.co/playlist/{vixid}'
    return url,url720,quality,

async def get_season_episode_id(tid,slug,season,episode,version,client):
    #Set some basic headers for the request
    headers = {
            'user-agent': "Mozilla/5.0 (Windows NT 10.10; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            'x-inertia': 'true', 
            #Version of streaming community
            'x-inertia-version': version
        }   
      #Get episode ID 
    response = await client.get(f'https://streamingcommunity.{SC_DOMAIN}/titles/{tid}-{slug}/stagione-{season}', headers=headers, follow_redirects=True)
    # Print the json got
    json_response = response.json().get('props', {}).get('loadedSeason', {}).get('episodes', [])
    for dict_episode in json_response:
        if dict_episode['number'] == episode:
            return dict_episode['id']

async def get_episode_link(episode_id,tid,version,client):
    #The parameters for the request
    params = {
                'episode_id': episode_id, 
                'next_episode': '1'
            }
    #Let's try to get the link from iframe source
        # Make a request to get iframe source
    response = await client.get(f"https://streamingcommunity.{SC_DOMAIN}/iframe/{tid}", params=params, follow_redirects=True)

    # Parse response with BeautifulSoup to get iframe source
    soup = BeautifulSoup(response.text, "lxml")
    iframe = soup.find("iframe").get("src")
    vixid = iframe.split("/embed/")[1].split("?")[0]
    headers = {
            'user-agent': "Mozilla/5.0 (Windows NT 10.10; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537",
            'x-inertia': 'true',
            #Version of streaming community
            'x-inertia-version': version
         }
    parsed_url = urlparse(iframe)
    query_params = parse_qs(parsed_url.query)
    #Get real token and expires by looking at the page in the iframe, vixcloud/embed
    resp = await client.get(iframe, headers = headers, follow_redirects=True)
    soup=  BeautifulSoup(resp.text, "lxml")
    script = soup.find("body").find("script").text
    token = re.search(r"'token':\s*'(\w+)'", script).group(1)
    expires = re.search(r"'expires':\s*'(\d+)'", script).group(1)
    quality = re.search(r'"quality":(\d+)', script).group(1)
    #Example url  https://vixcloud.co/playlist/231315?b=1&token=bce060eec3dc9d1965a5d258dc78c964&expires=1728995040&rendition=1080p
    url = f'https://vixcloud.co/playlist/{vixid}?token={token}&expires={expires}'
    if 'canPlayFHD' in query_params:
       canPlayFHD = 'h=1'
       url += "&h=1"
    if 'b' in query_params:
       b = 'b=1'
       url += "&b=1"
    url720 = f'https://vixcloud.co/playlist/{vixid}'
    return url,url720,quality


async def streaming_community(imdb,client):
    try:
        general = is_movie(imdb)
        ismovie = general[0]
        imdb_id = general[1]
        type = "StreamingCommunity"
        if ismovie == 0 : 
            season = int(general[2])
            episode = int(general[3])
            #Check if fast search is enabled or disabled
            if SC_FAST_SEARCH == "1":
                if "tt" in imdb:
                #Get showname
                    showname = await get_info_imdb(imdb_id,ismovie,type,client)
                    date = None
                else:
                    #I just set n season to None to avoid bugs, but it is not needed if Fast search is enabled
                    date = None
                    #else just equals them
                    tmdba = imdb_id.replace("tmdb:","")
                    showname = get_info_tmdb(tmdba,ismovie,type)
            elif SC_FAST_SEARCH == "0":
                tmdba = await get_TMDb_id_from_IMDb_id(imdb_id,client)
                showname,date = get_info_tmdb(tmdba,ismovie,type) 
        #HERE THE CASE IF IT IS A MOVIE
        else:
            if "tt" in imdb:
                #Get showname
                date = None
                showname = await get_info_imdb(imdb_id,ismovie,type,client)
            else:
                    date = None
                    tmdba = imdb_id.replace("tmdb:","")
                    showname = get_info_tmdb(tmdba,ismovie,type) 
        
        showname = showname.replace(" ", "+").replace("–", "+").replace("—","+")
        query = f'https://streamingcommunity.{SC_DOMAIN}/api/search?q={showname}'
        tid,slug = await search(query,date,ismovie,client)
        version = await get_version(client)
        if ismovie == 1:
            #TID means temporaly ID
            url,url720,quality = await get_film(tid,version,client)
            print(url)
            return url,url720,quality
        if ismovie == 0:
            #Uid = URL ID
            episode_id = await get_season_episode_id(tid,slug,season,episode,version,client)
            url,url720,quality = await get_episode_link(episode_id,tid,version,client)
            print(url)
            return url,url720,quality
    except Exception as e:
        print("StreamingCommunity failed")
        return None,None,None

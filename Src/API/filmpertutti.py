
from tmdbv3api import TMDb, Movie, TV
from bs4 import BeautifulSoup,SoupStrainer
import string
import re
import dateparser
from Src.Utilities.convert import get_TMDb_id_from_IMDb_id
from Src.Utilities.info import get_info_tmdb, is_movie, get_info_imdb
from Src.Utilities.convert_date import convert_US_date
import Src.Utilities.config as config
FT_DOMAIN = config.FT_DOMAIN
import urllib.parse
WOA = 0
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

async def search(query,date,client,season,ismovie):
    response = await client.get(query)
    response = response.json()
    #Get link tid of every item and then open the link to see if the date = date
    for json in response:
        link = json['link']
        tid = json['id']
        series_response = await client.get(link, headers=headers, allow_redirects=True, timeout = 30)
        series_soup = BeautifulSoup(series_response.text, 'lxml')
        release_span = series_soup.find('span', class_='released')
        if release_span:
            if release_span.text != "Data di uscita: N/A":
                date_string = release_span.text.split(': ')[-1]  # Get the date part
                release_date = date_string[-4:]
            if WOA:
                for eng, ita in month_mapping.items():
                    date_string = re.sub(rf'\b{eng}\b', ita, date_string)

    # Swap to YY-MM-DD formatting using dateparser
                release_date = dateparser.parse(date_string, languages=['it']).strftime("%Y-%m-%d")
        if release_date == date:
            url = link
            tid = tid
            if ismovie == 0:
                Seasons = series_soup.find_all('span', class_="season-name")
                i = 0
                for item in Seasons:
                    season_text = item.text.strip()
                    if season in season_text and "SUB" not in season_text:
                        actual_season = i
                        return url, tid, actual_season
                    else:
                        i = i + 1 
                        continue
            else:        
                actual_season = None
                return url, tid, actual_season 
        else:
            print("")

def get_episode_link(actual_season,episode,tid,url): 
    #Get the link from where we have to obtain mixdrop link
    tlink = f'{url}?show_video=true&post_id={tid}&season_id={actual_season}&episode_id={episode-1}'
    return tlink


def get_film(url):
    #Get the link from where we have to obtain mixdrop link
    tlink = url + "?show_video=true"
    return tlink

async def get_real_link(tlink,client):
    #Some basic code to get the mixdrop link
    page = await client.get(tlink, headers=headers, allow_redirects=True)
    soup = BeautifulSoup(page.content, features="lxml",parse_only=SoupStrainer('iframe'))
    iframe_src = soup.find('iframe')['src']
    iframe_page = await client.get(iframe_src, headers=headers, allow_redirects=True, timeout = 30)
    iframe_soup = BeautifulSoup(iframe_page.content, features="lxml")

    mega_button = iframe_soup.find('div', attrs={'class': 'megaButton', 'rel': 'nofollow'}, string='MIXDROP')
    if mega_button:
        real_link = mega_button.get('meta-link')
        return real_link
    
async def get_true_link(real_link,client):
    response = await client.get(real_link, headers=headers, allow_redirects=True,timeout = 30)
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

async def filmpertutti(imdb,client):
    general = is_movie(imdb)
    ismovie = general[0]
    imdb_id = general[1]
    type = "Filmpertutti"
    if ismovie == 0 : 
        season = general[2]
        episode = int(general[3])
    if "tt" in imdb:
        if ismovie == 0:
        #Get showname and date
            showname,date = await get_info_imdb(imdb_id,ismovie,type,client)
        else:
            #THIS IS needed cause the only way to get all releases dates is by giving a tmdb ID not a IMDB
            showname,date = await get_info_imdb(imdb_id,ismovie,type, client)
            season = None

    elif "tmdb" in imdb:
        #Get showname and date
        tmdba = imdb_id.replace("tmdb:","")
        showname,date = get_info_tmdb(tmdba,ismovie,type)
    showname = showname.replace(" ", "+").replace("–", "+").replace("—","+")
    showname = urllib.parse.quote_plus(showname)
    #Build the query
    query = f'https://filmpertutti.{FT_DOMAIN}/wp-json/wp/v2/posts?search={showname}&page=1&_fields=link,id'
    try:
        url,tid,actual_season = await search(query,date,client,season,ismovie)
    except:
        print("MammaMia: No results found for Filmpertutti")
        return None
    if ismovie == 0:
        episode_link =  get_episode_link(actual_season,episode,tid,url)
        #Let's get mixdrop link 
        real_link = await get_real_link(episode_link,client)
        #let's get delivery link, streaming link
        streaming_link = await get_true_link(real_link,client)
        print(streaming_link)
        return streaming_link
    elif ismovie == 1:
        film_link = get_film(url)
        #Let's get mixdrop link
        real_link = await get_real_link(film_link,client)
        #let's get delivery link, streaming link
        streaming_link = await get_true_link(real_link,client)
        return streaming_link
    

'''
async def test_animeworld():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        # Replace with actual id, for example 'anime_id:episode' format
        test_id = "tt4655480:1:1"  # This is an example ID format
        results = await filmpertutti(test_id, client)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_animeworld())


'''






'''
    series_response = await client.get(link, headers=headers, follow_redirects=True)
        series_soup = BeautifulSoup(series_response.text, 'lxml')
        release_span = series_soup.find('span', class_='released')
        if release_span:
            if release_span.text != "Data di uscita: N/A":
                date_string = release_span.text.split(': ')[-1]  # Get the date part
            for eng, ita in month_mapping.items():
                date_string = re.sub(rf'\b{eng}\b', ita, date_string)

    # Swap to YY-MM-DD formatting using dateparser
        release_date = dateparser.parse(date_string, languages=['it']).strftime("%Y-%m-%d")
'''
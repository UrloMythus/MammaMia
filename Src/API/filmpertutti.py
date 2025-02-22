
from tmdbv3api import TMDb, Movie, TV
from bs4 import BeautifulSoup,SoupStrainer
import string
import re
import dateparser
from Src.Utilities.convert import get_TMDb_id_from_IMDb_id, get_IMDB_id_from_TMDb_id
from Src.Utilities.info import get_info_tmdb, is_movie, get_info_imdb
from Src.Utilities.convert_date import convert_US_date
import Src.Utilities.config as config
FT_DOMAIN = config.FT_DOMAIN
import urllib.parse
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
async def get_streamtape(link,client):
    headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }
    response = await client.get(link, headers=headers, impersonate = "chrome124")
    regex = r"id=.*?(?=')"
    matches = re.findall(regex, response.text)
    i = 0
    final_url = next((f"https://streamtape.com/get_video?{matches[i + 1]}" for i in range(len(matches) - 1) if matches[i] == matches[i + 1]), None)
    return final_url


async def search(query,imdb_id,client,season,ismovie):
    response = await client.get(query)
    response = response.json()
    #Get link tid of every item and then open the link to see if the date = date
    for json in response:
        link = json['link']
        tid = json['id']
        series_response = await client.get(link, headers=headers, allow_redirects=True, timeout = 30)
        series_soup = BeautifulSoup(series_response.text, 'lxml')
        imdb_pattern = r"'imdb_id':\s*'([^']+)'"
        imdb_match = re.search(imdb_pattern, series_response.text)
        if imdb_match:
            id = imdb_match.group(1)
            print(id)
            if id == imdb_id:
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
            print("There's no IMDB_ID")

def get_episode_link(actual_season,episode,tid,url): 
    #Get the link from where we have to obtain mixdrop link
    tlink = f'{url}?show_video=true&post_id={tid}&season_id={actual_season}&episode_id={episode-1}'
    return tlink


def get_film(url):
    #Get the link from where we have to obtain mixdrop link
    tlink = url + "?show_video=true"
    return tlink

async def get_real_link(tlink,client):
    try:
        print(tlink)
        #Some basic code to get the mixdrop link
        page = await client.get(tlink, headers=headers, allow_redirects=True)
        soup = BeautifulSoup(page.content, features="lxml",parse_only=SoupStrainer('iframe'))
        iframe_src = soup.find('iframe')['src']
        iframe_page = await client.get(iframe_src, headers=headers, allow_redirects=True, timeout = 30)
        iframe_soup = BeautifulSoup(iframe_page.content, features="lxml", parse_only=SoupStrainer('div',class_="megaButton"))

        mega_button = iframe_soup.find('div', attrs={'class': 'megaButton', 'rel': 'nofollow'}, string='MIXDROP')
        if mega_button:
            real_link = mega_button.get('meta-link')
            return real_link
        else:
            mega_button = iframe_soup.find('div', attrs={'class': 'megaButton', 'rel': 'nofollow'}, string='STREAMTAPE')
            real_link = mega_button.get('meta-link')
            return real_link
    except Exception as e:
        print(f"Error: {e}")
        return None
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

async def filmpertutti(imdb,client,MFP):
    try:
        general = await is_movie(imdb)
        ismovie = general[0]
        imdb_id = general[1]
        type = "Filmpertutti"
        if ismovie == 0 : 
            season = general[2]
            episode = int(general[3])
        else:
            season = None
            episode = None
        if "tt" in imdb:
            showname = await get_info_imdb(imdb_id,ismovie,type,client)
        elif "tmdb" in imdb:
            #Get showname and date
            tmdba = imdb_id.replace("tmdb:","")
            imdb_id = await get_IMDB_id_from_TMDb_id(tmdba,client)
            showname = get_info_tmdb(tmdba,ismovie,type)
        showname = showname.replace(" ", "+").replace("–", "+").replace("—","+")
        showname = urllib.parse.quote_plus(showname)
        #   Build the query
        query = f'{FT_DOMAIN}/wp-json/wp/v2/posts?search={showname}&page=1&_fields=link,id'
        try:
            url,tid,actual_season = await search(query,imdb_id,client,season,ismovie)
        except:
            print("MammaMia: No results found for Filmpertutti")
            return None,None
        if ismovie == 0:
            episode_link =  get_episode_link(actual_season,episode,tid,url)
            #Let's get mixdrop link 
            real_link = await get_real_link(episode_link,client)
            if MFP == "1":
                if "mixdrop" in real_link:
                    Host = "Mixdrop"
                elif "streamtape" in real_link:
                    Host = "Streamtape"
                return real_link, Host
            #let's get delivery link, streaming link
            if "mixdrop" in real_link:
                streaming_link = await get_true_link(real_link,client)
            elif "streamtape" in real_link:
                streaming_link = await get_streamtape(real_link,client)
            Host = None
            return streaming_link, Host
        elif ismovie == 1:
            film_link = get_film(url)
            #Let's get mixdrop link
            real_link = await get_real_link(film_link,client)
            if MFP == "1":
                if "mixdrop" in real_link:
                    Host = "Mixdrop"
                elif "streamtape" in real_link:
                    Host = "Streamtape"
                return real_link, Host
            if "mixdrop" in real_link:
                streaming_link = await get_true_link(real_link,client)
            elif "streamtape" in real_link:
                streaming_link = await get_streamtape(real_link,client)
            #let's get delivery link, streaming link
            Host = None
            return streaming_link, Host
    except Exception as e:
        print(f"Filmpertutti failed: {e}")
        return None,None

async def test_animeworld():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        MFP = "1"
        # Replace with actual id, for example 'anime_id:episode' format
        test_id = "tt1190634:1:1"  # This is an example ID format
        results = await filmpertutti(test_id, client,MFP)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_animeworld())





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
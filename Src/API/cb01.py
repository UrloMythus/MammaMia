import re
from bs4 import BeautifulSoup,SoupStrainer
from Src.Utilities.info import is_movie,get_info_tmdb,get_info_imdb
from Src.Utilities.convert import get_TMDb_id_from_IMDb_id
from fake_headers import Headers
import Src.Utilities.config as config
from Src.Utilities.loadenv import load_env
CB_DOMAIN = config.CB_DOMAIN
CB_PROXY = config.CB_PROXY
MX_PROXY = config.MX_PROXY
proxies = {}
proxies2 = {}
env_vars = load_env()
import random
import json
if MX_PROXY == "1":
    PROXY_CREDENTIALS = env_vars.get('PROXY_CREDENTIALS')
    proxy_list = json.loads(PROXY_CREDENTIALS)
    proxy = random.choice(proxy_list)
    if proxy == "":
        proxies2 = {}
    else:
        proxies2 = {
            "http": proxy,
            "https": proxy
        }      
if CB_PROXY == "1":
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
        proxies2 = proxies
 
CB_ForwardProxy = config.CB_ForwardProxy
MX_ForwardProxy = config.MX_ForwardProxy
if CB_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
    ForwardProxy2 = ForwardProxy
    if MX_ForwardProxy == "1":
        ForwardProxy2 = ForwardProxy
elif MX_ForwardProxy == "1":
    ForwardProxy2 = env_vars.get('ForwardProxy')
else:
    ForwardProxy2 = ""
    ForwardProxy = ""


fake_headers = Headers()

async def get_stayonline(link,client):
    headers = {
                    'origin': 'https://stayonline.pro',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0',
                    'x-requested-with': 'XMLHttpRequest',
                }
    data = {'id': link.split("/")[-2], 'ref': ''}
    response = await client.post('https://stayonline.pro/ajax/linkEmbedView.php', headers=headers, data=data, proxies = proxies2)
    real_url = response.json()['data']['value']
    return real_url


async def get_uprot(link,client):
        if "msf" in link:
             link = link.replace("msf","mse")    
        headers = fake_headers.generate()
        response = await client.get(ForwardProxy2 + link, headers=headers, allow_redirects=True, timeout=10, proxies=proxies2, impersonate = "chrome124")
        soup = BeautifulSoup(response.text, "lxml")
        maxstream_url = soup.find("a")
        maxstream_url = maxstream_url.get("href")
        return maxstream_url

async def get_true_link_mixdrop(real_link,client,MFP):
    try:
        import string
        if "club" in real_link:
            real_link = real_link.replace("club","ps").split('/2')[0] 

        if MFP == "1":
             return real_link
        headers = fake_headers.generate()
        response = await client.get(real_link, headers=headers, allow_redirects=True,timeout = 30, impersonate = "chrome124")
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
    except Exception as e:
        print(e)
        return None
async def get_true_link_maxstream(maxstream_url,client):
        headers = fake_headers.generate()    
        # Send a GET request to the Maxstream URL)
        response = await client.get(ForwardProxy2 + maxstream_url, headers=headers, allow_redirects=True, timeout=10,proxies = proxies2, impersonate = "chrome124")
        [s1, s2] = re.search(r"\}\('(.+)',.+,'(.+)'\.split", response.text).group(1, 2)
        terms = s2.split("|")
        urlset_index = terms.index('urlset')
        hls_index = terms.index('hls')
        sources_index =  terms.index('sources')
        result = terms[urlset_index + 1 : hls_index]
        reversed_elements = result[::-1]
        first_part = terms[hls_index +1 : sources_index]
        reversed_first_part = first_part[::-1]
        first_url_part = ""
        for first_part in reversed_first_part:
                if "0" in first_part:
                        first_url_part += first_part
                else:
                        first_url_part += first_part + "-"  
        


        base_url = f"https://{first_url_part}.host-cdn.net/hls/" 
        if len(reversed_elements) == 1:
                final_url = base_url + "," + reversed_elements[0] + ".urlset/master.m3u8"
        lenght = len(reversed_elements)
        i = 1    
        for element in reversed_elements:
                base_url += element + ","
                if lenght == i:
                        base_url += ".urlset/master.m3u8"
                else:
                        i += 1
        final_url = base_url
        return final_url

async def search_movie(showname,date,client):
    try:
        showname = showname.replace(" ","+").replace("ò","o").replace("è","e").replace("à","a").replace("ù","u").replace("ì","i")  
        headers = fake_headers.generate()
        headers['Referer'] = f'https://cb01new.{CB_DOMAIN}/'
        query = f'https://cb01new.{CB_DOMAIN}/?s={showname}'
        response = await client.get(ForwardProxy + query,headers=headers, impersonate = "chrome124", proxies = proxies)
        if response.status_code != 200:
            print(f"CB01 Failed to fetch search results: {response.status_code}")
        soup = BeautifulSoup(response.text, 'lxml',parse_only=SoupStrainer('div', class_='card-content'))
        cards = soup.find_all('div', class_='card-content')
        year_pattern = re.compile(r'(19|20)\d{2}')
        for card in cards:
    # Find the link inside the current card
            link_tag = card.find('h3', class_='card-title').find('a')
            href = link_tag['href']
    # Find the date span and extract possible years

            date_text = href.split("/")[-2]
                # Search for the first occurrence of a year (starting with 19 or 20)
            match = year_pattern.search(date_text)
            if match:
                year = match.group(0)
                if year == date :  # Check if the year is 2011
                    return href
    except Exception as e:
        print(f'MammaMia: Error in search_series cb01: {e}')


async def search_series(showname,date,client):
    try:
        showname = showname.replace(" ","+")
        headers = fake_headers.generate()
        headers['Referer'] = f'https://cb01new.{CB_DOMAIN}/serietv/'
        query = f'https://cb01new.{CB_DOMAIN}/serietv/?s={showname}'
        response = await client.get(ForwardProxy + query,headers=headers,impersonate = "chrome124", proxies = proxies)
        if response.status_code != 200:
            print(f"CB01 Failed to fetch search results: {response.status_code}")
        soup = BeautifulSoup(response.text, 'lxml',parse_only=SoupStrainer('div', class_='card-content'))
        cards = soup.find_all('div', class_='card-content')
        year_pattern = re.compile(r'(19|20)\d{2}')
        for card in cards:
    # Find the link inside the current card
            link_tag = card.find('h3', class_='card-title').find('a')
            href = link_tag['href']
    
    # Find the date span and extract possible years
            date_span = card.find('span', style=re.compile('color'))
            if date_span:
                date_text = date_span.text
                # Search for the first occurrence of a year (starting with 19 or 20)
                match = year_pattern.search(date_text)
                if match:
                    year = match.group(0)
                    if year == date :  # Check if the year is 2011
                        return href
    except Exception as e:
        print(f'MammaMia: Error in search_series cb01: {e}')

async def movie_redirect_url(link,client,MFP):
        headers = fake_headers.generate()
        response = await client.get(ForwardProxy + link, headers=headers, allow_redirects=True, timeout=10, impersonate = "chrome124", proxies = proxies)
        # Extract the redirect URL from the HTML
        soup = BeautifulSoup(response.text, "lxml",parse_only=SoupStrainer('div'))
        redirect_url = soup.find("div", id="iframen2").get("data-src")
        try:
            if "stayonline" in redirect_url:
                mixdrop_real_link = await get_stayonline(redirect_url,client)
                final_url = await get_true_link_mixdrop(mixdrop_real_link,client,MFP)
                return final_url
        except Exception as e:  
            redirect_url = soup.find("div", id="iframen1").get("data-src")
            if "stayonline" in redirect_url:
                    redirect_url =await get_stayonline(redirect_url,client)
            maxstream_real_link = await get_uprot(redirect_url,client)
            final_url = await get_true_link_maxstream(maxstream_real_link,client) 
            return(final_url)

        return redirect_url
async def series_redirect_url(link,season,episode,client,MFP):
        if len(episode) == 1:
                        episode = f'0{episode}'
        headers = fake_headers.generate()
        response = await client.get(ForwardProxy + link, headers=headers, allow_redirects=True, timeout=10,impersonate = "chrome124", proxies = proxies)
        soup = BeautifulSoup(response.text, "lxml")     
        seasons_text = soup.find_all('div', class_='sp-head')
        for season_text in seasons_text:
            text = season_text.text
            if f'STAGIONE' in text and f'{season}' in text:
                text = text.replace("STAGIONE","").replace("ITA", "")
                if "A" in text:
                    if len(season) == 1:
                        season = f'0{season}'
                    sp_body = season_text.find_next('div', class_='sp-body')
                    link_tag = sp_body.find('a')
                    uprot_long = link_tag.get('href')
                    response = await client.get(ForwardProxy + uprot_long, headers=headers, allow_redirects=True, timeout=10, impersonate = "chrome124", proxies = proxies)
                    season = "01"
                    episode = "04"
                    pattern1 = rf"(?i)\S*?\.{season}x{episode}\S*?\.mkv.*?href=['\"](.*?)['\"]"
                    pattern2 = rf"\S*\.S{season}E{episode}\S*?\.mkv|\.mp4|\.avi.*?href=['\"](.*?)['\"]"
                    match = re.search(pattern1, response.text)
                    if match:
                            maxstream_link = match.group(1)
                    else:
                         match = re.search(pattern2, response.text)
                         if match:
                              maxstream_link = match.group(1)
                    if "stayonline" in maxstream_link:
                            maxstream_link =await get_stayonline(maxstream_link,client)
                    maxstream_real_link = await get_uprot(maxstream_link,client)
                    final_url = await get_true_link_maxstream(maxstream_real_link,client)
                    return final_url
                else:
                    pattern = re.compile(r'4&#215;03\s*&#8211;.*?<a href="(.*?)".*?>Maxstream</a>\s*&#8211;.*?<a href="(.*?)".*?>Mixdrop</a>', re.DOTALL)
                    match = pattern.search(response.text)
                    maxstream_link = match.group(1)
                    mixdrop_link = match.group(2)
                    print(f"Maxstream: {maxstream_link}")
                    print(f"Mixdrop: {mixdrop_link}")
                    mixdrop_real_link = await get_stayonline(mixdrop_link,client)
                    final_url = await get_true_link_mixdrop(mixdrop_real_link,client,MFP)
                    if final_url == None:
                        if "stayonline" in maxstream_link:
                            maxstream_link =await get_stayonline(maxstream_link,client)
                        maxstream_real_link = await get_uprot(maxstream_link,client)
                        final_url = await get_true_link_maxstream(maxstream_real_link,client)                        
                        return final_url



async def cb01(id,client,MFP):
    try:
        general = await is_movie(id)
        ismovie = general[0]
        real_id = general[1]
        type = "Cb01"
        if "tt" in id:
            showname, date = await get_info_imdb(real_id,ismovie,type,client)
        elif  "tmdb" in real_id:
            showname, date = get_info_tmdb(real_id,ismovie,type)
        if ismovie == 0:
            season = general[2]
            episode = general[3]
            link = await search_series(showname,date,client)
            final_url = await series_redirect_url(link,season,episode,client,MFP)
            return final_url
        elif ismovie == 1:
            season = None
            episode = None
            link = await search_movie(showname,date,client)
            redirect_url = await movie_redirect_url(link,client,MFP)
            return redirect_url
    except Exception as e:
        print(f'MammaMia: Error in cb01: {e}')
        return None



















async def test_animeworld():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        # Replace with actual id, for example 'anime_id:episode' format
        test_id = "tt0045247"  # This is an example ID format
        MFP = "1"
        results = await cb01(test_id, client,MFP)
        print(results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_animeworld())

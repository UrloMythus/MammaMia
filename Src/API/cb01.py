import re
from bs4 import BeautifulSoup,SoupStrainer
from Src.Utilities.info import is_movie,get_info_tmdb,get_info_imdb
from Src.Utilities.convert import get_TMDb_id_from_IMDb_id
from fake_headers import Headers

fake_headers = Headers()

async def get_stayonline(link,client):
    headers = {
                    'origin': 'https://stayonline.pro',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0',
                    'x-requested-with': 'XMLHttpRequest',
                }
    data = {'id': link.split("/")[-2], 'ref': ''}
    response = await client.post('https://stayonline.pro/ajax/linkEmbedView.php', headers=headers, data=data)
    real_url = response.json()['data']['value']
    print(real_url)
    return real_url


async def get_uprot(link,client):
        if "msf" in link:
             link = link.replace("msf","mse")

        headers = fake_headers.generate()
        response = await client.get(link, headers=headers, allow_redirects=True, timeout=10)
        soup = BeautifulSoup(response.text, "lxml")
        maxstream_url = soup.find("a")
        maxstream_url = maxstream_url.get("href")
        return maxstream_url

async def get_true_link_mixdrop(real_link,client):
    try:
        import string
        headers = fake_headers.generate()
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
        print(s)    
        return s
    except Exception as e:
        return None
async def get_true_link_maxstream(maxstream_url,client):
        headers = fake_headers.generate()
        # Send a GET request to the Maxstream URL
        response = await client.get(maxstream_url, headers=headers, allow_redirects=True, timeout=10)
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
        showname = showname.replace(" ","+")
        headers = fake_headers.generate()
        headers['Referer'] = 'https://cb01.technology/'
        query = f'https://cb01.technology/?s={showname}'
        response = await client.get(query,headers=headers)
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
                        print(f"Link: {href}")
                        return href
    except Exception as e:
        print(f'MammaMia: Error in search_series cb01: {e}')


async def search_series(showname,date,client):
    try:
        showname = showname.replace(" ","+")
        headers = fake_headers.generate()
        headers['Referer'] = 'https://cb01.technology/serietv/'
        query = f'https://cb01.technology/serietv/?s={showname}'
        response = await client.get(query,headers=headers)
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
                        print(f"Link: {href}")
                        return href
    except Exception as e:
        print(f'MammaMia: Error in search_series cb01: {e}')

async def movie_redirect_url(link,client):
        headers = fake_headers.generate()
        response = client.get(link, headers=headers, allow_redirects=True, timeout=10)
        # Extract the redirect URL from the HTML
        soup = BeautifulSoup(response.text, "lxml",parse_only=SoupStrainer('div', id='iframen1'))
        redirect_url = soup.find("div", id="iframen1").get("data-src")
        return redirect_url
async def series_redirect_url(link,season,episode,client):
        if len(episode) == 1:
                        episode = f'0{episode}'
        headers = fake_headers.generate()
        response = await client.get(link, headers=headers, allow_redirects=True, timeout=10)
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
                    response = await client.get(uprot_long, headers=headers, allow_redirects=True, timeout=10)
                    season = "01"
                    episode = "04"
                    pattern1 = rf"(?i)\S*?\.{season}x{episode}\S*?\.mkv.*?href=['\"](.*?)['\"]"
                    pattern2 = rf"\S*\.S{season}E{episode}\S*?\.mkv.*?href=['\"](.*?)['\"]"
                    match = re.search(pattern1, response.text)
                    if match:
                            maxstream_link = match.group(1)
                    else:
                         match = re.search(pattern2, response.text)
                         if match:
                              maxstream_link = match.group(1)
                    print(maxstream_link)
                    if "stayonline" in maxstream_link:
                            maxstream_link =await get_stayonline(maxstream_link,client)
                    maxstream_real_link = await get_uprot(maxstream_link,client)
                    final_url = await get_true_link_maxstream(maxstream_real_link,client)
                    print(final_url)

                else:
                    pattern = re.compile(r'4&#215;03\s*&#8211;.*?<a href="(.*?)".*?>Maxstream</a>\s*&#8211;.*?<a href="(.*?)".*?>Mixdrop</a>', re.DOTALL)
                    match = pattern.search(response.text)
                    maxstream_link = match.group(1)
                    mixdrop_link = match.group(2)
                    print(f"Maxstream: {maxstream_link}")
                    print(f"Mixdrop: {mixdrop_link}")
                    mixdrop_real_link = await get_stayonline(mixdrop_link,client)
                    final_url = await get_true_link_mixdrop(mixdrop_real_link,client)
                    if final_url == None:
                        if "stayonline" in maxstream_link:
                            maxstream_link =await get_stayonline(maxstream_link,client)
                        maxstream_real_link = await get_uprot(maxstream_link,client)
                        final_url = await get_true_link_maxstream(maxstream_real_link,client)
                        print(final_url)
                        




async def cb01(id,client):
    try:
        general = is_movie(id)
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
            redirect_url = await series_redirect_url(link,season,episode,client)
        elif ismovie == 1:
            season = None
            episode = None
            link = await search_movie(showname,date,client)
            redirect_url = await movie_redirect_url(link,client)
    except Exception as e:
        print(f'MammaMia: Error in cb01: {e}')
        return None


















'''
async def test_animeworld():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        # Replace with actual id, for example 'anime_id:episode' format
        test_id = "tt0158552:1:1"  # This is an example ID format
        results = await cb01(test_id, client)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_animeworld())
'''


from tmdbv3api import TMDb, Movie, TV
from bs4 import BeautifulSoup,SoupStrainer
from Src.Utilities.convert import get_TMDb_id_from_IMDb_id
from Src.Utilities.info import get_info_tmdb, is_movie, get_info_imdb
import Src.Utilities.config as config
import re
import json
LC_DOMAIN = config.LC_DOMAIN

async def search(showname,date,season,episode,ismovie,client):
    cookies = {
        'csrftoken': '7lvc502CZe8Zbx7iSX1xkZOBA1NbDxJZ',
    }

    headers = {
        'authority': f'lordchannel.{LC_DOMAIN}',
        'accept': '*/*',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'csrftoken=7lvc502CZe8Zbx7iSX1xkZOBA1NbDxJZ',
        'referer': f'{LC_DOMAIN}/anime/anime-ita/',
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
    
    try:
        response = await client.get(f'{LC_DOMAIN}/live_search/', params=params, cookies=cookies, headers=headers, allow_redirects=True, impersonate = "chrome120")
        
        if response.status_code != 200:
            print(f"LordChannel search failed with status: {response.status_code}")
            return None, None
            
        data = response.json()
        
        if not data or 'data' not in data:
            print("LordChannel: No data in response")
            return None, None
            
        for entry in data['data']:
            if entry is not None:  # check if the a_tag exists
                href = entry.get('url')
                quality = entry.get('qualità_video', 'Unknown')
                
                if not href:
                    continue
                    
                link = f'{LC_DOMAIN}{href}'
                response = await client.get(link, allow_redirects=True, impersonate = "chrome120")
                soup2 = BeautifulSoup(response.text,'lxml')
                li_tag = soup2.select_one("ul.card__meta li:nth-of-type(2)")
                
                if li_tag is not None:  # check if the li_tag exists
                    card_date = li_tag.text[-4:]
                    if card_date == date:
                        if ismovie == 1:
                            video_url_tag = soup2.find('a', class_="btn-streaming streaming_btn")
                            if video_url_tag and 'href' in video_url_tag.attrs:
                                video_url = video_url_tag['href']
                                return video_url, quality
                        elif ismovie == 0:
                            div = soup2.find('div', id=f'collapse{season}')
                            if div:
                                episodes = div.select('tr')
                                if len(episodes) > episode:
                                    episode_find = episodes[episode]
                                    link_tag = episode_find.find('a')
                                    if link_tag and 'href' in link_tag.attrs:
                                        video_url = link_tag.get('href')
                                        return video_url, quality
                    else:
                        continue
        
        print("LordChannel: No matching results found")
        return None, None
        
    except Exception as e:
        print(f"LordChannel search error: {e}")
        return None, None

async def get_m3u8(video_url,client):
    response = await client.get(video_url, allow_redirects=True, impersonate = "chrome120")
    pattern = r'https?://[^\s]+\.m3u8'
    match = re.search(pattern, response.text)
    if match:
       url = match.group(0)
       return url

async def lordchannel(imdb,client):
    try:
        general = await is_movie(imdb)
        ismovie = general[0]
        imdb_id = general[1]
        type = "LordChannel"
        if ismovie == 0:
            season  = int(general[2])
            episode = int(general[3])
            if "tt" in imdb:
                tmdba =  await get_TMDb_id_from_IMDb_id(imdb_id,client)
            else:
                tmdba = imdb_id
        else:
            season = None
            episode = None
            if "tt" in imdb:
                tmdba = await get_TMDb_id_from_IMDb_id(imdb_id,client)
            else:
                tmdba = imdb_id
        
        showname,date = get_info_tmdb(tmdba,ismovie,type)
        
        if not showname or not date:
            print("LordChannel: Failed to get show info")
            return None, None
            
        search_result = await search(showname,date,season,episode,ismovie,client)
        
        if not search_result or search_result[0] is None or search_result[1] is None:
            print("LordChannel: Search returned no results")
            return None, None
            
        video_url, quality = search_result
        
        if not video_url:
            print("LordChannel: No video URL found")
            return None, None
            
        url = await get_m3u8(video_url,client)
        
        if not url:
            print("LordChannel: Failed to get m3u8 URL")
            return None, None
            
        url = url.replace('"','')
        print("MammaMia: Found results for LordChannel")
        return url,quality
        
    except Exception as e:
        print("MammaMia: Lordchannel Failed",e)
        return None,None

'''
async def test_animeworld():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        results = await lordchannel("tt0920489:3:2",client)
        print(results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_animeworld())  
    #python3 -m Src.API.lordchannel
'''
from bs4 import BeautifulSoup,SoupStrainer 
from Src.Utilities.convert import get_TMDb_id_from_IMDb_id
from Src.Utilities.info import get_info_tmdb, is_movie, get_info_imdb
import Src.Utilities.config as config
import re
import json
SW_DOMAIN = config.SW_DOMAIN
async def wponce_get(client):
    response = await client.get(f"{SW_DOMAIN}/contatto/")
    pattern = r'"admin_ajax_nonce":"(\w+)"'
    matches = re.findall(pattern, response.text)
    wponce = matches[1]
    return wponce

async def search(showname,season,episode,date,ismovie,client):
    if ismovie == 1:
        try:
            wponce = await wponce_get(client)
            if not wponce:
                print("StreamingWatch: Failed to get wponce")
                return None
                
            query = f'{SW_DOMAIN}/wp-admin/admin-ajax.php'
            headers = {
                'authority': f'{SW_DOMAIN}',
                'accept': '*/*',
                'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': f'{SW_DOMAIN}',
                'referer': f'{SW_DOMAIN}/',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }
            data = {
                'action': 'data_fetch',
                'keyword': showname,
                '_wpnonce': wponce,
            }
            cookies = {
                 'wordpress_test_cookie': 'WP%20Cookie%20check',
            }
            response = await client.post(query,cookies=cookies, headers=headers, data=data)
            
            if response.status_code != 200:
                print(f"StreamingWatch: Search failed with status {response.status_code}")
                return None
                
            soup = BeautifulSoup(response.content,'lxml')
            all_page_dates = soup.find_all(id = 'search-cat-year')
            all_hrefs = soup.find_all('a')
            
            for temp_data,temp_href in zip(all_page_dates,all_hrefs):
                if temp_data and temp_href:
                    page_date = temp_data.text.strip() if temp_data.text else ""
                    if date == page_date:
                        href = temp_href.get('href')
                        if href:
                            response = await client.get(href, allow_redirects=True, impersonate = "chrome124")
                            soup = BeautifulSoup(response.text,'lxml',parse_only=SoupStrainer('iframe'))
                            iframe = soup.find('iframe')
                            if iframe:
                                hdplayer = iframe.get('data-lazy-src')
                                if hdplayer:
                                    return hdplayer
            return None
            
        except Exception as e:
            print(f"StreamingWatch movie search error: {e}")
            return None
            
    elif ismovie == 0:
        try:
            #Some series have the name in english so we first search with the categories option and then we use the obtained ID to get all the episodes
            id_response = await client.get(f'{SW_DOMAIN}/wp-json/wp/v2/categories?search={showname}&_fields=id', allow_redirects=True, impersonate = "chrome120")
            
            if id_response.status_code != 200:
                print(f"StreamingWatch: Categories search failed with status {id_response.status_code}")
                return None
                
            data = id_response.json()
            
            if not data or len(data) == 0:
                print("StreamingWatch: No categories found")
                return None
                
            category_id = data[0].get('id')
            if not category_id:
                print("StreamingWatch: No category ID found")
                return None
                
            query = f'{SW_DOMAIN}/wp-json/wp/v2/posts?categories={category_id}&per_page=100'
            response = await client.get(query, allow_redirects=True, impersonate = "chrome120")
            
            if response.status_code != 200:
                print(f"StreamingWatch: Posts search failed with status {response.status_code}")
                return None
                
            data_json = response.text
            data = json.loads(data_json)
            
            for entry in data:
                if entry and 'slug' in entry:
                    slug = entry['slug']
                    if f"stagione-{season}-episodio-{episode}" in slug or f"stagione-{season}-episode-{episode}" in slug:
                        if f"stagione-{season}-episodio-{episode}0" not in slug:
                            content = entry.get("content", {}).get("rendered", "")
                            if content:
                                start = content.find('src="') + len('src="') #start of url
                                end = content.find('"', start) #end of url
                                if start > len('src="') - 1 and end > start:
                                    hdplayer = content[start:end]
                                    return hdplayer
            return None
            
        except Exception as e:
            print(f"StreamingWatch series search error: {e}")
            return None
async def hls_url(hdplayer,client):
    response = await client.get(hdplayer, allow_redirects=True, impersonate = "chrome120")
    match = re.search(r'sources:\s*\[\s*\{\s*file\s*:\s*"([^"]*)"', response.text)
    url = match.group(1)

    return url
async def streamingwatch(imdb,client):
    try:
       general = await is_movie(imdb)
       ismovie = general[0]
       imdb_id = general[1]
       type = "StreamingWatch"
       if ismovie == 0:
           season  = int(general[2])
           episode = int(general[3])
           if "tt" in imdb:
               tmdba = await get_TMDb_id_from_IMDb_id(imdb_id,client)
           else:
               tmdba = imdb_id
       else:
           season = None
           episode = None
           if "tt" in imdb:
               tmdba = await get_TMDb_id_from_IMDb_id(imdb_id,client)
           else:
               tmdba = imdb_id
       
       showname_date = get_info_tmdb(tmdba,ismovie,type)
       
       if not showname_date or len(showname_date) < 2:
           print("StreamingWatch: Failed to get show info")
           return None, None
           
       showname, date = showname_date
       
       if not showname:
           print("StreamingWatch: No showname found")
           return None, None
           
       showname = showname.replace(" ", "+").replace("–", "+").replace("—","+").replace("&","")
       hdplayer = await search(showname,season,episode,date,ismovie,client)
       
       if not hdplayer:
           print("StreamingWatch: No hdplayer found")
           return None, None
           
       url = await hls_url(hdplayer,client)
       
       if url:
           #Fix for Exoplayer which needs .m3u8 in the url to play the file
           url = url + ".m3u8"
           return url, hdplayer
       else:
           print("StreamingWatch: Failed to get HLS URL")
           return None, None
           
    except Exception as e:
          print("MammaMia: StreamingWatch Failed",e)
          return None,None

async def test_animeworld():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        # Replace with actual id, for example 'anime_id:episode' format
        test_id = "tt1190634:4:8"  # This is an example ID format
        results = await streamingwatch(test_id, client)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_animeworld())

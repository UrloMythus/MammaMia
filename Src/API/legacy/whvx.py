from Src.Utilities.info import is_movie,get_info_imdb,get_info_tmdb
import json
import urllib.parse
#This doesn't work anymore.
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Origin': 'https://www.vidbinge.com',
    'DNT': '1',
    'Sec-GPC': '1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Connection': 'keep-alive',
    'Priority': 'u=4',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}









async def whvx(id,client):
    general = is_movie(id)
    ismovie = general[0]
    imdb_id = general[1]
   
    type = "Whvx"    
    if ismovie == 0:
        ismovie2 = "tv"
        season = general[2]
        episode = general[3]
    elif ismovie == 1:
        ismovie2 = "movie"
        season = ""
        episode = ""
    if "tt" in id:
        showname,date = await get_info_imdb(imdb_id,ismovie,type,client)
   
        params = {
            "query": {
                "title": showname,
                "releaseYear": date,
                "imdbId": imdb_id,
                "type": ismovie2,
                "season": season,
                "episode": episode
            },
            "provider": "nova"
        }


        
    elif "tmdb" in id:
        showname,date = get_info_tmdb(id,ismovie,type)
        params = {
            "query": {
                "title": showname,
                "releaseYear": date,
                "tmdbId": imdb_id,
                "type": ismovie2,
                "season": season,
                "episode": episode
            },
            "provider": "nova"
        }
    showname = urllib.parse.quote_plus(showname)
    response = await client.get(f'https://api.whvx.net/search', params = params,  headers=headers, impersonate = "chrome120")
    data = json.loads(response.text)
    print(data)
    url = data['url']
    print(data)
    params = {
        'resourceId': url,
        'provider': 'nova',
    }


    headers2 = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Origin': 'https://www.vidbinge.com',
        'DNT': '1',
        'Sec-GPC': '1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Connection': 'keep-alive',
        'Priority': 'u=4',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }
    response = await client.get('https://api.whvx.net/source', params=params, headers=headers2, impersonate = "chrome120")
    data = json.loads(response.text)
    resolution_links = {}
    for quality, details in data['stream'][0]['qualities'].items():
        resolution_links[quality] = details['url']
    print(resolution_links)
    return resolution_links


async def test_animeworld():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        # Replace with actual id, for example 'anime_id:episode' format
        test_id = "tt6263850"  # This is an example ID format
        results = await whvx(test_id, client)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_animeworld())



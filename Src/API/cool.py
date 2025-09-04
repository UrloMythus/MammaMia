import json
from Src.Utilities.info import get_info_tmdb,is_movie
from Src.Utilities.convert import get_TMDb_id_from_IMDb_id
from Src.Utilities.loadenv import load_env  
env_vars = load_env()
ForwardProxy = env_vars.get('ALTERNATIVE_LINK')
MYSTERIUS_KEY = env_vars.get('MYSTERIUS_KEY')

async def get_links(slug,season,episode,ismovie,client):
    try:
        headers = {
            "x-api-key": MYSTERIUS_KEY
        }
        response = await client.get("https://aimammam-ulala12431.hf.space/api/cookie", headers=headers)
        Auths = response.json()
        Bearer = Auths.get('cookie')
        ap_session = Auths.get('auth')
        
        cookies = {'ap_session': ap_session}
        print(cookies)
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': f'Bearer {Bearer}',
            'referer': f'https://altadefinizioneapp.com/play/{slug}',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0',
            'x-requested-with': 'XMLHttpRequest',
        }
        if ismovie == 1:

            response = await client.get(f'https://altadefinizioneapp.com/api/post/urls/stream/{slug}',cookies=cookies,headers=headers)
        elif ismovie == 0:
            request_url =f'https://altadefinizioneapp.com/api/post/urls/stream/{slug}/{season}/{episode}'
            print(request_url)
            response = await client.get(request_url,cookies=cookies,headers=headers)
        try:
            video_data = response.json()  # Assuming this is the JSON response containing video streams
            if 'streams' not in video_data:
                print("Invalid JSON format: 'streams' key not found or incorrect structure")
                return None
            
            streams = video_data['streams']

            resolutions = {}

            for stream in streams:
                resolution_name = stream['resolution']['name'].lower()  # Convert resolution name to lowercase
                url = stream['url']

                # Remove everything after '.mp4' in the URL
                mp4_index = url.find('.mp4')
                if mp4_index != -1:
                    url = url[:mp4_index + 4]  # +4 to include '.mp4' in the substring

                resolutions[resolution_name] = url
            
            return resolutions

        except KeyError as e:
            print(f"KeyError: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"JSONDecodeError: {e}")
            return None

    except Exception as e:
        print(f"Request error: {e}")
        return None
    

# Example usage: Fetch video links


# Print the dictionary





async def search_imdb(showname,tmdba,client):
        showname = showname.replace(" ","%20")
        tmdba = str(tmdba)
        query = f'https://altadefinizioneapp.com/api/search?search={showname}&page=1'
        response = await client.get(query,allow_redirects=True, impersonate = "chrome120")
        if response.status_code == 200:
            data = response.json()
            if 'data' in data:
                for item in data['data']:
                    tmdb_id = item.get('tmdb_id')
                    tmdb_id = ''.join(char for char in tmdb_id if char.isdigit())
                    if tmdb_id == tmdba:
                        slug = item.get('slug')
                        return slug
                    


def parse_links(resolution_links):  
    results = {}      
    if resolution_links:
        for resolution, link in resolution_links.items():
            if "cdn.altadefinizione-originale.com" in link or "cdn.altadefinizioneapp.com" in link:
                link = link.replace("cdn.altadefinizione-originale.com","protectlinknt.b-cdn.net").replace("cdn.altadefinizioneapp.com","protectlinknt.b-cdn.net")
            results[resolution] = link
        return results    
    else:
        print("Failed to fetch video links")


async def cool(imdb,client):
    try:
        type = "Cool"    
        general = await is_movie(imdb)
        ismovie = general[0]
        imdb_id = general[1]
        if ismovie == 0 : 
            season = int(general[2])
            episode = int(general[3])
        
        if "tt" in imdb:
                #Get showname
            tmdba = await get_TMDb_id_from_IMDb_id(imdb_id,client)
        else:
            tmdba = imdb_id.replace("tmdb:","")

        showname = get_info_tmdb(tmdba,ismovie,type)
        

        slug = await search_imdb(showname,tmdba,client)
        if ismovie == 1:
            season = None
            episode = None
            resolution_links = await get_links(slug,episode,season,ismovie,client)
            results = parse_links(resolution_links)
            return results
        elif ismovie == 0:
            season = season -1
            episode = episode - 1
            resolution_links = await get_links(slug,season,episode,ismovie,client)
            results = parse_links(resolution_links)
            return results
    except Exception as e:
        print("Cool Error",e)
        return None

async def test_animeworld():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        # Replace with actual id, for example 'anime_id:episode' format
        test_id = "tt1839578:1:1"  # This is an example ID format
        results = await cool(test_id, client)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_animeworld())

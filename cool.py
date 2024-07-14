import requests
import json
from info import get_info_tmdb,is_movie
from convert import get_TMDb_id_from_IMDb_id
from loadenv import load_env
_,MYSTERIUS_KEY = load_env()
def get_links(slug,season,episode,ismovie):
    try:
        headers = {
            "x-api-key": MYSTERIUS_KEY
        }
        response = requests.get("https://mammamia-urlo-ulala12431.hf.space/api/cookie", headers=headers)
        Auths = response.json()
        Bearer = Auths.get('cookie')
        ap_session = Auths.get('auth')

        cookies = {'ap_session': ap_session}

        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': f'Bearer {Bearer}',
            'referer': f'https://altadefinizione-originale.com/play/{slug}',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0',
            'x-requested-with': 'XMLHttpRequest',
        }
        if ismovie == 1:

            response = requests.get(f'https://altadefinizione-originale.com/api/post/urls/stream/{slug}',cookies=cookies,headers=headers)
        elif ismovie == 0:
            print("HERE SEASON",season)
            print("HERE EPISODE",episode)
            request_url =f'https://altadefinizione-originale.com/api/post/urls/stream/{slug}/{season}/{episode}'
            print(request_url)
            response = requests.get(request_url,cookies=cookies,headers=headers)
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

    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None
    

# Example usage: Fetch video links


# Print the dictionary





def search_imdb(showname,tmdba):
        tmdba = str(tmdba)
        query = f'https://altadefinizione-originale.com/api/search?search={showname}&page=1'
        response = requests.get(query)
        if response.status_code == 200:
            data = response.json()
            if 'data' in data:
                for item in data['data']:
                    if item.get('tmdb_id') == tmdba:
                        slug = item.get('slug')
                        print(slug)
                        return slug
                    


def parse_links(resolution_links):  
    results = {}      
    if resolution_links:
        print("Video links:")
        for resolution, link in resolution_links.items():
            print(f"{resolution}: {link}")
            results[resolution] = link
        return results    
    else:
        print("Failed to fetch video links")


def cool(imdb):
    try:
        type = "Cool"    
        general = is_movie(imdb)
        ismovie = general[0]
        imdb_id = general[1]
        if ismovie == 0 : 
            episode = int(general[2])
            season = int(general[3])
        
        if "tt" in imdb:
                #Get showname
            tmdba = get_TMDb_id_from_IMDb_id(imdb_id)
        else:
            tmdba = imdb_id.replace("tmdb:","")

        showname = get_info_tmdb(tmdba,ismovie,type)
        

        slug = search_imdb(showname,tmdba)
        print(ismovie)
        if ismovie == 1:
            season = None
            episode = None
            resolution_links = get_links(slug,episode,season,ismovie)
            results = parse_links(resolution_links)
            return results
        elif ismovie == 0:
            season = season -1
            episode = episode - 1
            resolution_links = get_links(slug,episode,season,ismovie)
            results = parse_links(resolution_links)
            return results
    except Exception as e:
        print("Cool Error")
        return None
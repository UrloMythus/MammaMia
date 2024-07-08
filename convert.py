import requests
from tmdbv3api import TMDb, Movie, TV
from loadenv import load_env
TMDB_KEY, DOMAIN = load_env()

def get_TMDb_id_from_IMDb_id(imdb_id):
    if ":" in imdb_id:
        season = imdb_id.split(":")[1]
        episode = imdb_id[-1]
        ismovie = 0
        imdb_id = imdb_id.split(":")[0]
    else:
        ismovie = 1
    response = requests.get(f'https://api.themoviedb.org/3/find/{imdb_id}', 
                            params={'external_source': 'imdb_id', 'api_key': f'{TMDB_KEY}'})
    tmbda = response.json()
    if tmbda['movie_results']:
        print(tmbda)
        return tmbda['movie_results'][0]['id'], ismovie
    elif tmbda['tv_results']:
        print(tmbda['tv_results'][0]['id'])
        return tmbda['tv_results'][0]['id'], season, episode , ismovie 
    else:
        return None
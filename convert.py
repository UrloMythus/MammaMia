import requests 
from tmdbv3api import TMDb, Movie, TV
from loadenv import load_env
import config
env_vars = load_env()

TMDB_KEY = env_vars.get('TMDB_KEY')
def get_TMDb_id_from_IMDb_id(imdb_id): 
    response = requests.get(f'https://api.themoviedb.org/3/find/{imdb_id}', 
                            params={'external_source': 'imdb_id', 'api_key': f'{TMDB_KEY}'})
    tmbda = response.json()
    if tmbda['movie_results']:
        return tmbda['movie_results'][0]['id']
    elif tmbda['tv_results']:
        return tmbda['tv_results'][0]['id']
    else:
        return None
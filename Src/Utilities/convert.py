from Src.Utilities.loadenv import load_env
env_vars = load_env()

TMDB_KEY = env_vars.get('TMDB_KEY')
async def get_TMDb_id_from_IMDb_id(imdb_id,client):
    response = await client.get(f'https://api.themoviedb.org/3/find/{imdb_id}', 
                            params={'external_source': 'imdb_id', 'api_key': f'{TMDB_KEY}'})
    tmbda = response.json()
    if tmbda['movie_results']:
        return tmbda['movie_results'][0]['id']
    elif tmbda['tv_results']:
        return tmbda['tv_results'][0]['id']
    else:
        return None
async def get_IMDB_id_from_TMDb_id(tmdb_id,client):
    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={TMDB_KEY}"
    response = await client.get(url)
    if response.status_code == 200:
        data = response.json()
        imdb_id = data.get('imdb_id')
        if imdb_id:
            return imdb_id




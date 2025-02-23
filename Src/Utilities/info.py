from Src.Utilities.loadenv import load_env
from tmdbv3api import TMDb, Movie, TV
from Src.Utilities.convert_date import convert_US_date, convert_IT_date
import Src.Utilities.config as config
import json
env_vars = load_env()
TMDB_KEY = env_vars.get('TMDB_KEY')


def get_info_tmdb(tmbda,ismovie,type):
    tmdb = TMDb()
    tmdb.api_key = f'{TMDB_KEY}'
    tmdb.language = 'it'
    if ismovie == 0:
        tv = TV()
        show= tv.details(tmbda)
        showname = show.name
        if type == "Filmpertutti":
            return showname
        elif type == "StreamingCommunity":
            full_date = show.first_air_date
            date = full_date.split("-")[0]
            return showname,date
        elif type == "StreamingCommunityFS":
                return showname
        elif type == "Tantifilm":
            date = show.first_air_date
            date = date.split("-")[0]
            return showname,date
        elif type == "TantifilmFS":
            return showname
        elif type == "Cool":
            return showname
        elif type == "LordChannel":
            date = show.first_air_date
            date = date.split("-")[0]
            return showname,date
        elif type == "StreamingWatch":
            date = show.first_air_date
            date = date.split("-")[0]
            return showname,date
        elif type == "DDLStream":
            return showname
        elif type == "Cb01":
            date = show.first_air_date
            date = date.split("-")[0]
            return showname,date
        elif type == "Whvx":
            date = show.first_air_date
            date = date.split("-")[0]
            return showname,date
    
    elif ismovie == 1:
        movie = Movie()
        show= movie.details(tmbda)
        showname= show.title
        #Get all release dates
        if type == "Filmpertutti":
            return showname
        elif type == "StreamingCommunity":
            date = show.release_date
            date = date.split("-")[0]
            return showname,date
        elif type == "StreamingCommunityFS":
            return showname
        elif type == "Tantifilm":
            date = show.release_date
            date = date.split("-")[0]
            return showname,date
        elif type == "TantifilmFS":
                return showname
        elif type == "Cool":
            return showname
        elif type == "LordChannel":
            date = show.release_date
            date = date.split("-")[0]
            return showname,date
        elif type == "StreamingWatch":
            date = show.release_date
            date = date.split("-")[0]
            return showname,date
        elif type == "DDLStream":
            return showname
        elif type == "Cb01":
            date = show.release_date
            date = date.split("-")[0]
            return showname,date
        elif type == "Whvx":
            date = show.release_date
            date = date.split("-")[0]
            return showname,date

async def get_info_imdb(imdb_id, ismovie, type,client):
    resp = await client.get(f'https://api.themoviedb.org/3/find/{imdb_id}?api_key={TMDB_KEY}&language=it&external_source=imdb_id')
    data = resp.json()
    if ismovie == 0:
        showname = data['tv_results'][0]['name']
        if type == "Filmpertutti":
            return showname
        elif type == "StreamingCommunity":
            date = data['tv_results'][0]['first_air_date']
            date = date.split("-")[0]
            return showname,date
        elif type == "StreamingCommunityFS":
            return showname
        elif type == "Tantifilm":
            date = data['tv_results'][0]['first_air_date']
            date = date.split("-")[0]
            return showname,date
        elif type == "TantifilmFS":
                return showname
        elif type == "Cool":
            return showname
        elif type == "DDLStream":
            return showname
        elif type == "Cb01":
            date = data['tv_results'][0]['first_air_date']
            date = date.split("-")[0]
            return showname,date
        elif type == "Whvx":
            date = data['tv_results'][0]['first_air_date']
            date = date.split("-")[0]
            return showname,date
        elif type == "Onlineserietv":
            date = data['tv_results'][0]['first_air_date']
            date = date.split("-")[0]
            return showname,date

    elif ismovie == 1:
        showname= data['movie_results'][0]['title']
        if type == "Filmpertutti":
            return showname
        elif type == "StreamingCommunity":
            date = data['movie_results'][0]['release_date']
            date = date.split("-")[0]
            return showname,date
        elif type == "StreamingCommunityFS":
            return showname
        elif type == "Tantifilm":
            date = data['movie_results'][0]['release_date']
            date = date.split("-")[0]
            return showname,date
        elif type == "Cool":
            return showname
        elif type == "DDLStream":
            return showname
        elif type == "Cb01":
            date = data['movie_results'][0]['release_date']
            date = date.split("-")[0]
            return showname,date
        elif type == "Whvx":
            date = data['movie_results'][0]['release_date']
            date = date.split("-")[0]
            return showname,date
        elif type == "Onlineserietv":
            date = data['movie_results'][0]['release_date']
            date = date.split("-")[0]
            return showname,date


async def get_info_kitsu(kitsu_id,client):
    api_url = f'https://kitsu.io/api/edge/anime/{kitsu_id}'
    response = await client.get(api_url)
    data = json.loads(response.text)
    try:
        showname = data['data']['attributes']['titles']['en']
    except Exception as e:
        showname = data['data']['attributes']['canonicalTitle']
    date = data['data']['attributes']['startDate']
    return showname,date           




async def is_movie(imdb_id):
    if "tmdb:" in imdb_id:
        imdb_id = imdb_id.replace("tmdb:","")
    if ":"  in imdb_id:
        season = imdb_id.split(":")[1]
        episode = imdb_id.split(":")[-1]
        ismovie = 0
        imdb_id = imdb_id.split(":")[0]
        return ismovie,imdb_id,season,episode
    else:
        ismovie = 1
        return ismovie,imdb_id

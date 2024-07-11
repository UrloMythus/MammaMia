from loadenv import load_env
from tmdbv3api import TMDb, Movie, TV
from convert_date import convert_US_date, convert_IT_date
import requests
import config
SC_FAST_SEARCH = config.SC_FAST_SEARCH
TMDB_KEY= load_env()

def get_info_tmdb(tmbda,ismovie,type):
    tmdb = TMDb()
    tmdb.api_key = f'{TMDB_KEY}'
    tmdb.language = 'it'
    if ismovie == 0:
        tv = TV()
        show= tv.details(tmbda)
        showname = show.name
        if type == "Filmpertutti":
            date= show.first_air_date
            print("Real date",date)
            return showname,date
        elif type == "StreamingCommunity":
            if SC_FAST_SEARCH == "0":
                n_season = show.number_of_seasons
                return showname,n_season
            
    else:
        movie = Movie()
        show= movie.details(tmbda)
        showname= show.title
        #Get all release dates
        date = show.release_dates
        if type == "Filmpertutti":
            #GET US RELEASE DATE because filmpertutti somewhy uses US release date
            date = convert_US_date(date)
    return showname,date




def get_info_imdb(imdb_id, ismovie, type):

    resp = requests.get(f'https://api.themoviedb.org/3/find/{imdb_id}?api_key={TMDB_KEY}&language=it&external_source=imdb_id')
    data = resp.json()
    if ismovie == 0:     
        showname = data['tv_results'][0]['name']
        if type == "Filmpertutti":
            date= data['tv_results'][0]['first_air_date']
            print("Real date",date)
            return showname, date
        elif type == "StreamingCommunity":
            return showname

    elif ismovie == 1:
        showname= data['movie_results'][0]['title']
        if type == "Filmpertutti":
            return
        elif type == "StreamingCommunity":
            return showname
            




def is_movie(imdb_id):
    if "tmdb:" in imdb_id:
        imdb_id = imdb_id.replace("tmdb:","")
    if ":"  in imdb_id:
        season = imdb_id.split(":")[1]
        episode = imdb_id[-1]
        ismovie = 0
        imdb_id = imdb_id.split(":")[0]
        return ismovie,imdb_id,season,episode
    else:
        ismovie = 1
        return ismovie,imdb_id
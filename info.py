from loadenv import load_env
from tmdbv3api import TMDb, Movie, TV
from convert_date import convert_US_date, convert_IT_date
TMDB_KEY= load_env()

def get_info(tmbda,ismovie,type):
    tmdb = TMDb()
    tmdb.api_key = f'{TMDB_KEY}'
    tmdb.language = 'it'
    if ismovie == 0:
        tv = TV()
        show= tv.details(tmbda)
        showname = show.name
        if type == "Filmpertutti":
            date= show.first_air_date
        elif type == "StreamingCommunity":
            date = show.last_air_date
            print("Real date",date)
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
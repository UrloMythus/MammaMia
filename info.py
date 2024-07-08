from loadenv import load_env
from tmdbv3api import TMDb, Movie, TV
from US_date import convert_US_date
TMDB_KEY, DOMAIN = load_env()

def get_info(tmbda,ismovie):
    tmdb = TMDb()
    tmdb.api_key = f'{TMDB_KEY}'
    tmdb.language = 'it'
    if ismovie == 0:
        tv = TV()
        show= tv.details(tmbda)
        showname = show.name
        date= show.first_air_date
    else:
        movie = Movie()
        show= movie.details(tmbda)
        showname= show.title
        #Get all release dates
        date = show.release_dates
        #GET US RELEASE DATE because filmpertutti somewhy uses US release date
        date = convert_US_date(date)
    if ismovie==0:
        return showname,date
    else:
        return showname,date
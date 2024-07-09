import os
from dotenv import load_dotenv
load_dotenv(".env")
def load_env():
    TMDB_KEY = os.getenv('TMDB_KEY')
    FT_DOMAIN = os.getenv('FT_DOMAIN')
    SC_DOMAIN= os.getenv('SC_DOMAIN')
    FILMPERTUTTI = os.getenv('FILMPERTUTTI')
    STREAMINGCOMMUNITY = os.getenv('STREAMINGCOMMUNITY')
    return TMDB_KEY, FT_DOMAIN, SC_DOMAIN, FILMPERTUTTI, STREAMINGCOMMUNITY
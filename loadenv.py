import os
from dotenv import load_dotenv
load_dotenv(".env")
def load_env():
    TMDB_KEY = os.getenv('TMDB_KEY')
    DOMAIN = os.getenv('DOMAIN')
    FILMPERTUTTI = os.getenv('FILMPERTUTTI')
    STREAMINGCOMMUNITY = os.getenv('STREAMINGCOMMUNITY')
    return TMDB_KEY, DOMAIN, FILMPERTUTTI, STREAMINGCOMMUNITY
import os
from dotenv import load_dotenv
load_dotenv(".env")
def load_env():
    TMDB_KEY = os.getenv('TMDB_KEY')
    DOMAIN = os.getenv('DOMAIN')
    return TMDB_KEY, DOMAIN
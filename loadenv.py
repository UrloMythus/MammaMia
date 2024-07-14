import os
import config
import config
MYSTERIUS = config.MYSTERIUS  
dotenv = config.dotenv
#You need to keep dotenv disabled on remote servers
if dotenv == "1":
    from dotenv import load_dotenv
    load_dotenv(".env")


def load_env():
    TMDB_KEY = os.getenv('TMDB_KEY')
    if MYSTERIUS == "1":
        MYSTERIUS_KEY = os.getenv('MYSTERIUS_KEY')
        return TMDB_KEY, MYSTERIUS_KEY
    return TMDB_KEY
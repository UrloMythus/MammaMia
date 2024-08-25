import os
import config
import config
MYSTERIUS = config.MYSTERIUS  
dotenv = config.dotenv
TUTTIFILM = config.TUTTIFILM
HF = config.HF
#You need to keep dotenv disabled on remote servers
if dotenv == "1":
    from dotenv import load_dotenv
    load_dotenv(".env")


def load_env():
    env_vars = {}
    env_vars['TMDB_KEY'] = os.getenv('TMDB_KEY')
    if MYSTERIUS == "1":
        env_vars['MYSTERIUS_KEY'] = os.getenv('MYSTERIUS_KEY')
    if TUTTIFILM == "1":
        if HF == "1":
            env_vars['PROXY_CREDENTIALS'] = os.getenv('PROXY')
    return env_vars

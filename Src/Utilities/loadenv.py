import os
import Src.Utilities.config as config
MYSTERIUS = config.MYSTERIUS  
dotenv_var = config.dotenv_var
Public_Instance = config.Public_Instance
# Carica sempre .env all'avvio
from dotenv import load_dotenv
load_dotenv(".env")

def load_env():
    env_vars = {}
    env_vars['TMDB_KEY'] = os.getenv('TMDB_KEY')
    if MYSTERIUS == "1":
        env_vars['MYSTERIUS_KEY'] = os.getenv('MYSTERIUS_KEY')
    env_vars['PROXY_CREDENTIALS'] = os.getenv('PROXY')
    if Public_Instance == "1":
        env_vars['ALTERNATIVE_LINK'] = os.getenv('ALTERNATIVE_LINK')
    env_vars['ForwardProxy'] = os.getenv('FORWARDPROXY')
    return env_vars

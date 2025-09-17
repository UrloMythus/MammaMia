import os
import Src.Utilities.config as config
dotenv = config.dotenv
#You need to keep dotenv disabled on remote servers
if dotenv == "1":
    from dotenv import load_dotenv
    load_dotenv(".env")


def load_env():
    env_vars = {}
    env_vars['TMDB_KEY'] = os.getenv('TMDB_KEY')
    env_vars['PROXY_CREDENTIALS'] = os.getenv('PROXY')
    env_vars['ForwardProxy'] = os.getenv('FORWARDPROXY')
    env_vars['PORT_ENV'] = os.getenv('PORT')
    return env_vars

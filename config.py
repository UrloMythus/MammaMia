#LOAD THE CONFIG
import json

# Open the configuration file
with open('config.json') as f:
    # Load JSON data from file
    config = json.load(f)

# Accessing SC_DOMAIN
SITE = config["Siti"]
FT_DOMAIN = SITE["Filmpertutti"]['domain']
SC_DOMAIN = SITE["StreamingCommunity"]['domain']
TF_DOMAIN = SITE["Tuttifilm"]['enabled']
FILMPERTUTTI = SITE["Filmpertutti"]['enabled']
STREAMINGCOMMUNITY = SITE["StreamingCommunity"]['enabled']
SC_FAST_SEARCH = SITE["StreamingCommunity"]['fast_search']
TF_FAST_SEARCH = SITE["Tuttifilm"]['fast_search']
#General
GENERAL = config['General']
dotenv = GENERAL["load_env"]
HOST = GENERAL["HOST"]
PORT = GENERAL["PORT"]
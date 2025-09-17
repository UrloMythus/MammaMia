#LOAD THE CONFIG
import json
import logging
# Open the configuration file
with open('config.json') as f:
    # Load JSON data from file
    config = json.load(f)

# Accessing SC_DOMAIN
SITE = config["Siti"]
SC_DOMAIN = SITE["StreamingCommunity"]['url']
SW_DOMAIN = SITE["StreamingWatch"]['url']
AW_DOMAIN = SITE['AnimeWorld']['url']
CB_DOMAIN = SITE['CB01']['url']
GS_DOMAIN = SITE['Guardaserie']['url']
GHD_DOMAIN = SITE['GuardaHD']['url']
ES_DOMAIN = SITE['Eurostreaming']['url']
GF_DOMAIN = SITE['Guardaflix']['url']
GO_DOMAIN = SITE['Guardoserie']['url']
SC = SITE['StreamingCommunity']['enabled']
SW = SITE['StreamingWatch']['enabled']
AW = SITE['AnimeWorld']['enabled']
CB = SITE['CB01']['enabled']
GS = SITE['Guardaserie']['enabled']
GHD = SITE['GuardaHD']['enabled']
ES= SITE['Eurostreaming']['enabled']
GF = SITE['Guardaflix']['enabled']
GO = SITE['Guardoserie']['enabled']
SC_ForwardProxy = SITE['StreamingCommunity']["SC_ForwardProxy"]
GS_ForwardProxy = SITE['Guardaserie']["GS_ForwardProxy"]
GH_ForwardProxy = SITE['GuardaHD']["GH_ForwardProxy"]
VX_ForwardProxy = SITE['StreamingCommunity']["VX_ForwardProxy"]
AW_ForwardProxy = SITE['AnimeWorld']["AW_ForwardProxy"]
MX_ForwardProxy = SITE['CB01']["MX_ForwardProxy"]
CB_ForwardProxy = SITE['CB01']["CB_ForwardProxy"]
ES_ForwardProxy = SITE['Eurostreaming']['ES_ForwardProxy']
GF_ForwardProxy = SITE['Guardaflix']['GF_ForwardProxy']
GO_ForwardProxy = SITE['Guardoserie']['GO_ForwardProxy']
SW_ForwardProxy = SITE['StreamingWatch']['SW_ForwardProxy']
GS_PROXY = SITE['Guardaserie']["GS_PROXY"]
GH_PROXY = SITE['GuardaHD']["GH_PROXY"]
CB_PROXY = SITE['CB01']["CB_PROXY"]
SC_PROXY = SITE['StreamingCommunity']["SC_PROXY"]
VX_PROXY = SITE['StreamingCommunity']["VX_PROXY"]
AW_PROXY = SITE['AnimeWorld']["AW_PROXY"]
MX_PROXY = SITE['CB01']["MX_PROXY"]
ES_PROXY = SITE['Eurostreaming']['ES_PROXY']
GF_PROXY = SITE['Guardaflix']['GF_PROXY']
GO_PROXY = SITE['Guardoserie']['GO_PROXY']
SW_PROXY = SITE['StreamingWatch']['SW_PROXY']
#General
GENERAL = config['General']
dotenv = GENERAL["load_env"]
HOST = GENERAL["HOST"]
PORT = GENERAL["PORT"]
Icon = GENERAL["Icon"]
Name = GENERAL["Name"]
LEVEL = GENERAL["level"]
Global_Proxy =  GENERAL["Global_Proxy"]

def setup_logging(LEVEL):
    LEVEL = LEVEL.upper()
    level = getattr(logging, LEVEL, logging.DEBUG) 
    logging.basicConfig(level=level,format='%(message)s')
    logger = logging.getLogger(__name__)
    return logger
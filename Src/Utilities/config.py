#LOAD THE CONFIG
import os
from typing import Optional

def get_env_bool(key: str, default: str = "0") -> str:
    """Get environment variable as string, defaulting to "0" for disabled"""
    return os.getenv(key, default)

def get_env_str(key: str, default: str = "") -> str:
    """Get environment variable as string"""
    return os.getenv(key, default)

def get_env_int(key: str, default: int = 0) -> int:
    """Get environment variable as integer"""
    try:
        return int(os.getenv(key, str(default)))
    except ValueError:
        return default

# Site URLs
FT_DOMAIN = get_env_str("FT_URL", "https://filmpertutti.motorcycles")
SC_DOMAIN = get_env_str("SC_URL", "https://streamingunity.bio")
TF_DOMAIN = get_env_str("TF_URL", "https://www.tanti.bond")
LC_DOMAIN = get_env_str("LC_URL", "https://lordchannel.net")
SW_DOMAIN = get_env_str("SW_URL", "https://www.streamingwatch.org")
AW_DOMAIN = get_env_str("AW_URL", "https://www.animeworld.so")
SKY_DOMAIN = get_env_str("SKY_URL", "https://skystreaming.watch")
CB_DOMAIN = get_env_str("CB_URL", "https://cb01net.life")
DDL_DOMAIN = get_env_str("DDL_URL", "https://ddlstreamitaly.co")
DLHD_DOMAIN = get_env_str("DLHD_URL", "https://daddylive.mp")
GS_DOMAIN = get_env_str("GS_URL", "https://guardaserietv.cc")
GHD_DOMAIN = get_env_str("GHD_URL", "https://mostraguarda.stream")
OST_DOMAIN = get_env_str("OST_DOMAIN", "com")

# Site enabled flags
SC = get_env_bool("SC_ENABLED", "1")
FT = get_env_bool("FT_ENABLED", "1")
TF = get_env_bool("TF_ENABLED", "1")
LC = get_env_bool("LC_ENABLED", "1")
SW = get_env_bool("SW_ENABLED", "1")
AW = get_env_bool("AW_ENABLED", "1")
SKY = get_env_bool("SKY_ENABLED", "1")
CB = get_env_bool("CB_ENABLED", "1")
DDL = get_env_bool("DDL_ENABLED", "1")
MYSTERIUS = get_env_bool("MYSTERIUS_ENABLED", "0")
GS = get_env_bool("GS_ENABLED", "1")
GHD = get_env_bool("GHD_ENABLED", "1")
OST = get_env_bool("OST_ENABLED", "1")
DLHD = get_env_bool("DLHD_ENABLED", "1")

# Proxy configurations
TF_ForwardProxy = get_env_bool("TF_FORWARD_PROXY", "0")
SC_ForwardProxy = get_env_bool("SC_FORWARD_PROXY", "0")
GS_ForwardProxy = get_env_bool("GS_FORWARD_PROXY", "0")
GH_ForwardProxy = get_env_bool("GHD_FORWARD_PROXY", "0")
VX_ForwardProxy = get_env_bool("VX_FORWARD_PROXY", "0")
AW_ForwardProxy = get_env_bool("AW_FORWARD_PROXY", "0")
MX_ForwardProxy = get_env_bool("MX_FORWARD_PROXY", "0")
CB_ForwardProxy = get_env_bool("CB_FORWARD_PROXY", "0")
OST_ForwardProxy = get_env_bool("OST_FORWARD_PROXY", "0")

GS_PROXY = get_env_bool("GS_PROXY", "0")
GH_PROXY = get_env_bool("GHD_PROXY", "0")
TF_PROXY = get_env_bool("TF_PROXY", "0")
CB_PROXY = get_env_bool("CB_PROXY", "0")
SC_PROXY = get_env_bool("SC_PROXY", "0")
VX_PROXY = get_env_bool("VX_PROXY", "0")
AW_PROXY = get_env_bool("AW_PROXY", "0")
MX_PROXY = get_env_bool("MX_PROXY", "0")
OST_PROXY = get_env_bool("OST_PROXY", "0")

# DDLStream cookies
ips4_device_key = get_env_str("DDL_IPS4_DEVICE_KEY")
ips4_IPSSessionFront = get_env_str("DDL_IPS4_IPSSESSIONFRONT")
ips4_member_id = get_env_str("DDL_IPS4_MEMBER_ID")
ips4_login_key = get_env_str("DDL_IPS4_LOGIN_KEY")

# General configurations
dotenv = get_env_bool("LOAD_ENV", "0")
HOST = get_env_str("HOST", "0.0.0.0")
PORT = get_env_int("PORT", 8080)
Icon = get_env_str("ICON", "Pizza")
Name = get_env_str("NAME", "MammaMia")
Public_Instance = get_env_bool("PUBLIC_INSTANCE", "0")
Remote_Instance = get_env_bool("REMOTE_INSTANCE", "1")
Global_Proxy = get_env_bool("GLOBAL_PROXY", "0")

import requests
from Crypto.Cipher import AES
import json
import re
from rich.prompt import Prompt
from rich.console import Console
from fake_headers import Headers
import  Src.Utilities.config as config
import logging
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)
Icon = config.Icon
Name = config.Name
'''
This script was done mostly by @Arrowar, creator of https://github.com/Arrowar/StreamingCommunity/
It was modified for the use in MammaMia
'''


random_headers = Headers()

KEY = b'kiemtienmua911ca'          # 16 byte
IV = b'1234567890oiuytr'           # 16 byte


async def fetch_response(client,referer,player_url,url,id, proxies, ForwardProxy):
    headers = random_headers.generate()
    headers['referer'] = player_url
    data = {
    'id': id,
    'w': '2560',
    'h': '1440',
    'r': referer,
    }
    response =  await client.get(ForwardProxy + url, headers=headers, params = data, proxies = proxies)
    return response.text

def hex_to_bytes(hex_str):
    hex_str = re.sub(r'[^0-9a-fA-F]', '', hex_str)

    if len(hex_str) % 2 != 0:
        hex_str = '0' + hex_str

    return bytes(int(hex_str[i:i+2], 16) for i in range(0, len(hex_str), 2))

def decrypt_aes_cbc(ciphertext_bytes, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext_bytes)

    pad_len = decrypted[-1]
    if 1 <= pad_len <= 16:
        decrypted = decrypted[:-pad_len]
        
    return decrypted



async def loadm(player_link,client,streams,referer,site_name,proxies,ForwardProxy):
    parts = player_link.split('#')
    id = parts[1]
    player_url = parts[0]
    api = player_url + 'api/v1/video'
    #It downloads m (crypted informations) from the API"
    response_hex = await fetch_response(client,referer,player_url,api,id, proxies, ForwardProxy)
    #Convert Hex in Bytes
    ciphertext_bytes = hex_to_bytes(response_hex)
    #We decrypt AES-CBC encryption with Key,IV and the bytes
    decrypted_bytes = decrypt_aes_cbc(ciphertext_bytes, KEY, IV)
    decrypted_str = decrypted_bytes.decode('utf-8')
    data = json.loads(decrypted_str)
    #We get the hls
    hls = data['cf']
    title = data['title']
    if hls:
        streams['streams'].append({'name': f"{Name}",'title': f'{Icon}{site_name}\n▶️ Loadm\n{title}', 'url': hls, 'behaviorHints': {'proxyHeaders': {"request": {"Referer": player_url}}, 'notWebReady': True, 'bingeGroup': f'{site_name.lower()}'}})
        logger.info(f"{site_name} on Loadm found results for the current ID")
        return streams





#Testing
async def test_loadm():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        results = await loadm("https://loadm.cam/#6wx1p",client,{'streams': []},'guardoserie.live', 'Guardoserie', {},"")
        print(results)
if __name__ == "__main__":
    import asyncio
    asyncio.run(test_loadm()) 

# https://loadm.cam/#cfnqx
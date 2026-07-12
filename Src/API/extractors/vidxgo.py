


import  Src.Utilities.config as config
Icon = config.Icon
Name = config.Name
import re
from fake_headers import Headers
random_headers = Headers()
import logging
from Src.Utilities.config import setup_logging
from base64 import b64encode,b64decode
level = config.LEVEL
logger = setup_logging(level)
import base64
from bs4 import BeautifulSoup,SoupStrainer
VD_DOMAIN = config.VD_DOMAIN
from curl_cffi.requests import AsyncSession
import json
VD_PROXY = config.VD_PROXY
proxies = {}
if VD_PROXY == "1":
    PROXY_CREDENTIALS = env_vars.get('PROXY_CREDENTIALS')
    proxy_list = json.loads(PROXY_CREDENTIALS)
    proxy = random.choice(proxy_list)
    if proxy == "":
        proxies = {}
    else:
        proxies = {
            "http": proxy,
            "https": proxy
        }   
VD_ForwardProxy = config.VD_ForwardProxy
if VD_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
else:
    ForwardProxy = ""
VD_DOMAIN = config.VD_DOMAIN

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:150.0) Gecko/20100101 Firefox/150.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Sec-GPC': '1',
    'Alt-Used': 'v.vidxgo.co',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'DNT': '1',
    'Referer': 'https://altadefinizione.you/',
    'Sec-Fetch-Storage-Access': 'none',
    '-': '-',
    'Priority': 'u=0, i',
}

headers2 = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:150.0) Gecko/20100101 Firefox/150.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://v.vidxgo.co/tt34437972',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'DNT': '1',
    'Priority': 'u=4',
}
async def vidxgo_refresh(link,id):
    async with AsyncSession() as client:
        headers['Referer'] = f'{VD_DOMAIN}/t/{id}'
        response = await client.get(ForwardProxy + f'{VD_DOMAIN}/t/{id}', allow_redirects=True, headers = headers2, proxies = proxies)
        return response.json()['url'].replace('\\','')

async def vidxgo(link,client,streams,instance_url):
    #headers = random_headers.generate()
    response = await client.get(ForwardProxy + link, allow_redirects=True, headers = headers, proxies = proxies)
    soup = BeautifulSoup(response.text,'lxml',parse_only=SoupStrainer('script'))
    scripts = soup.find_all('script')
    text = [item for item in scripts if len(item.text) > 3000]
    match = re.search(r"var .+'(.*)',d=atob\('(.*)'",text[0].text)
    if match:
        key = match.group(1)
        base64_text = match.group(2)
        decoded = base64.b64decode(base64_text)
        u = bytearray(len(decoded))
        for i in range(len(decoded)):
            u[i] = decoded[i] ^ ord(key[i % len(key)])
        decrypted_code = u.decode('utf-8')
        match = re.search(r'currentSrc.+"(https:[^";]+)',decrypted_code)
        submatch = re.search(r'window.__EXTERNAL_SUBS\s+=\s+(\[.*]);',decrypted_code)
        suburlmatch = re.search(r'window.__SUBS_ORIGIN\s+=\s*"(.*)";',decrypted_code)
        if match:
            url = match.group(1).replace("\\","")
            subtitles = []
            if submatch and suburlmatch:
                subtitles = json.loads(submatch.group(1))
                for item in subtitles: 
                    if item['forced'] == True:
                        item['id'] = item['lang'] + '-forced'
                    else:
                        item['id'] = item['lang']
                    del item['forced']
                    del item['file']
                    item['url'] = suburlmatch.group(1).replace('\\','') + item['url']
            streams['streams'].append({'name': f"{Name}",'title': f'{Icon}Vidxgo\n ▶️ Vidxgo', 'url': f'{instance_url}/clone/manifest.m3u8?d={b64encode(url.encode("utf-8")).decode("utf-8")}',  'behaviorHints': {'proxyHeaders': {"request": {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',"Accept": "*/*", "Accept-Language":"en-US,en;q=0.9","Referer":VD_DOMAIN+"/","Origin":VD_DOMAIN,"Sec-GPC": "1","Connection": "keep-alive","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"cross-site","DNT": "1","Priority":"u=0"}}, 'notWebReady': True, 'bingeGroup': f'vidxgo'},'subtitles' : subtitles})
            logger.info(f"Vidxgo found results for the current ID")

    return streams

#Testing
async def test_vidxgo():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        results = await vidxgo("https://v.vidxgo.co/tt0816692",client,{'streams': []},"localhost")
        print(results)
if __name__ == "__main__":
    import asyncio
    asyncio.run(test_vidxgo()) 




# XOR decryption


import os
from bs4 import BeautifulSoup,SoupStrainer
import json
import logging
import  Src.Utilities.config as config
from Src.Utilities.config import setup_logging
from Src.Utilities.loadenv import load_env  

UT_PROXY = config.UT_PROXY
UT_ForwardProxy = config.UT_ForwardProxy
level = config.LEVEL
env_vars = load_env()
import random
logger = setup_logging(level)
#Set up proxies
proxies = {}
if UT_PROXY == "1":
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
if UT_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
else:
    ForwardProxy = ""

url = 'https://uprot.net/msf/r4hcq47tarq8'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:146.0) Gecko/20100101 Firefox/146.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': url.split('msf')[0],
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Referer': url,
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'DNT': '1',
    'Priority': 'u=0, i',
    }
async def get_uprot_numbers(client):
    try:
        response = await client.post(ForwardProxy + url, headers=headers, proxies = proxies)
        set_cookie = response.headers.get('set-cookie')
        parts = set_cookie.split(';')[0].split('=')
        key = parts[0]
        value = parts[1]
        cookies = {
            key:value
        }
        soup = BeautifulSoup(response.text,'lxml',parse_only=SoupStrainer('img'))
    
        img = soup.find('img')['src']
        return img,cookies
    except Exception as e:
        logger.info(f'Uprot failed  to generate numberers/cookies: {e}')
        return None,None
async def generate_uprot_txt(numbers,cookies,client):
    try:
        data = {
        'captcha': str(numbers),
        }
        response = await client.post(ForwardProxy + url, cookies=cookies, headers=headers, data=data, proxies = proxies)
        if response.status_code != 200:
            return False
        set_cookie = response.headers.get('set-cookie')
        parts = set_cookie.split(';')[0].split('=')
        key = parts[0]
        value = parts[1]
        cookies[key] = value
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, 'uprot.txt')
        with open(file_path,'w') as file:
            file.write(f'{str(cookies)}\n{str(data)}')
            return True
        return False
    except Exception as e:
        logger.info(f'Uprot failed  to generate captcha cookie: {e}')
        return False

async def get_maxstream_link(text,client):
    soup = BeautifulSoup(text,'lxml',parse_only=SoupStrainer('a'))
    a_tags = soup.find_all('a')

    max_stream = None
    for tag in a_tags:
        if 'C O N T I N U E' in tag.text.upper():
            max_stream = tag['href']
    if max_stream: 
        redirect = max_stream
        time = 0
        while 'uprots' in redirect:
            response = await client.head(ForwardProxy + max_stream,headers=headers,impersonate = 'chrome', allow_redirects = True, proxies = proxies)
            redirect = response.url
            time+=1
            if time == 1000:
                return False
        max_stream = 'https://maxstream.video/emvvv/' + response.url.split('watchfree/')[1].split('/')[1]
    return max_stream

async def bypass_uprot(client,link):
    try:
        if 'mse' in link:
            link = link.replace('mse','msf')
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, 'uprot.txt')
        with open(file_path,'r') as file:
            text = file.read()
            parts = text.split('\n')
            cookies = json.loads(parts[0].replace("'", '"'))
            data = json.loads(parts[1].replace("'", '"'))
        response = await client.post(ForwardProxy + link, cookies=cookies, headers=headers, data =data, impersonate = 'chrome', proxies = proxies)
        max_stream = await get_maxstream_link(response.text,client)
        return max_stream
    except Exception as e:
        logger.info(f'Uprot failed: {e}')
        if '[Errno 2] No such file or directory' in e:
            return None
        return False


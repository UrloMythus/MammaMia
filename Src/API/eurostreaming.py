from Src.Utilities.info import get_info_tmdb, is_movie, get_info_imdb
import Src.Utilities.config as config
from fake_headers import Headers  
from urllib.parse import quote
from Src.Utilities.loadenv import load_env  
import re
from bs4 import BeautifulSoup,SoupStrainer
env_vars = load_env()
from fake_headers import Headers  
random_headers = Headers()
try:
    import pytesseract
    from PIL import Image
except Exception as e:
    print("You can not use ES")

import base64
from io import BytesIO
import time
from Src.Utilities.eval import eval_solver
import os
import json
import difflib
import random
ES_DOMAIN = config.ES_DOMAIN

ES_PROXY = config.ES_PROXY
proxies = {}
if ES_PROXY == "1":
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
ES_ForwardProxy = config.ES_ForwardProxy
if ES_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
else:
    ForwardProxy = ""




'''
OK <a href="https://uprot.net/msf/fwbtgsssmt0q" target="_blank" rel="noopener">MaxStream</a> – <a href="https://clicka.cc/delta/6svqpze62r8z" target="_blank" rel="noopener">DeltaBit</a> – <a href="https://clicka.cc/tv/5eumjxxt" target="_blank" rel="noopener">Turbovid</a>
pattern = r'href="([^"]+)"'
match = re.search(pattern, text)
 href_value = match.group(1)
'''
async def mixdrop(url,MFP,client):
    """Extract Mixdrop URL."""
    if "club" in url:
        url = url.replace("club", "cv").split("/2")[0]
    if "cfd" in url:
        url = url.replace("cfd", "cv").replace("emb","e").split("/2")[0]
    if MFP == "1": 
        return url,""
    headers = {"accept-language": "en-US,en;q=0.5"}
    final_url = f"https:{await eval_solver(url, proxies , ForwardProxy, client)}"
    return final_url,""

async def deltabit(page_url,client):
    """Extract Deltabit URL."""
    i = 0
    #Set up some headers
    headers = random_headers.generate()
    headers2 = random_headers.generate()

    #Get the redirected link, so the actual deltabit link.
    page_url_response = await client.get(ForwardProxy + page_url,headers={**headers, 'Range': 'bytes=0-0'}, proxies=proxies)
    page_url = page_url_response.url
    print("Page_URl is",page_url)

    #Change the referer  and user agent of the generated headers
    headers2['referer'] = 'https://safego.cc/'
    headers2['user-agent'] =  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'

    #Request to the deltabit link
    response = await client.get(ForwardProxy + page_url, headers = headers2, allow_redirects = True, proxies = proxies)
    page_url = response.url

    #Often deltabit redirects to another deltabit link. We need the redirected link to put it in the headers.
    origin = page_url.split('/')[2]
    headers['origin'] = f'https://{origin}'
    headers['referer'] = page_url
    headers['user-agent'] =  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'

    #We check the page for the data such as hash and fname.
    soup = BeautifulSoup(response.text, 'lxml', parse_only=SoupStrainer('input'))
    data = {}
    for input in soup:
        name = input.get('name')
        value = input.get('value')
        data[name] = value 
    data['imhuman'] = ''
    data['referer']= page_url

    #We need to wait 2.5 seconds or the request will fail
    time.sleep(2.5)
    
    
    
    fname = data['fname']
    #Request to the deltabit link
    response = await client.post(ForwardProxy + page_url, data = data, headers = headers, proxies = proxies)
    link = re.findall(r'sources:\s*\["([^"]+)"', response.text, re.DOTALL)
    print(link)
    if not link:
        if not i >= 3:
            link,fname = await deltabit(page_url,client)
            i +=1
    else:
        link = link[0]
    
    
    return link,fname


def convert_numbers(base64_data):
    image_data = base64.b64decode(base64_data)
    image = Image.open(BytesIO(image_data))
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    number_string = pytesseract.image_to_string(image, config=custom_config)
    return number_string.strip()


async def get_numbers(safego_url,client):
    headers = random_headers.generate()
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:138.0) Gecko/20100101 Firefox/138.0'
    response = await client.get(ForwardProxy + safego_url,headers = headers, proxies = proxies)
    cookies = (response.cookies.get_dict())
    soup = BeautifulSoup(response.text,'lxml',parse_only=SoupStrainer('img'))
    numbers = soup.img['src'].split(',')[1]
    return numbers,cookies

async def real_page(safego_url,client):
    try:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, 'cookie.txt')
        headers = random_headers.generate()
        headers['Origin'] = 'https://safego.cc'
        headers['Referer'] = safego_url
        headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:138.0) Gecko/20100101 Firefox/138.0'
        with open(file_path, 'r') as file:
            cookies = file.read()
        cookies = json.loads(cookies.replace("'", '"'))
        response = await client.post(ForwardProxy + safego_url,headers=headers, cookies = cookies, proxies = proxies)
        soup = BeautifulSoup(response.text,'lxml', parse_only=SoupStrainer('a'))
        if len(soup)>= 1:
            return soup.a['href']
        else:
            print("Getting numbers")
            numbers,cookies = await get_numbers(safego_url,client)
            numbers = convert_numbers(numbers)
            data = {'captch4': numbers}
            response = await client.post(ForwardProxy + safego_url,headers=headers, data=data, cookies = cookies, proxies = proxies)
            cap4 = response.headers.get('set-cookie').split(';')[0]
            cookies[cap4.split('=')[0]] = cap4.split('=')[1]
            with open(file_path, 'w') as file:
                file.write(str(cookies))
            soup = BeautifulSoup(response.text,'lxml', parse_only=SoupStrainer('a'))
            return soup.a['href']
    except Exception as e:
        print(e)
async def get_host_link(pattern,atag,client):
    match = re.search(pattern, atag)
    headers = random_headers.generate()
    if match:
        href_value = match.group(1)
        response = await client.head(ForwardProxy + href_value, headers={**headers, 'Range': 'bytes=0-0'}, proxies = proxies)
        href_value = response.url
        href = await real_page(href_value,client)
        return href
async def scraping_links(atag,MFP,client):
    #Check which hosts are avaiable and extract the links from one of them. Turbovid uses Cloudflare therefore is not avaiable. Maxstream has a captcha. 
    if "MixDrop" and "DeltaBit" in atag:
        pattern = r'<a\s+href="([^"]+)"[^>]*rel="noopener"[^>]*>DeltaBit</a>'
        href = await get_host_link(pattern,atag,client)
        try:
            full_url,name = await deltabit(href,client)
        except Exception as e:
            pattern = r'<a\s+href="([^"]+)"[^>]*rel="noopener"[^>]*>MixDrop</a>'
            href = await get_host_link(pattern,atag,client)
            full_url,name = await mixdrop(href,MFP,client)
        return full_url,name
    if "MixDrop" in atag and  "DeltaBit" not in atag:
        pattern = r'<a\s+href="([^"]+)"[^>]*rel="noopener"[^>]*>MixDrop</a>'
        href = await get_host_link(pattern,atag,client)
        full_url,name = await mixdrop(href,MFP,client)
        return full_url,name
    if 'DeltaBit' in atag and "MixDrop" not in atag:
        pattern = r'<a\s+href="([^"]+)"[^>]*rel="noopener"[^>]*>DeltaBit</a>'
        href = await get_host_link(pattern,atag,client)
        full_url,name = await deltabit(href,client)
        return full_url,name
    if 'DeltaBit' not in atag and 'MixDrop' not in atag:
        print("Just give up")
        return None,""

async def episodes_find(description,season,episode,MFP,client):
    episode = episode.zfill(2)
    pattern = rf'{season}&#215;{episode}\s*(.*?)(?=<br\s*/?>)'
    match = re.findall(pattern, description)
    urls= {}
    if match:
        for episode_details in match:
            if "href" in episode_details:
                full_url,name = await scraping_links(episode_details.split(' – ', 1)[1],MFP,client)
                if full_url:
                    urls[full_url] = name
        return urls
async def search(showname,date,season,episode,MFP,client):
    headers = random_headers.generate()

    response = await client.get(ForwardProxy + f"{ES_DOMAIN}/wp-json/wp/v2/search?search={quote(showname)}&_fields=id", proxies = proxies, headers = headers)
    results = response.json()
    for i in results:
        response = await client.get(ForwardProxy + f"{ES_DOMAIN}/wp-json/wp/v2/posts/{i['id']}?_fields=content,title", proxies = proxies, headers = headers)
        if f'ID articolo non valido' in response.text:
            continue
        description = response.json()
        title = description['title']['rendered']
        description = description['content']['rendered']
        ratio = difflib.SequenceMatcher(None, title, showname).ratio()
        if ratio >=0.96:
            urls = await episodes_find(description,season,episode,MFP,client)
            return urls
        else:
            year_pattern = re.compile(r'(?<!/)(19|20)\d{2}(?!/)')
            match = year_pattern.search(description)
            if match:
                year = match.group(0)

            else:
                pattern = r'<a\s+href="([^"]+)"[^>]*>Continua a leggere</a>'
                match = re.search(pattern, description)
                if match:
                    href_value = match.group(1)
                    response_2 = await client.get(ForwardProxy + href_value, proxies = proxies, headers = headers)
                    match = year_pattern.search(response_2.text)
                    if match:
                        year = match.group(0)
            if abs(int(year) - int(date)) <=1:
                urls = await episodes_find(description,season,episode,MFP,client)
                return urls




async def eurostreaming(id,client,MFP):
    try:
        general = await is_movie(id)
        ismovie = general[0]
        clean_id = general[1]
        type = "Eurostreaming"
        if ismovie == 0 : 
            season = str(general[2])
            episode = str(general[3])
        elif ismovie == 1:
            return None
        if "tmdb" in id:
            showname,date = get_info_tmdb(clean_id,ismovie,type)
        else:
            showname,date = await get_info_imdb(clean_id,ismovie,type,client)
        print(showname)
        urls = await search(showname,date, season,episode,MFP,client)
        return urls
    except Exception as e:
        print(e)




async def test_euro():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        results = await eurostreaming("tt2261391:6:1",client,0)
        print(results)

async def test_deltabit():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        results = await deltabit("https://deltabit.co/fgeki2456ab1",client)
        print(results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_euro())  
    #python3 -m Src.API.eurostreaming

'''tt11950864
'''

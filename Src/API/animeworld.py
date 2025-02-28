
from bs4 import BeautifulSoup
import datetime
import json
from Src.Utilities.info import get_info_kitsu
import Src.Utilities.config as config
import re
from fake_headers import Headers  
random_headers = Headers()
proxies = {}
from Src.Utilities.loadenv import load_env  
env_vars = load_env()
AW_PROXY = config.AW_PROXY
AW_ForwardProxy = config.AW_ForwardProxy
if AW_PROXY == "1":
    import random
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
if AW_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
else:
    ForwardProxy = ""        


AW_DOMAIN = config.AW_DOMAIN
months = {
        "Gennaio": "January", "Febbraio": "February", "Marzo": "March", 
        "Aprile": "April", "Maggio": "May", "Giugno": "June", 
        "Luglio": "July", "Agosto": "August", "Settembre": "September", 
        "Ottobre": "October", "Novembre": "November", "Dicembre": "December"
    }
showname_replace = {
    "Attack on Titan": "L'attacco dei Giganti",
    "Season": "",
    "  ": " ",
    "Shippuuden": "Shippuden",
    " ": "+",
    "Solo+Leveling+2": "Solo+Leveling+2:",
    "-": ""
}
async def security_cookie (response):
    match = re.search(r'SecurityAW-([A-Za-z0-9]{2})=([^;]+)', response.text)
    if match:
        unknown_chars = match.group(1).strip()
        Security_Cookie = match.group(2).strip()
        cookies = {
            f"SecurityAW-{unknown_chars}": Security_Cookie
        }
        return cookies
async def get_mp4(anime_url,ismovie,episode,client):
    cookies = {}
    if ForwardProxy != "":
        response = await client.get(ForwardProxy + anime_url,allow_redirects=True,impersonate = "chrome124",proxies=proxies)
        anime_url = f'{AW_DOMAIN}/{response.url.replace(ForwardProxy,"")}?d=1'
        response = await client.get(ForwardProxy + anime_url, allow_redirects=True,  cookies = cookies,impersonate = "chrome124",proxies=proxies)
        cookies = await security_cookie(response)
        response = await client.get(ForwardProxy + anime_url, allow_redirects=True,  cookies = cookies,impersonate = "chrome124",proxies=proxies)
    else:
        response = await client.get(ForwardProxy + anime_url, allow_redirects=True,  cookies = cookies,impersonate = "chrome124",proxies=proxies)
    soup = BeautifulSoup(response.text,'lxml')
    if ismovie == 0:
        episode_page = soup.find('a', {'data-episode-num':episode })
        if episode_page is None:
            return None
        episode_page = f'{AW_DOMAIN}{episode_page["href"]}'
        response = await client.get(ForwardProxy + episode_page,allow_redirects=True, cookies = cookies,impersonate = "chrome124", proxies=proxies)
        if response.status_code == 202:
            cookies = await security_cookie(response)
            response = await client.get(ForwardProxy + episode_page,allow_redirects=True, cookies = cookies,impersonate = "chrome124", proxies=proxies)
        soup = BeautifulSoup(response.text,'lxml')

    a_tag  = soup.find('a', {'id': 'alternativeDownloadLink', 'class': 'm-1 btn btn-sm btn-primary'}) 
    url = a_tag['href']
    response = await client.head(url)
    if response.status_code == 404:
        url = None
    return url




async def search(showname,date,ismovie,episode,client):
    search_year = date[:4] 
    headers = random_headers.generate()
    link = f'{AW_DOMAIN}/filter?year={search_year}&sort=2&keyword={showname}'
    response = await client.get(ForwardProxy + link,allow_redirects=True, impersonate = "chrome124", headers = headers, proxies = proxies)
    if response.status_code == 202:
        cookies = await security_cookie(response)
        response = await client.get(ForwardProxy + link,allow_redirects=True, impersonate = "chrome124", proxies = proxies, headers = headers, cookies = cookies)
    else:
        cookies = {}
    soup = BeautifulSoup(response.text,'lxml')
    anime_list = soup.find_all('a', class_=['poster', 'tooltipstered'])
    final_urls = []
    for anime in anime_list:
        anime_info_url = f'{AW_DOMAIN}/{anime["data-tip"]}'
        response = await client.get(ForwardProxy + anime_info_url,allow_redirects=True, impersonate = "chrome124", cookies = cookies, proxies = proxies)
        if response.status_code == 202:
            cookies = await security_cookie(response)
            response = await client.get(ForwardProxy + anime_info_url,allow_redirects=True, impersonate = "chrome124", cookies = cookies, proxies = proxies)
        pattern = r'<label>Data di uscita:</label>\s*<span>\s*(.*?)\s*</span>'
        match = re.search(pattern, response.text, re.S)
        release_date = match.group(1).strip()
        for ita, eng in months.items():
            release_date = release_date.replace(ita, eng)
        release_date_object = datetime.datetime.strptime(release_date, "%d %B %Y")
        date_object = datetime.datetime.strptime(date, "%Y-%m-%d")
        release_date = release_date_object.strftime("%Y-%m-%d")
        if (release_date == date or 
    release_date == (datetime.datetime.strptime(date, "%Y-%m-%d") + datetime.timedelta(days=1)).strftime("%Y-%m-%d") or
    release_date == (datetime.datetime.strptime(date, "%Y-%m-%d") - datetime.timedelta(days=1)).strftime("%Y-%m-%d")):
            anime_url = f'{AW_DOMAIN}{anime["href"]}'
            final_url = await get_mp4(anime_url,ismovie,episode,client)
            if final_url:
                final_urls.append(final_url)
    return final_urls

async def animeworld(id,client):
    try:
        kitsu_id = id.split(":")[1]
        ismovie = 1 if len(id.split(":")) == 2 else 0
        if ismovie == 1:
            episode = None
        else:
            episode = id.split(":")[2]
        showname,date = await get_info_kitsu(kitsu_id,client)
        #Format Showname
        for key in showname_replace:
            if key in showname:  # Check if the key is a substring of showname
                showname = showname.replace(key, showname_replace[key])
                if "Naruto:" in showname:
                    showname = showname.replace(":", "")
                if  "’" in showname:
                    showname = showname.split("’")[0]
                if ":" in showname:
                    showname = showname.split(":")[0]
        final_urls = await search(showname,date,ismovie,episode,client)
        return final_urls
    except Exception as e:
        print("Animeworld failed",e)
        return None

async def test_animeworld():
    async with AsyncSession() as client:
        # Replace with actual id, for example 'anime_id:episode' format
        test_id = "kitsu:508:2"  # This is an example ID format
        results = await animeworld(test_id, client)
        print(results)

if __name__ == "__main__":
    from curl_cffi.requests import AsyncSession
    import asyncio
    asyncio.run(test_animeworld())













async def old_search(showname,date,ismovie,episode,client):
    cookies = {
    'sessionId': 's%3AtGSRfYcsIoaeV0nqFJgN69Zxixb_-uJU.fcNz%2FsJBiiP8v8TwthMN9%2FmynWFciI5gezZuz8CltyQ',
    }

    headers = {
        'authority': f'www.animeworld.{AW_DOMAIN}',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
         # 'content-length': '0',
         # 'cookie': 'sessionId=s%3AtGSRfYcsIoaeV0nqFJgN69Zxixb_-uJU.fcNz%2FsJBiiP8v8TwthMN9%2FmynWFciI5gezZuz8CltyQ',
         'csrf-token': 'oKFK43s4-BzfqPX27RlAORUd-iyiAfXyfDAo',
         'origin': f'https://www.animeworld.{AW_DOMAIN}',
         'referer': f'https://www.animeworld.{AW_DOMAIN}/',
         'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
         'sec-ch-ua-mobile': '?0',
         'sec-ch-ua-platform': '"Android"',
         'sec-fetch-dest': 'empty',
         'sec-fetch-mode': 'cors',
         'sec-fetch-site': 'same-origin',
         'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
         'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'keyword': showname,
    }

    response = await client.post(f'https://www.animeworld.{AW_DOMAIN}/api/search/v2', params=params, cookies=cookies, headers=headers,allow_redirects=True, impersonate = "chrome124")

    data = json.loads(response.text)
    final_urls = []
    for anime in data["animes"]:
        release_date = anime["release"]
        for ita, eng in months.items():
            release_date = release_date.replace(ita, eng)
        release_date = datetime.datetime.strptime(release_date, "%d %B %Y")
        release_date = release_date.strftime("%Y-%m-%d")
        if release_date == date:
            identifier = anime["identifier"]
            link = anime["link"]
            anime_url = f'https://animeworld.{AW_DOMAIN}/play/{link}.{identifier}'
            final_url = await get_mp4(anime_url,ismovie,episode,client)
            final_urls.append(final_url)
            break
    showname = showname + " (ITA)"
    params = {
        'keyword': showname,
    }
    response = await client.post(ForwardProxy + f'https://www.animeworld.{AW_DOMAIN}/api/search/v2', params=params, cookies=cookies, headers=headers, allow_redirects=True, impersonate = "chrome124", proxies = proxies)
    data = json.loads(response.text)
    for anime in data["animes"]:
        release_date = anime["release"]
        for ita, eng in months.items():
            release_date = release_date.replace(ita, eng)
        release_date = datetime.datetime.strptime(release_date, "%d %B %Y")
        release_date = release_date.strftime("%Y-%m-%d")
        if release_date == date:
            identifier = anime["identifier"]
            link = anime["link"]
            anime_url = f'https://animeworld.{AW_DOMAIN}/play/{link}.{identifier}'
            final_url = await get_mp4(anime_url,ismovie,episode,client)
            final_urls.append(final_url)
            break
    return final_urls
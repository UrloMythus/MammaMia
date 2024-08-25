import requests
from bs4 import BeautifulSoup
import datetime
import json
from info import get_info_kitsu
import config
AW_DOMAIN = config.AW_DOMAIN
def get_mp4(anime_url,ismovie,episode):
   response = requests.get(anime_url)
   soup = BeautifulSoup(response.text,'lxml')
   episode_page = soup.find('a', {'data-episode-num':episode })
   episode_page = f'https://animeworld.{AW_DOMAIN}{episode_page["href"]}'
   response = requests.get(episode_page)
   soup = BeautifulSoup(response.text,'lxml')
   a_tag  = soup.find('a', {'id': 'alternativeDownloadLink', 'class': 'm-1 btn btn-sm btn-primary'}) 
   url = a_tag['href']
   response = requests.head(url)
   if response.status_code == 404:
        url = None
   return url







def search(showname,date,ismovie,episode):
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

    response = requests.post(f'https://www.animeworld.{AW_DOMAIN}/api/search/v2', params=params, cookies=cookies, headers=headers)
    months = {
        "Gennaio": "January", "Febbraio": "February", "Marzo": "March", 
        "Aprile": "April", "Maggio": "May", "Giugno": "June", 
        "Luglio": "July", "Agosto": "August", "Settembre": "September", 
        "Ottobre": "October", "Novembre": "November", "Dicembre": "December"
    }
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
            final_url = get_mp4(anime_url,ismovie,episode)
            final_urls.append(final_url)
            break
    showname = showname + " (ITA)"
    params = {
        'keyword': showname,
    }
    response = requests.post(f'https://www.animeworld.{AW_DOMAIN}/api/search/v2', params=params, cookies=cookies, headers=headers)
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
            final_url = get_mp4(anime_url,ismovie,episode)
            final_urls.append(final_url)
            break
    return final_urls
def animeworld(id):
    try:
        kitsu_id = id.split(":")[1]
        episode = id.split(":")[2]
        ismovie = 1 if len(id.split(":")) == 2 else 0
        showname,date = get_info_kitsu(kitsu_id)
        final_urls = search(showname,date,ismovie,episode)
        print(final_urls)
        return final_urls
    except:
        print("Animeworld failed")
        return None

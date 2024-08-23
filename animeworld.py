import requests
from bs4 import BeautifulSoup
import datetime
import json
from info import get_info_kitsu
def get_mp4(anime_url,ismovie,episode):
   response = requests.get(anime_url)
   soup = BeautifulSoup(response.text,'lxml')
   a_tag  = soup.find('a', {'id': 'alternativeDownloadLink', 'class': 'm-1 btn btn-sm btn-primary'}) 
   url = a_tag['href']
   if ismovie == 1:
    response = requests.head(url)
    if response.status_code == 404:
        url = None
    return url
   elif ismovie == 0:
       parts = url.split("_Ep_")
       base = parts[0]
       episode_part = parts[1]
       episode_number, rest = episode_part.split("_", 1)
       num_digits = len(episode_number)
       episode = int(episode)
       new_episode_number = str(episode).zfill(num_digits)
       url = f"{base}_Ep_{new_episode_number}_{rest}"
       response = requests.head(url)
       if response.status_code == 404:
           url = None
       return url








def search(showname,date,ismovie,episode):
    cookies = {
    'sessionId': 's%3AtGSRfYcsIoaeV0nqFJgN69Zxixb_-uJU.fcNz%2FsJBiiP8v8TwthMN9%2FmynWFciI5gezZuz8CltyQ',
    }

    headers = {
        'authority': 'www.animeworld.so',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
         # 'content-length': '0',
         # 'cookie': 'sessionId=s%3AtGSRfYcsIoaeV0nqFJgN69Zxixb_-uJU.fcNz%2FsJBiiP8v8TwthMN9%2FmynWFciI5gezZuz8CltyQ',
         'csrf-token': 'oKFK43s4-BzfqPX27RlAORUd-iyiAfXyfDAo',
         'origin': 'https://www.animeworld.so',
         'referer': 'https://www.animeworld.so/',
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

    response = requests.post('https://www.animeworld.so/api/search/v2', params=params, cookies=cookies, headers=headers)
    months = {
        "Gennaio": "January", "Febbraio": "February", "Marzo": "March", 
        "Aprile": "April", "Maggio": "May", "Giugno": "June", 
        "Luglio": "July", "Agosto": "August", "Settembre": "September", 
        "Ottobre": "October", "Novembre": "November", "Dicembre": "December"
    }
    data = json.loads(response.text)
    final_urls = []
    i = 0
    for anime in data["animes"]:
        release_date = anime["release"]
        i+=1
        for ita, eng in months.items():
            release_date = release_date.replace(ita, eng)
        release_date = datetime.datetime.strptime(release_date, "%d %B %Y")
        release_date = release_date.strftime("%Y-%m-%d")
        if release_date == date:
            identifier = anime["identifier"]
            link = anime["link"]
            anime_url = f'https://animeworld.so/play/{link}.{identifier}'
            final_url = get_mp4(anime_url,ismovie,episode)
            final_urls.append(final_url)
        if i == 2:
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
animeworld("kitsi:12:10")

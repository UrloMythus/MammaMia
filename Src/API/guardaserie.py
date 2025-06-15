from Src.Utilities.info import  is_movie
from bs4 import BeautifulSoup,SoupStrainer
import re
import Src.Utilities.config as config
from fake_headers import Headers  
from Src.Utilities.loadenv import load_env  
import json, random
from Src.Utilities.info import get_info_imdb,get_info_tmdb
from Src.Utilities.eval import eval_solver
import urllib.parse
from Src.Utilities.convert import get_IMDB_id_from_TMDb_id
env_vars = load_env()
GS_PROXY = config.GS_PROXY
proxies = {}
if GS_PROXY == "1":
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
GS_ForwardProxy = config.GS_ForwardProxy
if GS_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
else:
    ForwardProxy = ""
#Get domain
GS_DOMAIN = config.GS_DOMAIN
random_headers = Headers()

async def get_supervideo_link(link,client):
    headers = random_headers.generate()
    response = await client.get(ForwardProxy + link, headers=headers, allow_redirects=True,timeout = 30, proxies = proxies)
    s2 = re.search(r"\}\('(.+)',.+,'(.+)'\.split", response.text).group(2)
    terms = s2.split("|")
    file_index = terms.index('file')
    #I start to loop from file cause hfs it's one or two position after it usually.

    for i in range(file_index,len(terms)):
        if "hfs" in terms[i]:
            hfs = terms[i]
            break
    urlset_index = terms.index('urlset')
    hls_index = terms.index('hls')
    result = terms[urlset_index + 1 : hls_index]
    #If the len is >1 then you have to merge the elements from the last to the first
    reversed_elements = result[::-1]
    base_url =f"https://{hfs}.serversicuro.cc/hls/"
    if len(reversed_elements) == 1:
        final_url = base_url + "," + reversed_elements[0] + ".urlset/master.m3u8"
    lenght = len(reversed_elements)
    i = 1    
    for element in reversed_elements:
        base_url += element + ","
        if lenght == i:
            base_url += ".urlset/master.m3u8"
        else:
            i += 1
    final_url = base_url
    return final_url



async def search_imdb(clean_id,client):
    try:
        headers = random_headers.generate()
        response = await client.get(ForwardProxy + f'{GS_DOMAIN}/?story={clean_id}&do=search&subaction=search', allow_redirects=True, impersonate = "chrome124", headers = headers, proxies = proxies)
        if response.status_code != 200:
            print(f"Guardaserie Failed to fetch search results: {response.status_code}")
        soup = BeautifulSoup(response.text,'lxml',parse_only=SoupStrainer('div',class_="mlnh-2"))
        div_mlnh2 = soup.select_one('div.mlnh-2:nth-of-type(2)')
        a_tag = div_mlnh2.find('h2').find('a')
        href = a_tag['href']
        return href
    except Exception as e:
        return None

async def search(showname,date,client):
    try:
        headers = random_headers.generate()
        showname = urllib.parse.quote(showname)
        response = await client.get(ForwardProxy + f'{GS_DOMAIN}/?story={showname}&do=search&subaction=search', allow_redirects=True, impersonate = "chrome124", headers = headers, proxies = proxies)
        if response.status_code != 200:
            print(f"Guardaserie Failed to fetch search results: {response.status_code}")
        soup = BeautifulSoup(response.text,'lxml',parse_only=SoupStrainer('div'))
        div_mlnew = soup.find_all('div', class_='mlnew')
        for mlnew in div_mlnew:
            div_date = mlnew.find('div', class_='mlnh-3 hdn').text
            div_date = div_date[:4]
            if div_date == date:
                a_tag = mlnew.find('div', class_='mlnh-2').find('h2').find('a')
                href = a_tag['href']
                return href

    except Exception as e:
        return None



async def player_url(page_url, season, episode,client):
    try:
        headers = random_headers.generate()
        response = await client.get(ForwardProxy + page_url, allow_redirects=True, impersonate = "chrome124", headers = headers, proxies = proxies)
        soup = BeautifulSoup(response.text,'lxml',parse_only=SoupStrainer('a'))
        a_tag = soup.find('a', id = f"serie-{season}_{episode}")
        href = a_tag['data-link']
        return href
    except Exception as e:
        return None





async def guardaserie(id,client):
    try:
        general = await is_movie(id)
        ismovie = general[0]
        clean_id = general[1]
        season = general[2]
        episode = general[3]
        if "tt" not in clean_id:
            clean_id = await get_IMDB_id_from_TMDb_id(clean_id,client) 
            print(clean_id)
        '''
        type = "Guardaserie"
        if "tt" in id:
            showname,date = await get_info_imdb(clean_id,ismovie,type,client)
        else:
            showname,date = get_info_tmdb(clean_id,ismovie,type)
        showname = showname.replace("'"," ")
        if "Guru" in showname:
            showname = showname.split("-")[0]
        '''
        if ismovie == 1:
            return None
        '''
        page_url = await search(showname,date,client)
        '''
        page_url = await search_imdb(clean_id,client)
        supervideo_link =await player_url(page_url,season,episode,client)
        if supervideo_link: 
            final_url = await eval_solver(supervideo_link,proxies, ForwardProxy, client)
            return final_url
        else:
            print("Couldn't find iframe source")
            return None
    except Exception as e:
        print("MammaMia: Guardaserie Failed",e)
        return None
    


async def test_script():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        # Replace with actual id, for example 'anime_id:episode' format
        test_id = "tmdb:36247:1:1"  # This is an example ID format tt0460649
        results = await guardaserie(test_id, client)
        print(results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_script())
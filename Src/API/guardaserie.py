from Src.Utilities.info import  is_movie
from bs4 import BeautifulSoup,SoupStrainer
import re
import Src.Utilities.config as config
from fake_headers import Headers  
from Src.Utilities.loadenv import load_env  
import json, random
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







async def search(clean_id,client):
    try:
        headers = random_headers.generate()
        response = await client.get(ForwardProxy + f'https://guardaserietv.{GS_DOMAIN}/?story={clean_id}&do=search&subaction=search', allow_redirects=True, impersonate = "chrome124", headers = headers, proxies = proxies)
        if response.status_code != 200:
            print(f"Guardaserie Failed to fetch search results: {response.status_code}")
        soup = BeautifulSoup(response.text,'lxml',parse_only=SoupStrainer('div',class_="mlnh-2"))
        div_mlnh2 = soup.select_one('div.mlnh-2:nth-of-type(2)')
        a_tag = div_mlnh2.find('h2').find('a')
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
        if ismovie == 1:
            return None
        page_url = await search(clean_id,client)
        supervideo_link =await player_url(page_url,season,episode,client)
        final_url = await get_supervideo_link(supervideo_link,client)
        return final_url
    except Exception as e:
        print("MammaMia: Guardaserie Failed",e)
        return None
    


async def test_script():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        # Replace with actual id, for example 'anime_id:episode' format
        test_id = "tt1190634:1:1"  # This is an example ID format
        results = await guardaserie(test_id, client)
        print(results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_script())
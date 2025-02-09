from Src.Utilities.info import  is_movie
from bs4 import BeautifulSoup,SoupStrainer
import re
import Src.Utilities.config as config
from fake_headers import Headers  
from Src.Utilities.loadenv import load_env  
import json, random
env_vars = load_env()
GH_PROXY = config.GH_PROXY
proxies = {}
if GH_PROXY == "1":
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
GH_ForwardProxy = config.GH_ForwardProxy
if GH_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
else:
    ForwardProxy = ""
#Get domain

GHD_DOMAIN = config.GHD_DOMAIN

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
    headers = random_headers.generate()
    response = await client.get(ForwardProxy + f"https://mostraguarda.{GHD_DOMAIN}/set-movie-a/{clean_id}", allow_redirects=True, impersonate = "chrome124", headers = headers, proxies = proxies)
    if response.status_code != 200:
            print(f"GuardaHD Failed to fetch search results: {response.status_code}")
    soup = BeautifulSoup(response.text,'lxml',parse_only=SoupStrainer('li'))
    li_tag = soup.find('li')
    href = "https:" + li_tag['data-link']
    return href



async def guardahd(id,client):
    try:
        general = await is_movie(id)
        ismovie = general[0]
        clean_id = general[1]
        if ismovie == 0:
            return None
        supervideo_link = await search(clean_id,client)
        final_url = await get_supervideo_link(supervideo_link,client)
        return final_url
    except Exception as e:
        print("MammaMia: GuardaHD Failed",e)
        return None
    
async def test_script():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        # Replace with actual id, for example 'anime_id:episode' format
        test_id = "tt9218128"  # This is an example ID format
        results = await guardahd(test_id, client)
        print(results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_script())
    
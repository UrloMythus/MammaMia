import requests
import re
from bs4 import BeautifulSoup, SoupStrainer
from Src.Utilities.info import get_info_imdb, is_movie, get_info_tmdb
import urllib.parse
import Src.Utilities.config as config
import urllib.parse
DDL_DOMAIN = config.DDL_DOMAIN
ips4_device_key = config.ips4_device_key
ips4_login_key = config.ips4_login_key
ips4_member_id = config.ips4_member_id
ips4_IPSSessionFront = config.ips4_IPSSessionFront
cookies = {
    'ips4_device_key': ips4_device_key,
    'ips4_IPSSessionFront': ips4_IPSSessionFront,
    'ips4_member_id': ips4_member_id,
    'ips4_login_key': ips4_login_key,
    }

async def search_series(client,id,season,episode,showname):
    showname = showname.replace(" ", "%20").replace("–", "+").replace("—","+")
    response = await client.get(f"{DDL_DOMAIN}/search/?&q={showname}%20{season}%20Streaming&type=videobox_video&quick=1&nodes=11,36&search_and_or=and&search_in=titles&sortby=relevancy")
    soup = BeautifulSoup(response.text, 'lxml',parse_only=SoupStrainer('a'))
    a_tags = soup.find_all('a', {'data-linktype': 'link'})
    for a in a_tags:
        href = a['href']
        response = await client.get(href, cookies = cookies)
        soup = BeautifulSoup(response.text, 'lxml')
        movie_ids = soup.find_all('a',{'rel':'external nofollow'})
        for database in movie_ids:
            link = database['href']
            real_id = link.split('/')[4]
            if real_id == id:
                meta_description = soup.find('meta',{'name':'description'})
                content = meta_description['content']
                if f"Stagione {season}" in content:
                    return href
                else:
                    continue
            else:
                continue

async def get_episode(client,link,episode):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': link,
        'DNT': '1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Connection': 'keep-alive',
    #   'Cookie': 'ips4_device_key=b6f084be79c28bb53ecfc556fd7a2a70; ips4_IPSSessionFront=f2b9db91793e084cf2003a07c563e6aa; ips4_ipsTimezone=Europe/Rome; ips4_hasJS=true; ips4_noCache=1; ips4_announcement_3=true; ips4_member_id=4029711; ips4_login_key=41b6a70b16cce2fd39482f5b21a9c35f; ips4_loggedIn=1725985598',
        'Priority': 'u=1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    params = {
        'area': 'online',
    }


    response = await client.get(link, cookies = cookies, headers = headers, params = params, impersonate="chrome120")

    pattern = rf'<a\s+href="([^"]+)"[^>]*>\s*Part {episode}\s*</a>'
    match = re.search(pattern, response.text)
    mp4_link = match.group(1)
    mp4_link = mp4_link.replace("&amp","")
    mp4_link = mp4_link.replace(";","&")
    return mp4_link

async def search_movie(client,showname,id):
    showname = showname.replace("–", "+").replace("—","+")
    showname = urllib.parse.quote(showname)
    link = f"{DDL_DOMAIN}/search/?&q={showname}%20Streaming&quick=1&nodes=11&search_and_or=and&search_in=titles&sortby=relevancy"    
    response = await client.get(link,impersonate = "chrome120")
    soup = BeautifulSoup(response.text, 'lxml',parse_only=SoupStrainer('a'))
    a_tags = soup.find_all('a', {'data-linktype': 'link'})
    for a in a_tags:
        href = a['href']
        response = requests.get(href, cookies = cookies)
        soup = BeautifulSoup(response.text, 'lxml', parse_only=SoupStrainer('a'))
        movie_ids = soup.find_all('a',{'rel':'external nofollow'})
        for database in movie_ids:
            link = database['href']
            real_id = link.split('/')[4]
            if real_id == id:
                return href
            else:
                continue
    return



async def get_mp4(client,link):
    response = await client.get(link, cookies = cookies)   
    soup = BeautifulSoup(response.text,'lxml',parse_only=SoupStrainer('source'))
    source_tag = soup.find('source')
    final_url = source_tag['src']
    res = source_tag.get('res')
    return final_url,res














async def ddlstream(imdb,client):
    try:
        general = await is_movie(imdb)
        ismovie = general[0]
        id = general[1]
        type = "DDLStream"
        if "tt" in imdb:
                showname = await get_info_imdb(id,ismovie,type,client)
        else:
            showname = get_info_tmdb(id,ismovie,type)
        if ismovie == 0:
            season  = general[2]
            episode = general[3]
            page_link = await search_series(client,id,season,episode,showname)
            mp4_link = await get_episode(client,page_link,episode)
            final_url = await get_mp4(client,mp4_link)
            return final_url
        else:
             page_link = await search_movie(client,showname,id)
             mp4_link = page_link + "?area=online"
             final_url = await get_mp4(client,mp4_link)
             return final_url
            
    except Exception as e:
        print(f"MammaMia: DDLStream Failed {e}")
        return None
    

async def test_animeworld():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        test_id = "tt14948432"  # This is an example ID format
        results = await ddlstream(test_id, client)
        print(results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_animeworld())


    #python3 -m Src.API.ddlstream

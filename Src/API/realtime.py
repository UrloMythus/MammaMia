from Src.Utilities.info import get_info_tmdb, is_movie, get_info_imdb
import Src.Utilities.config as config
from fake_headers import Headers  
from Src.Utilities.loadenv import load_env  
from urllib.parse import quote
import logging
from Src.Utilities.config import setup_logging
level = config.LEVEL
import random
Icon = config.Icon
Name = config.Name
logger = setup_logging(level)
env_vars = load_env()
random_headers = Headers()
RT_PROXY = config.RT_PROXY
proxies = {}
if RT_PROXY == "1":
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
RT_ForwardProxy = config.RT_ForwardProxy
if RT_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
else:
    ForwardProxy = ""


endpoints = {
    'it' : 'https://public.aurora.enhanced.live',
    'dplay' : 'https://eu1-prod.disco-api.com'
}
async def search(showname,date,client):
    showname = showname.split('-')[0]
    showname = quote(showname)
    response = await client.get(ForwardProxy + f'https://public.aurora.enhanced.live/site/search/page/?include=default&filter[environment]=realtime&v=2&q={showname}&page[number]=1&page[size]=20', proxies = proxies)
    data = response.json()
    for item in data['data']:
        return item['slug']



async def program_info(slug,season,episode,client):
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://realtime.it/',
    'Origin': 'https://realtime.it',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'DNT': '1',
    'Priority': 'u=4',
    }
    link = f'https://public.aurora.enhanced.live/site/page/{slug}/?include=default&filter[environment]=realtime&v=2&parent_slug=programmi-real-time'
    
    response = await client.get(ForwardProxy + link,headers = headers, proxies = proxies)
    data = response.json()
    for item in reversed(data['blocks'][1]['items']):
        if season ==  item['seasonNumber'] and episode == item['episodeNumber']:
            if 'aurora' in data['blocks'][0]['item']['poster']['src']:
                platform = 'IT'
            elif 'eu1-prod' in data['blocks'][0]['item']['poster']['src']:
                platform = 'DPLAY'
            x_realm_it = ''
            x_realm_dplay = ''
            if 'X-REALM-IT' in data['userMeta']['realm']:
                x_realm_it = data['userMeta']['realm']['X-REALM-IT']
            if 'X-REALM-DPLAY' in data['userMeta']['realm']:
                x_realm_dplay = data['userMeta']['realm']['X-REALM-DPLAY']
            return item['id'],x_realm_it,x_realm_dplay, platform
    return None,None,None,None

async def get_token(client):
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://realtime.it/',
    'Content-Type': 'application/json',
    'X-disco-client': 'WEB:UNKNOWN:wbdatv:2.1.9',
    'X-disco-params': 'realm=dplay',
    'X-Device-Info': 'STONEJS/1 (Unknown/Unknown; Linux/undefined; Unknown)',
    'Origin': 'https://realtime.it',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'DNT': '1',
    'Priority': 'u=4',
    }
    response = await client.get(ForwardProxy + 'https://public.aurora.enhanced.live/site/page/casa-a-prima-vista/?include=default&filter[environment]=realtime&v=2&parent_slug=programmi-real-time', headers = headers, proxies = proxies)
    data = response.json()
    x_realm_it = data['userMeta']['realm']['X-REALM-IT']
    x_realm_dplay = data['userMeta']['realm']['X-REALM-DPLAY']
    return x_realm_it,x_realm_dplay



async def get_url(id, endpoint, x_realm_it,x_realm_dplay,streams,client):
    if 'IT' in endpoint:
        base_url = endpoints['it']
        token = x_realm_it
    elif 'DPLAY' in endpoint:
        base_url = endpoints['dplay']
        token = x_realm_dplay
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://realtime.it/',
    'Content-Type': 'application/json',
    'X-disco-client': 'WEB:UNKNOWN:wbdatv:2.1.9',
    'X-disco-params': 'realm=dplay',
    'X-Device-Info': 'STONEJS/1 (Unknown/Unknown; Linux/undefined; Unknown)',
    'Authorization': f'Bearer {token}',
    'Origin': 'https://realtime.it',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'DNT': '1',
    'Priority': 'u=4',
    }


    json_data = {
    'deviceInfo': {
        'adBlocker': False,
        'drmSupported': True,
        'hdrCapabilities': [
            'SDR',
        ],
        'hwDecodingCapabilities': [],
        'soundCapabilities': [
            'STEREO',
        ],
    },
    'wisteriaProperties': {},
    'videoId': id,
    }
    response = await client.post(ForwardProxy + f'{base_url}/playback/v3/videoPlaybackInfo', headers=headers, json=json_data, proxies = proxies)
    data = response.json()

    for item in data['data']['attributes']['streaming']:
        if item['type'] == 'hls':
            m3u8 = item['url']
            streams['streams'].append({'name': f"{Name}",'title': f'{Icon}▶️ Realtime\n HLS', 'url': m3u8, 'behaviorHints': {'bingeGroup': f'realtimehls'}})

        elif item['type'] == 'dash':
            mpd = item['url']
            streams['streams'].append({'name': f"{Name}",'title': f'{Icon}▶️ Realtime\n MPD', 'url': mpd, 'behaviorHints': {'bingeGroup': f'realtimempd'}})

    return streams




async def search_catalog(query,catalog,client):
    showname = quote(query)
    response = await client.get(f'https://public.aurora.enhanced.live/site/search/page/?include=default&filter[environment]=realtime&v=2&q={showname}&page[number]=1&page[size]=20')
    data = response.json()
    for item in data['data']:
        title = item['title']
        description = item['subtitle']
        date = item['datePublished'].split('-')[0]
        id = item['slug']
        image = item['image']['url']
        typeof = item['type']
        catalog['metas'].append({'id': f'realtime{typeof}:'+id, 'type': "series",'name': f'{title}', 'description': description, 'releaseInfo': date, 'background': image, 'poster': image })
    return catalog

async def meta_catalog(id,catalog,client):
    try:
        headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://realtime.it/',
        'Origin': 'https://realtime.it',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'DNT': '1',
        'Priority': 'u=4',
        }
        parts = id.split(':')
        slug = parts[1]
        parts2 = parts[0].split('realtime')
        typeof= parts2[1]
        if typeof == 'showpage':
            link = f'https://public.aurora.enhanced.live/site/page/{slug}/?include=default&filter[environment]=realtime&v=2&parent_slug=programmi-real-time'
        elif typeof == 'article':
            link = f'https://public.aurora.enhanced.live/site/page/{slug}/?include=default&filter[environment]=realtime&v=2'

        response = await client.get(ForwardProxy + link,headers = headers, proxies = proxies)
        data = response.json()
        title = data['title']
        subtitle = data['subtitle']
    
        if  data['type'] == 'articlepage':
            if data['blocks'][1]['sonicOverrideEnabled'] == True:
                platform = 'IT'
            else:
                platform = 'DPLAY'
        elif data['type'] == 'showpage':
            if 'aurora' in data['blocks'][0]['item']['poster']['src']:
                platform = 'IT'
            elif 'eu1-prod' in data['blocks'][0]['item']['poster']['src']:
                platform = 'DPLAY'
        if typeof == 'showpage':
            for item in reversed(data['blocks'][1]['items']):
                id = item['id']
                description = item['description']
                episode = item['episodeNumber']
                season = item['seasonNumber']
                poster = item['poster']
                date = item['publishStart']
                catalog['meta']['videos'].append({'title': f'S{season}'+ f'E{episode}','season': season, 'episode': episode,'firstAired':date,'overview': description, 'thumbnail': poster['src'], 'id': f'realtime{platform}:id:'+id})
        elif typeof == 'article':
            item = data['blocks'][1]['item']
            id = item['id']
            description = item['description']
            episode = item['episodeNumber']
            season = item['seasonNumber']
            poster = item['poster']
            date = item['publishStart']
            catalog['meta']['videos'].append({'title': f'{title}','season': season, 'episode': episode,'firstAired':date,'overview': description, 'thumbnail': poster['src'], 'id': f'realtime{platform}:id:'+id})

        catalog['meta']['name'] = title
        catalog['meta']['description'] = subtitle 
        catalog['meta']['releaseInfo'] = '-' + data['datePublished'].split('-')[0]
        catalog['meta']['background'] = data['metaMedia'][0]['media']['url']
        return catalog
    except Exception as e:
        catalog['meta']['name'] = title
        catalog['meta']['description'] = subtitle 
        catalog['meta']['releaseInfo'] = '-' + data['datePublished'].split('-')[0]
        catalog['meta']['background'] = data['metaMedia'][0]['media']['url']
        return catalog
async def realtime(streams,id,client):
    try:
        if 'realtime' in id:
            parts = id.split('id:')
            id = parts[1]
            endpoint = parts[0]
            x_realm_it,x_realm_dplay = await get_token(client)
            streams = await get_url(id, endpoint, x_realm_it,x_realm_dplay,streams,client)
        else:
            general = await is_movie(id)
            ismovie = general[0]
            clean_id = general[1]
            type = "Realtime"
            if ismovie == 0 : 
                season = int(general[2])
                episode = int(general[3])
            elif ismovie == 1:
                season = None
                episode = None
            if "tmdb" in id:
                showname,date = get_info_tmdb(clean_id,ismovie,type)
            else:
                showname,date = await get_info_imdb(clean_id,ismovie,type,client)
            logger.info(f'RT {showname}')
            slug = await search(showname,date,client)
            id,x_realm_it,x_realm_dplay,platform = await program_info(slug,season,episode,client)
            streams = await get_url(id,platform,x_realm_it,x_realm_dplay,streams,client)
        return streams
    except Exception as e:
        logger.warning(f'RT {e}')
        return streams




async def test_realtime():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        results = await realtime({'streams': []},"tt5684368:13:10",client)
        print(results)

        
if __name__ == "__main__":
    import asyncio
    asyncio.run(test_realtime()) 
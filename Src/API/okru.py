from bs4 import BeautifulSoup
import json
from Src.Utilities.dictionaries import okru
User_Agent= "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0"


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

async def okru_get_url(id,client):
    try:
        embed_link = okru[id]
        response = await client.get(embed_link, allow_redirects=True, headers = headers, impersonate = "chrome124")
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find('div', {'data-module': 'OKVideo'})
        data_options = div.get('data-options')
        data = json.loads(data_options)
        metadata = json.loads(data['flashvars']['metadata'])
        m3u8_link = metadata['hlsMasterPlaylistUrl']
        print("MammaMia: Found results for Okru")
        return m3u8_link
    except Exception as e:
        print("MammaMia: No results found for Okru")
        return None
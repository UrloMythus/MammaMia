from bs4 import BeautifulSoup
import json
from Src.Utilities.dictionaries import okru



async def okru_get_url(id,client):
    try:
        embed_link = okru[id]
        print(embed_link)
        response = await client.get(embed_link, allow_redirects=True, impersonate = "chrome120")
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find('div', {'data-module': 'OKVideo'})
        data_options = div.get('data-options')
        data = json.loads(data_options)
        metadata = json.loads(data['flashvars']['metadata'])
        m3u8_link = metadata['hlsMasterPlaylistUrl']
        print("MammaMia: Found results for Okru")
        print(m3u8_link)
        return m3u8_link
    except Exception as e:
        print("MammaMia: No results found for Okru")
        return None
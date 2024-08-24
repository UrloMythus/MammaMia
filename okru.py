import requests
from bs4 import BeautifulSoup
import json
from dictionaries import okru



def okru_get_url(id):
    embed_link = okru[id]
    print(embed_link)
    response = requests.get(embed_link)
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find('div', {'data-module': 'OKVideo'})
    data_options = div.get('data-options')
    data = json.loads(data_options)
    metadata = json.loads(data['flashvars']['metadata'])
    m3u8_link = metadata['hlsMasterPlaylistUrl']
    print(m3u8_link)
    return m3u8_link

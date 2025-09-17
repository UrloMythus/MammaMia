from fake_headers import Headers
import  Src.Utilities.config as config
from bs4 import BeautifulSoup,SoupStrainer
import re
import time
import logging
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)
Icon = config.Icon
Name = config.Name
random_headers = Headers()





async def deltabit(page_url,client,streams,site_name,proxies,ForwardProxy,language):
    """Extract Deltabit URL."""
    i = 0
    #Set up some headers
    headers = random_headers.generate()
    headers2 = random_headers.generate()

    #Get the redirected link, so the actual deltabit link.
    page_url_response = await client.get(ForwardProxy + page_url,headers={**headers, 'Range': 'bytes=0-0'}, proxies=proxies)
    page_url = page_url_response.url
    logger.info(f"Page_URl is {page_url}")

    #Change the referer  and user agent of the generated headers
    headers2['referer'] = 'https://safego.cc/'
    headers2['user-agent'] =  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'

    #Request to the deltabit link
    response = await client.get(ForwardProxy + page_url, headers = headers2, allow_redirects = True, proxies = proxies)
    page_url = response.url
    #Often deltabit redirects to another deltabit link. We need the redirected link to put it in the headers.
    origin = page_url.split('/')[2]
    headers['origin'] = f'https://{origin}'
    headers['referer'] = page_url
    headers['user-agent'] =  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    #We check the page for the data such as hash and fname.
    soup = BeautifulSoup(response.text, 'lxml', parse_only=SoupStrainer('input'))
    data = {}
    for input in soup:
        name = input.get('name')
        value = input.get('value')
        data[name] = value 
    data['imhuman'] = ''
    data['referer']= page_url
    #We need to wait 2.5 seconds or the request will fail
    time.sleep(2.5)
    
    
    fname = data['fname']
    #Request to the deltabit link
    response = await client.post(ForwardProxy + page_url, data = data, headers = headers, proxies = proxies)
    link = re.findall(r'sources:\s*\["([^"]+)"', response.text, re.DOTALL)
    if not link:
        if not i >= 3:
            page_url = 'https://deltabit.co/q4r8w4assff4'
            link,fname = await deltabit(page_url,client,streams,site_name,proxies,ForwardProxy,language)
            i +=1
    else:
        link = link[0]
    if link:
        streams['streams'].append({'name': f"{Name}{language}",'title': f'{Icon}{site_name}\n▶️ Deltabit\n{fname}', 'url': link, 'behaviorHints': {'bingeGroup': f'{site_name.lower()}'}})

    
    return streams




#Testing
async def test_deltabit():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        results = await deltabit("https://deltabit.co/a54ehb8w42pe",client,{'streams': []},'Deltabit', {},"","")
        print(results)
if __name__ == "__main__":
    import asyncio
    asyncio.run(test_deltabit()) 

# https://loadm.cam/#cfnqx
import  Src.Utilities.config as config
Icon = config.Icon
Name = config.Name
import re
from fake_headers import Headers
random_headers = Headers()
import logging
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)





async def hdplayer(hdplayer,client,streams,Referer,site_name,proxies,ForwardProxy):
    headers = random_headers.generate()
    response = await client.get(hdplayer, allow_redirects=True, headers = headers)
    match = re.search(r'sources:\s*\[\s*\{\s*file\s*:\s*"([^"]*)"', response.text)
    url = match.group(1)
    if url:
        #Fix for Exoplayer which needs .m3u8 in the url to play the file
        url = url + ".m3u8"
        streams['streams'].append({'name': f"{Name}\n720/1080p",'title': f'{Icon}{site_name}\n ▶️ HDPlayer', 'url': url,  'behaviorHints': {'proxyHeaders': {"request": {"Referer": Referer}}, 'notWebReady': True, 'bingeGroup': f'{site_name.lower()}'}})
        logger.info(f"{site_name} on HDPlayer found results for the current ID")

    return streams





#Testing
async def test_hdplayer():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        results = await hdplayer("https://hdplayer.gives/embed/udnjutxECQGuwsU",client,{'streams': []},'https://hdplayer.gives/', "StreamingWatch", {},'')
        print(results)
if __name__ == "__main__":
    import asyncio
    asyncio.run(test_hdplayer()) 
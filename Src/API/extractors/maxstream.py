import  Src.Utilities.config as config
from Src.Utilities.eval import eval_solver
import logging
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)
Icon = config.Icon
Name = config.Name
from fake_headers import Headers
random_headers = Headers()
import re

async def maxstream(url,client,streams,site_name,language,proxies,ForwardProxy):
    headers = random_headers.generate()
    response = await client.get( ForwardProxy + url,  allow_redirects=True, timeout=30, headers = headers, proxies = proxies, impersonate = "chrome")
    pattern = r'sources\W+src\W+(.*)",'
    match = re.search(pattern,response.text)
    if match:
        url = match.group(1)
        logger.info(f"{site_name} on Maxstream found results for the current ID")
        streams['streams'].append({'name': f"{Name}{language}",'title': f'{Icon}{site_name}\n▶️ Maxstream', 'url': url, 'behaviorHints': { 'bingeGroup': f'{site_name.lower()}'}})
    return streams

async def test_maxstream():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        results = await maxstream("https://maxstream.video/emvvv/a7wc8bb0h68c",client,{'streams': []},'CB01', {},'')
        print(results)
if __name__ == "__main__":
    import asyncio
    asyncio.run(test_maxstream()) 
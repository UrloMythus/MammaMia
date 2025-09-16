from fake_headers import Headers
import  Src.Utilities.config as config
Icon = config.Icon
Name = config.Name
from Src.Utilities.mfp import build_mfp
from fake_headers import Headers
import re
import logging
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)
random_headers = Headers()

async def uqload(player_link,client,MFP,MFP_CREDENTIALS,streams,site_name,proxies,ForwardProxy):
    headers = random_headers.generate()
    if MFP == "1":
        url = await build_mfp(MFP_CREDENTIALS, player_link, "Uqload",client)
        streams['streams'].append({'name': f"{Name} 🕵️‍♂️",'title': f'{Icon}{site_name}\n▶️ Uqload', 'url': url, 'behaviorHints': {'proxyHeaders': {"request": {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'}}, 'notWebReady': True, 'bingeGroup': 'guardaflix'}})
        return streams
    response = await client.get(ForwardProxy + player_link, headers = headers, proxies = proxies)
    video_url_match = re.search(r'sources: \["(.*?)"]', response.text)
    title = re.search(r'title: "(.*?)"', response.text).group(1)
    if video_url_match:
        url = video_url_match.group(1)
        if url:
            streams['streams'].append({'name': f"{Name}",'title': f'{Icon}{site_name}\n▶️ Uqload\n{title}', 'url': url, 'behaviorHints': {'proxyHeaders': {"request": {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'}}, 'notWebReady': True, 'bingeGroup': f'{site_name.lower()}'}})
            logger.info(f"{site_name} on Uqload found results for the current ID")
            return streams
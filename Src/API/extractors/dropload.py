import  Src.Utilities.config as config
from Src.Utilities.eval import eval_solver
import logging
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)
Icon = config.Icon
Name = config.Name



async def dropload(player_link,client,streams,site_name, proxies, ForwardProxy):
    url = await eval_solver(player_link, proxies,ForwardProxy, client)
    if url:
        streams['streams'].append({'name': f"{Name}",'title': f'{Icon}{site_name}\n▶️ Dropload', 'url': url, 'behaviorHints': {'proxyHeaders': {"request": {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'}}, 'notWebReady': True, 'bingeGroup': f'{site_name.lower()}'}})
        logger.info(f"{site_name} on Dropload found results for the current ID")

    return streams
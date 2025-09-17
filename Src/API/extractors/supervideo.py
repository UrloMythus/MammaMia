import  Src.Utilities.config as config
from Src.Utilities.eval import eval_solver
import logging
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)
Icon = config.Icon
Name = config.Name




async def supervideo(supervideo_link,client,streams, site_name, proxies,ForwardProxy):
    url = await eval_solver(supervideo_link,proxies, ForwardProxy, client)
    if url:
        streams['streams'].append({'name': f"{Name}",'title': f'{Icon}{site_name}\n▶️ Supervideo', 'url': url, 'behaviorHints': {'bingeGroup': f'{site_name.lower()}'}})
        logger.info(f"{site_name} on SuperVideo found results for the current ID")
    return streams
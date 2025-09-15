import  Src.Utilities.config as config
Icon = config.Icon
Name = config.Name
from Src.Utilities.mfp import build_mfp
import logging
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)
from Src.Utilities.eval import eval_solver


async def mixdrop(url,client,MFP,MFP_CREDENTIALS,streams,site_name,proxies,ForwardProxy,language):
    """Extract Mixdrop URL."""
    if "club" in url:
        url = url.replace("club", "cv").split("/2")[0]
    if "cfd" in url:
        url = url.replace("cfd", "cv").replace("emb","e").split("/2")[0]
    if MFP == "1": 
        url = await build_mfp(MFP_CREDENTIALS,url,"Mixdrop",client)
        if url and "https%3ANone" not in url:
            logger.info(f"{site_name} on Mixdrop found results for the current ID")
            streams['streams'].append({'name': f"{Name} 🕵️‍♂️\n{language}",'title': f'{Icon}{site_name}\n▶️ MixDrop', 'url': url, 'behaviorHints':{'bingeGroup': f'{site_name.lower()}'}})

    else:
        headers = {"accept-language": "en-US,en;q=0.5"}
        url = await eval_solver(url, proxies , ForwardProxy, client)
        if url:
            url = "https:" + url
            logger.info(f"{site_name} on Mixdrop found results for the current ID")
            streams['streams'].append({'name': f"{Name}{language}",'title': f'{Icon}{site_name}\n▶️ MixDrop', 'url': url, 'behaviorHints': {'proxyHeaders': {"request": {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'}}, 'notWebReady': True, 'bingeGroup': f'{site_name.lower()}'}})
    return streams
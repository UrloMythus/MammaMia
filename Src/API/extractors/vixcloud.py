from fake_headers import Headers
import re
from bs4 import BeautifulSoup,SoupStrainer
random_headers = Headers()
import  Src.Utilities.config as config
Icon = config.Icon
Name = config.Name
from Src.Utilities.mfp import build_mfp
import logging
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)
SC_DOMAIN = config.SC_DOMAIN
User_Agent= "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"


async def vixcloud(link,client,MFP,MFP_CREDENTIALS,streams,site_name,proxies,ForwardProxy):
    if MFP == "1":
        final_url = await build_mfp(MFP_CREDENTIALS, link, "VixCloud",client)
        quality = ""
        mfp_icon = '🕵️‍♂️'
        if final_url:
            streams['streams'].append({"name":f'{Name} {mfp_icon}\n{quality}', 'title': f'{Icon} StreamingCommunity\n▶️ Vixcloud','url': final_url,'behaviorHints': {'bingeGroup': f'{site_name.lower()}{quality}'}})
            return streams
    mfp_icon = ''
    headers =  random_headers.generate()
    headers['Referer'] = f"{SC_DOMAIN}/"
    headers['Origin'] = f"{SC_DOMAIN}"
    headers['User-Agent'] = User_Agent
    headers['user-agent'] = User_Agent
    response = await client.get(link)        
    if response.status_code != 200:
        logger.warning(f"Failed to extract URL components from VixSRC, Invalid Request: {response.status_code}") 
    soup = BeautifulSoup(response.text, "lxml", parse_only=SoupStrainer("body"))
    if soup:
        script = soup.find("body").find("script").text
        token = re.search(r"'token':\s*'(\w+)'", script).group(1)
        expires = re.search(r"'expires':\s*'(\d+)'", script).group(1)
        server_url = re.search(r"url:\s*'([^']+)'", script).group(1)
        try:
            quality = re.search(r'"quality":(\d+)', script).group(1)
        except:
            quality = ""
        if "?b=1" in server_url:
            final_url = f'{server_url}&token={token}&expires={expires}'
        else:
            final_url = f"{server_url}?token={token}&expires={expires}"
        if "window.canPlayFHD = true" in script:
            final_url += "&h=1"
    if final_url:
        logger.info(f"Vixcloud Found Results for the current ID")
        #We add .m3u8 after the VixID in order to make the video playable by ExoPlayer
        parts_final_url = final_url.split("?")
        first_part_final_url = parts_final_url[0] + ".m3u8"
        final_url = first_part_final_url + "?" + parts_final_url[1]
        streams['streams'].append({"name":f'{Name} {mfp_icon}\n{quality}', 'title': f'{Icon} StreamingCommunity\n▶️ Vixcloud','url': final_url,'behaviorHints': {'proxyHeaders': {"request": {"user-agent": User_Agent}}, 'notWebReady': True, 'bingeGroup': f'{site_name.lower()}{quality}'}})

    return streams









#Testing
async def test_vixcloud():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        results = await vixcloud("https://vixsrc.to/tv/204082/1/3/",client,"0",['',''],{'streams': []},'guardoserie.live', {},'')
        print(results)
if __name__ == "__main__":
    import asyncio
    asyncio.run(test_vixcloud()) 


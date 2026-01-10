'''
Code taken from https://github.com/mhdzumair/mediaflow-proxy/blob/main/mediaflow_proxy/extractors/voe.py adpted to work with MammaMia
The owner of MammaMia should not be thanked for any code in this script. 
'''




import base64
import re
from typing import Dict, Any
from urllib.parse import urljoin
import  Src.Utilities.config as config
from Src.Utilities.config import setup_logging
from Src.Utilities.mfp import build_mfp

level = config.LEVEL
logger = setup_logging(level)
Icon = config.Icon
Name = config.Name
from fake_headers import Headers
random_headers = Headers()


async def voe(url,streams,site_name,MFP,MFP_CREDENTIALS,proxies,ForwardProxy,client):
        if MFP == '1':
            url = await build_mfp(MFP_CREDENTIALS,url,"Voe",client)
            if url and "https%3ANone" not in url:
                logger.info(f"{site_name} on Voe found results for the current ID")
                streams['streams'].append({'name': f"{Name} 🕵️‍♂️",'title': f'{Icon}{site_name}\n▶️ Voe', 'url': url, 'behaviorHints':{'bingeGroup': f'{site_name.lower()}'}})
                return streams
        
        
        headers = random_headers.generate()
        response = await client.get(ForwardProxy + url,headers=headers, impersonate = 'chrome', proxies = proxies)

        # See https://github.com/Gujal00/ResolveURL/blob/master/script.module.resolveurl/lib/resolveurl/plugins/voesx.py
        redirect_pattern = r'''window\.location\.href\s*=\s*'([^']+)'''
        redirect_match = re.search(redirect_pattern, response.text, re.DOTALL)
        if redirect_match:
            if redirected:
                logger.info("VOE: too many redirects")

            return await voe(redirect_match.group(1))

        code_and_script_pattern = r'json">\["([^"]+)"]</script>\s*<script\s*src="([^"]+)'
        code_and_script_match = re.search(code_and_script_pattern, response.text, re.DOTALL)
        if not code_and_script_match:
             logger.info("VOE: unable to locate obfuscated payload or external script URL")
        

        script_response = await client.get(ForwardProxy+urljoin(url, code_and_script_match.group(2)),headers=headers, proxies = proxies)

        luts_pattern = r"(\[(?:'\W{2}'[,\]]){1,9})"
        luts_match = re.search(luts_pattern, script_response.text, re.DOTALL)
        if not luts_match:
            logger.info("VOE: unable to locate LUTs in external script")

        data = voe_decode(code_and_script_match.group(1), luts_match.group(1))

        final_url = data.get('source')
        if not final_url:
            logger.info("VOE: failed to extract video URL")
            return streams
        if final_url:
            logger.info(f"{site_name} on Voe found results for the current ID")
            streams['streams'].append({'name': f"{Name}",'title': f'{Icon}{site_name}\n▶️ Voe', 'url': final_url, 'behaviorHints': {'proxyHeaders': {"request": {"Referer": url}}, 'notWebReady': True, 'bingeGroup': f'{site_name.lower()}'}})

        return streams
        
def voe_decode(ct: str, luts: str) -> Dict[str, Any]:
        import json
        lut = [''.join([('\\' + x) if x in '.*+?^${}()|[]\\' else x for x in i]) for i in luts[2:-2].split("','")]
        txt = ''
        for i in ct:
            x = ord(i)
            if 64 < x < 91:
                x = (x - 52) % 26 + 65
            elif 96 < x < 123:
                x = (x - 84) % 26 + 97
            txt += chr(x)
        for i in lut:
            txt = re.sub(i, '', txt)
        ct = base64.b64decode(txt).decode('utf-8')
        txt = ''.join([chr(ord(i) - 3) for i in ct])
        txt = base64.b64decode(txt[::-1]).decode('utf-8')
        return json.loads(txt)





async def test_voe():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        results = await voe("https://crystaltreatmenteast.com/wnnov1m62xzy",{'streams': []},'ToonItalia','1','[https:idk.com,a]',{},'',client)
        print(results)
if __name__ == "__main__":
    import asyncio
    asyncio.run(test_voe()) 
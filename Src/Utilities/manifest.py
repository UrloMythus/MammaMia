
from fastapi import APIRouter, HTTPException, Response, Request
from fastapi.responses import RedirectResponse
from curl_cffi.requests import AsyncSession
from urllib.parse import urlparse, parse_qs,unquote,quote
from base64 import b64decode,b64encode
import re
from Src.API.extractors.vidxgo import vidxgo_refresh
import time
import  Src.Utilities.config as config
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)
 

VD_DOMAIN = config.VD_DOMAIN
router = APIRouter()
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:150.0) Gecko/20100101 Firefox/150.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': f'{VD_DOMAIN}/',
    'Origin': VD_DOMAIN,
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'DNT': '1',
}
async def fetch_m3u8(url):
    """Fetch the M3U8 file from the URL and store it in memory."""
    async with AsyncSession() as client:
        response = await client.get(url,headers = headers)
        return response.text,response.status_code

@router.get("/clone/manifest.m3u8")
async def clone_m3u8(d: str = None):
    if d:
        try:
            url = b64decode(d).decode('utf-8')
            m3u8_content,status = await fetch_m3u8(url)
            if status != 200:
                match = re.search(r'hls[\w/]*/(\d{2}\d*[/]*\d*[/]*\d*)[\w/]+master',url)
                if match:
                    id = match.group(1)
                    url = await vidxgo_refresh("",id)

                    m3u8_content,status =await fetch_m3u8(url)
            m3u8_content = re.sub(r'(&b=\d+)',rf'\1&base={d}',m3u8_content)

            return Response(content=m3u8_content, media_type='application/vnd.apple.mpegurl')
        except Exception as e:
            logger.info(f"Failed to fetch M3U8 file: {e}")
            raise HTTPException(status_code=404, detail="M3U8 content not found")

@router.get("/clone/index{suffix}")
async def index_route(suffix: str, base: str):
    try:
        text2 = b64decode(base).decode('utf-8')
        text = text2.replace("master.m3u8",f'index{suffix}')

        m3u8_content,status = await fetch_m3u8(text)
        match = re.search(r'hls[\w/]*/(\d{2}\d*[/]*\d*[/]*\d*)[\w/]+master',text2)
        if match:
                id = match.group(1)
        else:
            raise HTTPException(status_code=502, detail="ID  not found")  
        if status != 200:
            text = await vidxgo_refresh("",id)
            text = text.replace("master.m3u8",f'index{suffix}')
            m3u8_content,status =await fetch_m3u8(text)

        current_date = time.strftime('%Y-%m-%d %H:%M')
        m3u8_content = re.sub(r'(b=\d+)', rf'\1&id={b64encode(id.encode("utf-8")).decode("utf-8")}&date={b64encode(current_date.encode("utf-8")).decode("utf-8")}', m3u8_content)
        return Response(content=m3u8_content, media_type='application/vnd.apple.mpegurl')
    except Exception as e:
        logger.info(f"Failed to fetch M3U8 file: {e}")
        raise HTTPException(status_code=502, detail="M3U8 content not found")   


@router.get("/clone/seg{suffix}")
async def ts_route(suffix:str,id:str,date: str,t:str,e:str,b:str):
    try:
        url = await vidxgo_refresh("",b64decode(id).decode('utf-8'))
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        url = url.split("?")[0]
        text = url.replace("master.m3u8",f'seg{suffix}?t={params["t"][0]}&e={params["e"][0]}&b={b}')
        return RedirectResponse(text,headers=headers)
    except Exception as e:
        logger.info(f"Failed to redirect TS file: {e}")
        raise HTTPException(status_code=502, detail="Failed to redirect TS file")

async def test_fetch():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        results = await index_route('-v1-a1','aHR0cHM6Ly9jZG4udjMubWVkaWEtNjg0LmQyYi55b3UvcHJveHkvbWVkaWEtNDAyL2hscy8xNjQyNjQxOC9tYXN0ZXIubTN1OD90PTJiYjg0MGYwMzFjY2MzNmYmZT0xNzgwNTA2OTk2Njk5JmI9Mjk3Ng====')
        print(results)

        
if __name__ == "__main__":
    import asyncio
    asyncio.run(test_fetch()) 
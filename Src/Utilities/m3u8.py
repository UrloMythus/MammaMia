from urllib.parse import urlparse, parse_qs,unquote,quote
from fastapi import APIRouter, HTTPException, Response
from curl_cffi.requests import AsyncSession

router = APIRouter()
User_Agent= "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0"
async def fetch_m3u8(url):
    """Fetch the M3U8 file from the URL and store it in memory."""
    async with AsyncSession() as client:
        response = await client.get(url,headers = {"User-Agent": User_Agent, "user-agent": User_Agent})
        response.raise_for_status()  # Raise an error for bad responses
        return response.text

@router.get("/clone/manifest.m3u8")
async def clone_m3u8(d: str = None):
    if d:
        try:
            d = unquote(d)
            m3u8_content = await fetch_m3u8(d)
            return Response(content=m3u8_content, media_type='application/vnd.apple.mpegurl')
        except Exception as e:
            print(f"Failed to fetch M3U8 file: {e}")
            raise HTTPException(status_code=404, detail="M3U8 content not found")
#This is just for testing, ignore that endpoint and the func


@router.api_route("/vixcloud/manifest.m3u8", methods=["GET", "HEAD"])
async def clone2_m3u8(d:str,token:str,expires:str,h:str = None, b:str = None):
    try:
        m3u8 = f'{d}?token={token}&expires={expires}'
        if h:
            m3u8 = m3u8 + f'&h={h}'
        if b:
            m3u8 = m3u8 + f'&b={b}'
        
        m3u8_content = await fetch_m3u8(m3u8)
        return Response(content=m3u8_content, media_type='application/vnd.apple.mpegurl')
    except Exception as e:
        print(f"Failed to fetch M3U8 file: {e}")
        raise HTTPException(status_code=404, detail="M3U8 content not found")
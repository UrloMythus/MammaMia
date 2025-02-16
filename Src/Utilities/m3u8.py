from urllib.parse import urlparse, parse_qs,unquote,quote
from fastapi import APIRouter, HTTPException, Response, Request
from curl_cffi.requests import AsyncSession
import Src.Utilities.config as config
from Src.Utilities.loadenv import load_env  
env_vars = load_env()
SC_PROXY = config.SC_PROXY
VX_PROXY = config.VX_PROXY
import json        
import re

import random
proxies = {}
proxies2 = {}
if VX_PROXY == "1":
    PROXY_CREDENTIALS = env_vars.get('PROXY_CREDENTIALS')
    proxy_list = json.loads(PROXY_CREDENTIALS)
    proxy = random.choice(proxy_list)
    if proxy == "":
        proxies2 = {}
    else:
        proxies2 = {
            "http": proxy,
            "https": proxy
        }      
if SC_PROXY == "1":
    PROXY_CREDENTIALS = env_vars.get('PROXY_CREDENTIALS')
    proxy_list = json.loads(PROXY_CREDENTIALS)
    proxy = random.choice(proxy_list)
    if proxy == "":
        proxies = {}
    else:
        proxies = {
            "http": proxy,
            "https": proxy
        }   
    if VX_PROXY == "1":
        proxies2 = proxies
SC_ForwardProxy = config.SC_ForwardProxy
VX_ForwardProxy = config.VX_ForwardProxy
if SC_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
else:
    ForwardProxy = ""

if VX_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
else:
    ForwardProxy = ""


router = APIRouter()
User_Agent= "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0"
async def fetch_m3u8(url):
    """Fetch the M3U8 file from the URL and store it in memory."""
    async with AsyncSession() as client:
        response = await client.get(ForwardProxy + url,headers = {"User-Agent": User_Agent, "user-agent": User_Agent}, proxies = proxies2)
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
async def clone2_m3u8(d:str,token:str,expires:str,h:str = None, b:str = None, request: Request = None):
    try:
        m3u8 = f'{d}?token={token}&expires={expires}'
        if h:
            m3u8 = m3u8 + f'&h={h}'
        if b:
            m3u8 = m3u8 + f'&b={b}'
        forwarded_proto = request.headers.get("x-forwarded-proto")
        scheme = forwarded_proto if forwarded_proto else request.url.scheme
        instance_url = f"{scheme}://{request.url.netloc}"
        m3u8_content = await fetch_m3u8(m3u8)
        modified_playlist = m3u8_content.replace("https://vixcloud.co/playlist/", f"{instance_url}/clony/")

        return Response(content=modified_playlist, media_type='application/vnd.apple.mpegurl')
    except Exception as e:
        print(f"Failed to fetch M3U8 file: {e}")
        raise HTTPException(status_code=404, detail="M3U8 content not found")
    
@router.api_route("/clony/{segment:path}", methods=["GET", "HEAD"])
async def clony_m3u8(segment: str, request: Request):
    base_url = "https://vixcloud.co/playlist/"
    full_url = f"{base_url}{segment}?{request.query_params}"
    print(full_url, "A",request.query_params)
    if "rendition=1080p" in full_url or "type=subtitle" in full_url:
        print(full_url)
        raise HTTPException(status_code=404, detail="Requested variant not available.")
    m3u8_content = await fetch_m3u8(full_url)
    if "sc-u12" not  in m3u8_content:
        m3u8_content = re.sub(r"https://sc-[a-zA-Z0-9]+-\d+.scws-content.net", "https://sc-u12-01.scws-content.net", m3u8_content)
    return Response(content=m3u8_content, media_type='application/vnd.apple.mpegurl')
 
@router.api_route('/storage/enc.key')
async def get_key():
    async with AsyncSession(timeout = 20) as client:
        response = await client.get(ForwardProxy + 'https://vixcloud.co/storage/enc.key', headers = {"User-Agent": User_Agent, "user-agent": User_Agent}, proxies = proxies2)
    
    response_headers = {
        'date': response.headers['date'],
        'content-length': response.headers['content-length'],
        'content-type': 'application/octet-stream',
        'access-control-allow-origin': '*'
    }
    
    return Response(
        response.content,
        response.status_code,
        response_headers
    )
#r"https://sc-b1-([0-2][0-9]|30).scws-content.net", "https://sc-u9-01.scws-content.net", m3u8_content)


'''
                            forwarded_proto = request.headers.get("x-forwarded-proto")
                            scheme = forwarded_proto if forwarded_proto else request.url.scheme
                            instance_url = f"{scheme}://{request.url.netloc}"
                            url_streaming_community = url_streaming_community.replace("?","&")
                            url_streaming_community = instance_url + "/vixcloud/manifest.m3u8?d=" + url_streaming_community
'''
import logging
import Src.Utilities.config as config
from Src.Utilities.config import setup_logging
import urllib.parse 

level = config.LEVEL
logger = setup_logging(level)

async def transform_mfp(mfp_stream_url,client):
    try:
        response = await client.get(mfp_stream_url)
        data = response.json()
        url = data['mediaflow_proxy_url'] + "?api_password=" + data['query_params']['api_password'] + "&d=" + urllib.parse.quote(data['destination_url'])
        for i in data['request_headers']:
            url += f"&h_{i}={urllib.parse.quote(data['request_headers'][i])}"
        return url
    except Exception as e:
        logger.warning(f"Converting MFP failed {e}")
        return None

async def build_mfp(MFP_CREDENTIALS,url,host,client):
    MFP_url = MFP_CREDENTIALS[0]
    MFP_password = MFP_CREDENTIALS[1]
    url_mfp = f'{MFP_url}/extractor/video?api_password={MFP_password}&d={url}&host={host}&redirect_stream=false'
    #To build pieces together
    url_mfp = await transform_mfp(url_mfp,client)
    return url_mfp
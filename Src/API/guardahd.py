from Src.Utilities.info import  is_movie
from bs4 import BeautifulSoup,SoupStrainer
import re
import Src.Utilities.config as config
from fake_headers import Headers  
from Src.Utilities.loadenv import load_env  
from Src.Utilities.eval import eval_solver
import json, random
env_vars = load_env()
GH_PROXY = config.GH_PROXY
proxies = {}
if GH_PROXY == "1":
    try:
        PROXY_CREDENTIALS = env_vars.get('PROXY_CREDENTIALS')
        if PROXY_CREDENTIALS:
            proxy_list = json.loads(PROXY_CREDENTIALS)
            if proxy_list and len(proxy_list) > 0:
                proxy = random.choice(proxy_list)
                if proxy and proxy.strip() != "":
                    proxies = {
                        "http": proxy,
                        "https": proxy
                    }
                    print(f"GuardaHD: Using proxy: {proxy}")
                else:
                    print("GuardaHD: Empty proxy selected, using direct connection")
            else:
                print("GuardaHD: No proxies available in PROXY_CREDENTIALS")
        else:
            print("GuardaHD: PROXY_CREDENTIALS not found in environment")
    except (json.JSONDecodeError, Exception) as e:
        print(f"GuardaHD: Error parsing proxy credentials: {e}")
        proxies = {}

GH_ForwardProxy = config.GH_ForwardProxy
if GH_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy', "")
    if ForwardProxy:
        print(f"GuardaHD: Using ForwardProxy: {ForwardProxy}")
    else:
        print("GuardaHD: ForwardProxy enabled but not configured")
else:
    ForwardProxy = ""
#Get domain

GHD_DOMAIN = config.GHD_DOMAIN

random_headers = Headers()


async def get_supervideo_link(link,client):
    headers = random_headers.generate()
    response = await client.get(ForwardProxy + link, headers=headers, allow_redirects=True,timeout = 30, proxies = proxies)
    s2 = re.search(r"\}\('(.+)',.+,'(.+)'\.split", response.text).group(2)
    terms = s2.split("|")
    file_index = terms.index('file')
    #I start to loop from file cause hfs it's one or two position after it usually.

    for i in range(file_index,len(terms)):
        if "hfs" in terms[i]:
            hfs = terms[i]
            break
    urlset_index = terms.index('urlset')
    hls_index = terms.index('hls')
    result = terms[urlset_index + 1 : hls_index]
    #If the len is >1 then you have to merge the elements from the last to the first
    reversed_elements = result[::-1]
    base_url =f"https://{hfs}.serversicuro.cc/hls/"
    if len(reversed_elements) == 1:
        final_url = base_url + "," + reversed_elements[0] + ".urlset/master.m3u8"
    lenght = len(reversed_elements)
    i = 1    
    for element in reversed_elements:
        base_url += element + ","
        if lenght == i:
            base_url += ".urlset/master.m3u8"
        else:
            i += 1
    final_url = base_url
    return final_url

async def search(clean_id,client):
    # Try multiple domain options in case of issues
    domains_to_try = [
        GHD_DOMAIN,
        "https://mostraguarda.stream",  # Fallback 1
        "https://guardahd.stream"       # Fallback 2
    ]
    
    # Remove duplicates while preserving order
    seen = set()
    domains_to_try = [x for x in domains_to_try if not (x in seen or seen.add(x))]
    
    # Try different user agents for 403 issues
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ]
    
    for domain in domains_to_try:
        urls_to_try = []
        
        # Add ForwardProxy URL if configured
        if ForwardProxy:
            urls_to_try.append(ForwardProxy + f"{domain}/set-movie-a/{clean_id}")
        
        # Add direct URL
        urls_to_try.append(f"{domain}/set-movie-a/{clean_id}")
        
        for url in urls_to_try:
            # Try different user agents for 403 issues
            for user_agent in user_agents:
                try:
                    # Try with proxies first, then without if it fails
                    proxy_configs = [proxies, {}] if proxies else [{}]
                    
                    for proxy_config in proxy_configs:
                        try:
                            headers = random_headers.generate()
                            headers["User-Agent"] = user_agent
                            
                            response = await client.get(
                                url, 
                                allow_redirects=True, 
                                impersonate="chrome124", 
                                headers=headers, 
                                proxies=proxy_config,
                                timeout=15
                            )
                            
                            if response.status_code == 200:
                                soup = BeautifulSoup(response.text,'lxml',parse_only=SoupStrainer('li'))
                                li_tag = soup.find('li')
                                if li_tag and li_tag.get('data-link'):
                                    href = "https:" + li_tag['data-link']
                                    return href
                            elif response.status_code == 403:
                                # Try next user agent
                                continue
                            else:
                                print(f"GuardaHD search failed with status {response.status_code} for URL: {url}")
                                
                        except Exception as proxy_error:
                            continue
                            
                except Exception as url_error:
                    continue
    
    raise Exception("GuardaHD: All search attempts failed")



async def guardahd(id,client):
    try:
        general = await is_movie(id)
        ismovie = general[0]
        clean_id = general[1]
        if ismovie == 0:
            return None
        supervideo_link = await search(clean_id,client)
        final_url = await eval_solver(supervideo_link,proxies, ForwardProxy, client)
        return final_url
    except Exception as e:
        print("MammaMia: GuardaHD Failed",e)
        return None
    
async def test_script():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        # Replace with actual id, for example 'anime_id:episode' format
        test_id = "tt9218128"  # This is an example ID format
        results = await guardahd(test_id, client)
        print(results)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_script())
    
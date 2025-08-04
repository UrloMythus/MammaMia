import re
from bs4 import BeautifulSoup,SoupStrainer
from Src.Utilities.info import is_movie,get_info_tmdb,get_info_imdb
from Src.Utilities.convert import get_TMDb_id_from_IMDb_id
from fake_headers import Headers
import Src.Utilities.config as config
from Src.Utilities.loadenv import load_env
CB_DOMAIN = config.CB_DOMAIN
CB_PROXY = config.CB_PROXY
MX_PROXY = config.MX_PROXY
proxies = {}
proxies2 = {}
env_vars = load_env()
import random
import json
if MX_PROXY == "1":
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
if CB_PROXY == "1":
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
        proxies2 = proxies
 
CB_ForwardProxy = config.CB_ForwardProxy
MX_ForwardProxy = config.MX_ForwardProxy
if CB_ForwardProxy == "1":
    ForwardProxy = env_vars.get('ForwardProxy')
    ForwardProxy2 = ForwardProxy
    if MX_ForwardProxy == "1":
        ForwardProxy2 = ForwardProxy
elif MX_ForwardProxy == "1":
    ForwardProxy2 = env_vars.get('ForwardProxy')
else:
    ForwardProxy2 = ""
    ForwardProxy = ""


fake_headers = Headers()

async def get_stayonline(link,client):
    headers = {
                    'origin': 'https://stayonline.pro',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0',
                    'x-requested-with': 'XMLHttpRequest',
                }
    data = {'id': link.split("/")[-2], 'ref': ''}
    response = await client.post('https://stayonline.pro/ajax/linkEmbedView.php', headers=headers, data=data, proxies = proxies2)
    real_url = response.json()['data']['value']
    return real_url


async def get_uprot(link,client):
        try:
            if "msf" in link:
                 link = link.replace("msf","mse")    
            headers = fake_headers.generate()
            response = await client.get(ForwardProxy2 + link, headers=headers, allow_redirects=True, timeout=10, proxies=proxies2, impersonate = "chrome124")
            soup = BeautifulSoup(response.text, "lxml")
            
            # Look for specific patterns that indicate streaming links
            streaming_patterns = [
                r'https://[^"\s]*maxstream[^"\s]*',
                r'https://[^"\s]*\.host-cdn\.net[^"\s]*',
                r'https://[^"\s]*streaming[^"\s]*',
                r'href=["\']([^"\']*maxstream[^"\']*)["\']',
                r'href=["\']([^"\']*\.host-cdn\.net[^"\']*)["\']'
            ]
            
            # First try regex patterns on the raw HTML
            for pattern in streaming_patterns:
                matches = re.findall(pattern, response.text, re.IGNORECASE)
                if matches:
                    for match in matches:
                        if isinstance(match, tuple):
                            match = match[0] if match[0] else match[1]
                        if match and ('maxstream' in match.lower() or 'host-cdn' in match.lower()):
                            return match
            
            # Try to find links in specific containers or with specific attributes
            all_links = soup.find_all("a", href=True)
            for link_tag in all_links:
                href = link_tag.get("href")
                if href and any(keyword in href.lower() for keyword in ['maxstream', 'host-cdn', 'streaming']):
                    return href
            
            # Look for iframe sources that might contain the streaming link
            iframes = soup.find_all("iframe")
            for iframe in iframes:
                src = iframe.get("src")
                if src and any(keyword in src.lower() for keyword in ['maxstream', 'host-cdn', 'streaming']):
                    return src
            
            # Look for data attributes that might contain links
            elements_with_data = soup.find_all(attrs={"data-src": True})
            for element in elements_with_data:
                data_src = element.get("data-src")
                if data_src and any(keyword in data_src.lower() for keyword in ['maxstream', 'host-cdn', 'streaming']):
                    return data_src
            
            # Look for any form actions or button onclick events
            forms = soup.find_all("form")
            for form in forms:
                action = form.get("action")
                if action and any(keyword in action.lower() for keyword in ['maxstream', 'host-cdn', 'streaming']):
                    return action
            
            # Look for JavaScript variables that might contain the link
            script_tags = soup.find_all("script")
            for script in script_tags:
                if script.string:
                    # Look for URL patterns in JavaScript
                    js_patterns = [
                        r'["\']https://[^"\']*maxstream[^"\']*["\']',
                        r'["\']https://[^"\']*\.host-cdn\.net[^"\']*["\']',
                        r'url\s*[:=]\s*["\']([^"\']*)["\']',
                        r'src\s*[:=]\s*["\']([^"\']*)["\']'
                    ]
                    
                    for pattern in js_patterns:
                        matches = re.findall(pattern, script.string, re.IGNORECASE)
                        for match in matches:
                            # Clean up the match (remove quotes)
                            clean_match = match.strip('"\'')
                            if clean_match and any(keyword in clean_match.lower() for keyword in ['maxstream', 'host-cdn', 'streaming']):
                                return clean_match
            
            # If no specific streaming links found, try the first valid HTTP link as fallback
            for link_tag in all_links:
                href = link_tag.get("href")
                if href and href.startswith(('http://', 'https://')):
                    return href
            
            return None
        except Exception as e:
            return None

async def get_true_link_mixdrop(real_link,client,MFP):
    try:
        import string
        
        if "club" in real_link:
            real_link = real_link.replace("club","ps").split('/2')[0] 

        headers = fake_headers.generate()
        response = await client.get(real_link, headers=headers, allow_redirects=True, timeout=30, impersonate="chrome124")
        
        # Try multiple patterns for Mixdrop decoding
        patterns = [
            r"\}\('(.+)',.+,'(.+)'\.split",
            r"eval\(function\(p,a,c,k,e,d\)\{.*?\}\('(.+)',.+,'(.+)'\.split",
            r"return p\}\('(.+)',.+,'(.+)'\.split"
        ]
        
        match = None
        for pattern in patterns:
            match = re.search(pattern, response.text)
            if match:
                break
        
        if not match:
            # Try to find direct video links in the page
            video_patterns = [
                r'"(https://[^"]*\.mp4[^"]*)"',
                r"'(https://[^']*\.mp4[^']*)'",
                r'src="([^"]*\.mp4[^"]*)"',
                r"file:\s*['\"]([^'\"]*\.mp4[^'\"]*)['\"]"
            ]
            
            for video_pattern in video_patterns:
                video_match = re.search(video_pattern, response.text)
                if video_match:
                    direct_url = video_match.group(1)
                    return direct_url
            
            return None
            
        [s1, s2] = match.group(1, 2)
        
        # Improved Mixdrop decoding algorithm
        terms = s2.split("|")
        
        # Create substitution dictionary with better logic
        charset = string.digits + string.ascii_letters
        d = {}
        
        # Build the dictionary more carefully
        for i in range(len(terms)):
            if i < len(charset):
                # Only use non-empty terms for substitution
                if terms[i]:
                    d[charset[i]] = terms[i]
                else:
                    d[charset[i]] = charset[i]  # Keep original character if term is empty
        
        # Also create mappings for two-digit numbers (10, 11, 12, etc.)
        # This is crucial for proper Mixdrop decoding
        for i in range(len(terms)):
            if i >= 10:  # For indices 10 and above
                d[str(i)] = terms[i] if terms[i] else str(i)
        
        # Find the encoded URL in s1
        encoded_url = None
        
        # Method 1: Look for return statement with various patterns
        return_patterns = [
            r'return\s*["\']([^"\']+)["\']',
            r'return\s*([^;]+)',
            r'return\s*\+?\s*["\']([^"\']+)["\']'
        ]
        
        for pattern in return_patterns:
            return_match = re.search(pattern, s1)
            if return_match:
                encoded_url = return_match.group(1).strip().strip('"\'')
                break
        
        if not encoded_url:
            # Method 2: Look for the last string in s1
            parts = s1.split(';')
            for part in reversed(parts):
                if 'return' in part:
                    # Extract the part after return
                    return_part = part.split('return')[-1].strip()
                    # Remove quotes and extra characters
                    encoded_url = re.sub(r'["\'\s\(\)]', '', return_part)
                    if encoded_url:
                        break
        
        if not encoded_url:
            # Method 3: Try to find the schema in a different way
            if len(s1.split(";")) >= 3:
                schema_part = s1.split(";")[2]
                # Look for the encoded string
                schema_match = re.search(r'["\']([^"\']+)["\']', schema_part)
                if schema_match:
                    encoded_url = schema_match.group(1)
        
        if not encoded_url:
            return None
        
        # Improved decoding algorithm that handles multi-digit numbers
        decoded_url = ""
        i = 0
        
        while i < len(encoded_url):
            char = encoded_url[i]
            
            # Try to find the longest matching key starting from current position
            best_match = None
            best_replacement = None
            
            # Check for multi-character keys (numbers like 10, 11, 12, etc.)
            for key_len in range(3, 0, -1):  # Try 3, 2, 1 character keys
                if i + key_len <= len(encoded_url):
                    potential_key = encoded_url[i:i+key_len]
                    if potential_key in d:
                        best_match = potential_key
                        best_replacement = d[potential_key]
                        break
            
            if best_match:
                decoded_url += best_replacement
                i += len(best_match)
            else:
                decoded_url += char
                i += 1
        
        # Ensure proper URL format
        if not decoded_url.startswith('http'):
            if decoded_url.startswith('//'):
                decoded_url = 'https:' + decoded_url
            else:
                decoded_url = 'https://' + decoded_url
        
        # Comprehensive URL fixing
        if decoded_url.startswith('https:///'):
            decoded_url = 'https://' + decoded_url[8:]
        elif decoded_url.startswith('http:///'):
            decoded_url = 'http://' + decoded_url[7:]
        elif decoded_url.startswith('https:/') and not decoded_url.startswith('https://'):
            decoded_url = 'https://' + decoded_url[7:]
        elif decoded_url.startswith('http:/') and not decoded_url.startswith('http://'):
            decoded_url = 'http://' + decoded_url[6:]
        
        # Handle any remaining multiple slashes in the path
        if '://' in decoded_url:
            protocol_part, path_part = decoded_url.split('://', 1)
            while '///' in path_part:
                path_part = path_part.replace('///', '//')
            decoded_url = protocol_part + '://' + path_part
        
        # Validate the URL format
        if not decoded_url.startswith('https://') or '.mp4' not in decoded_url:
            return None
        
        # If MFP is enabled, return the original Mixdrop link for proxy processing
        if MFP == "1":
            return real_link
            
        return decoded_url
    except Exception as e:
        return None

async def get_true_link_maxstream(maxstream_url,client):
        try:
            headers = fake_headers.generate()    
            response = await client.get(ForwardProxy2 + maxstream_url, headers=headers, allow_redirects=True, timeout=10,proxies = proxies2, impersonate = "chrome124")
            
            match = re.search(r"\}\('(.+)',.+,'(.+)'\.split", response.text)
            if not match:
                return None
                
            [s1, s2] = match.group(1, 2)
            terms = s2.split("|")
            
            if 'urlset' not in terms or 'hls' not in terms or 'sources' not in terms:
                return None
                
            urlset_index = terms.index('urlset')
            hls_index = terms.index('hls')
            sources_index =  terms.index('sources')
            result = terms[urlset_index + 1 : hls_index]
            reversed_elements = result[::-1]
            first_part = terms[hls_index +1 : sources_index]
            reversed_first_part = first_part[::-1]
            first_url_part = ""
            for first_part in reversed_first_part:
                    if "0" in first_part:
                            first_url_part += first_part
                    else:
                            first_url_part += first_part + "-"  
            

            base_url = f"https://{first_url_part}.host-cdn.net/hls/" 
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
        except Exception as e:
            return None

async def search_movie(showname,date,client):
    try:
        showname = showname.replace(" ","+").replace("ò","o").replace("è","e").replace("à","a").replace("ù","u").replace("ì","i")  
        headers = fake_headers.generate()
        headers['Referer'] = f'{CB_DOMAIN}/'
        query = f'{CB_DOMAIN}/?s={showname}'
        response = await client.get(ForwardProxy + query,headers=headers, impersonate = "chrome124", proxies = proxies)
        if response.status_code != 200:
            return None
        soup = BeautifulSoup(response.text, 'lxml',parse_only=SoupStrainer('div', class_='card-content'))
        cards = soup.find_all('div', class_='card-content')
        year_pattern = re.compile(r'(19|20)\d{2}')
        for card in cards:
            link_tag = card.find('h3', class_='card-title').find('a')
            href = link_tag['href']
            date_text = href.split("/")[-2]
            match = year_pattern.search(date_text)
            if match:
                year = match.group(0)
                if year == date:
                    return href
    except Exception as e:
        return None


async def search_series(showname,date,client):
    try:
        showname = showname.replace(" ","+")
        headers = fake_headers.generate()
        headers['Referer'] = f'{CB_DOMAIN}/serietv/'
        query = f'{CB_DOMAIN}/serietv/?s={showname}'
        response = await client.get(ForwardProxy + query,headers=headers,impersonate = "chrome124", proxies = proxies)
        if response.status_code != 200:
            return None
        soup = BeautifulSoup(response.text, 'lxml',parse_only=SoupStrainer('div', class_='card-content'))
        cards = soup.find_all('div', class_='card-content')
        year_pattern = re.compile(r'(19|20)\d{2}')
        for card in cards:
            link_tag = card.find('h3', class_='card-title').find('a')
            href = link_tag['href']
            date_span = card.find('span', style=re.compile('color'))
            if date_span:
                date_text = date_span.text
                match = year_pattern.search(date_text)
                if match:
                    year = match.group(0)
                    if year == date:
                        return href
    except Exception as e:
        return None

async def movie_redirect_url(link,client,MFP):
        try:
            headers = fake_headers.generate()
            response = await client.get(ForwardProxy + link, headers=headers, allow_redirects=True, timeout=10, impersonate = "chrome124", proxies = proxies)
            soup = BeautifulSoup(response.text, "lxml",parse_only=SoupStrainer('div'))
            
            # Check if iframen2 exists
            iframe2 = soup.find("div", id="iframen2")
            if iframe2 and iframe2.get("data-src"):
                redirect_url = iframe2.get("data-src")
                if "stayonline" in redirect_url:
                    mixdrop_real_link = await get_stayonline(redirect_url,client)
                    final_url = await get_true_link_mixdrop(mixdrop_real_link,client,MFP)
                    if final_url != None:
                        return final_url
            
            # Try iframen1 as fallback
            iframe1 = soup.find("div", id="iframen1")
            if iframe1 and iframe1.get("data-src"):
                redirect_url = iframe1.get("data-src")
                if "stayonline" in redirect_url:
                    redirect_url = await get_stayonline(redirect_url,client)
                maxstream_real_link = await get_uprot(redirect_url,client)
                final_url = await get_true_link_maxstream(maxstream_real_link,client) 
                return final_url
            
            return None
            
        except Exception as e:
            return None

async def series_redirect_url(link,season,episode,client,MFP):
        if len(episode) == 1:
                        episode = f'0{episode}'
        headers = fake_headers.generate()
        response = await client.get(ForwardProxy + link, headers=headers, allow_redirects=True, timeout=10,impersonate = "chrome124", proxies = proxies)
        soup = BeautifulSoup(response.text, "lxml")     
        seasons_text = soup.find_all('div', class_='sp-head')
        for season_text in seasons_text:
            text = season_text.text
            if f'STAGIONE' in text and f'{season}' in text:
                text = text.replace("STAGIONE","").replace("ITA", "")
                if "A" in text:
                    if len(season) == 1:
                        season = f'0{season}'
                    sp_body = season_text.find_next('div', class_='sp-body')
                    link_tag = sp_body.find('a')
                    uprot_long = link_tag.get('href')
                    response = await client.get(ForwardProxy + uprot_long, headers=headers, allow_redirects=True, timeout=10, impersonate = "chrome124", proxies = proxies)
                    
                    season_formatted = season.zfill(2)
                    episode_formatted = episode.zfill(2)
                    
                    # Try multiple patterns to find the episode link
                    patterns = [
                        rf"(?i)\S*?\.{season_formatted}x{episode_formatted}\S*?\.mkv.*?href=['\"](.*?)['\"]",
                        rf"(?i)\S*\.S{season_formatted}E{episode_formatted}\S*?\.mkv.*?href=['\"](.*?)['\"]",
                        rf"(?i)\S*\.S{season_formatted}E{episode_formatted}\S*?\.mp4.*?href=['\"](.*?)['\"]",
                        rf"(?i)\S*\.S{season_formatted}E{episode_formatted}\S*?\.avi.*?href=['\"](.*?)['\"]",
                        rf"(?i){season_formatted}x{episode_formatted}.*?href=['\"](.*?)['\"]",
                        rf"(?i)S{season_formatted}E{episode_formatted}.*?href=['\"](.*?)['\"]"
                    ]
                    
                    maxstream_link = None
                    for pattern in patterns:
                        match = re.search(pattern, response.text)
                        if match:
                            maxstream_link = match.group(1)
                            break
                    
                    if not maxstream_link:
                        return None
                    if "stayonline" in maxstream_link:
                            maxstream_link =await get_stayonline(maxstream_link,client)
                    maxstream_real_link = await get_uprot(maxstream_link,client)
                    final_url = await get_true_link_maxstream(maxstream_real_link,client)
                    return final_url
                else:
                    season_formatted = season.zfill(2)
                    episode_formatted = episode.zfill(2)
                    
                    # Create dynamic pattern based on actual season and episode
                    episode_pattern = f'{season_formatted}&#215;{episode_formatted}'
                    pattern = re.compile(rf'{episode_pattern}\s*&#8211;.*?<a href="(.*?)".*?>Maxstream</a>\s*&#8211;.*?<a href="(.*?)".*?>Mixdrop</a>', re.DOTALL)
                    match = pattern.search(response.text)
                    
                    if not match:
                        # Try alternative patterns
                        alt_patterns = [
                            rf'{season_formatted}x{episode_formatted}\s*&#8211;.*?<a href="(.*?)".*?>Maxstream</a>\s*&#8211;.*?<a href="(.*?)".*?>Mixdrop</a>',
                            rf'S{season_formatted}E{episode_formatted}\s*&#8211;.*?<a href="(.*?)".*?>Maxstream</a>\s*&#8211;.*?<a href="(.*?)".*?>Mixdrop</a>',
                            rf'{season}x{episode}\s*&#8211;.*?<a href="(.*?)".*?>Maxstream</a>\s*&#8211;.*?<a href="(.*?)".*?>Mixdrop</a>'
                        ]
                        
                        for alt_pattern in alt_patterns:
                            alt_match = re.search(alt_pattern, response.text, re.DOTALL)
                            if alt_match:
                                match = alt_match
                                break
                    
                    if not match:
                        return None
                    
                    maxstream_link = match.group(1)
                    mixdrop_link = match.group(2)
                    mixdrop_real_link = await get_stayonline(mixdrop_link,client)
                    final_url = await get_true_link_mixdrop(mixdrop_real_link,client,MFP)
                    if final_url == None:
                        if "stayonline" in maxstream_link:
                            maxstream_link =await get_stayonline(maxstream_link,client)
                        maxstream_real_link = await get_uprot(maxstream_link,client)
                        final_url = await get_true_link_maxstream(maxstream_real_link,client)                        
                        return final_url


async def cb01(id,client,MFP):
    try:
        general = await is_movie(id)
        ismovie = general[0]
        real_id = general[1]
        type = "Cb01"
        if "tt" in id:
            info_result = await get_info_imdb(real_id,ismovie,type,client)
        elif  "tmdb" in real_id:
            info_result = get_info_tmdb(real_id,ismovie,type)
        else:
            return None
        
        if not info_result or len(info_result) < 2:
            return None
        
        showname, date = info_result
        
        if not showname or not date:
            return None
        if ismovie == 0:
            season = general[2]
            episode = general[3]
            link = await search_series(showname,date,client)
            final_url = await series_redirect_url(link,season,episode,client,MFP)
            return final_url
        elif ismovie == 1:
            season = None
            episode = None
            link = await search_movie(showname,date,client)
            redirect_url = await movie_redirect_url(link,client,MFP)
            return redirect_url
    except Exception as e:
        return None
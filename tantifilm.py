import requests
from bs4 import BeautifulSoup,SoupStrainer
import re
import time
from info import is_movie,get_info_imdb,get_info_tmdb
import config
from loadenv import load_env
TF_FAST_SEARCH = config.TF_FAST_SEARCH
TF_DOMAIN = config.TF_DOMAIN
HF = config.HF
env_vars = load_env()
PROXY_CREDENTIALS = env_vars.get('PROXY_CREDENTIALS')


async def search(showname,ismovie,date,client):
    url = f'https://www.tanti.{TF_DOMAIN}/search/{showname}'
    response =  await client.get(url, follow_redirects=True)
    soup = BeautifulSoup(response.text, "lxml")
    if ismovie == 1:
        all_link = soup.select('#movies .col .list-media')
        for link in all_link:
            url = link['href']
            response = client.get(url, follow_redirects=True)
            pattern = r'Data di rilascio\s*</div>\s*<div class="text">\s*(\d{4})\s*</div>'
            found_date = re.search(pattern, response.text)
            release_date = str(found_date.group(1))
            if release_date == date:
                tid= url.split('-')[-1]
                #Return URL and even the soup so I can use it later
                #I try to get doodstream link inside this function so I do not have to get again the response
                return tid,url
    elif ismovie == 0: 
        all_link = soup.select('#series .col .list-media')
        for link in all_link:
            base_url = link['href']
            url = f'{base_url}-1-season-1-episode'
            response = await client.get(url, follow_redirects=True)
            pattern = r'Data di rilascio\s*</div>\s*<div class="text">\s*(\d{4})\s*</div>'
            found_date = re.search(pattern, response.text)
            release_date = str(found_date.group(1))
            if release_date == date:
                tid= url.split('-')[1]
                soup = BeautifulSoup(response.text, 'lxml')
                a_tag = soup.find('a', class_='dropdown-toggle btn-service selected')
                embed_id = a_tag['data-embed']
                #I try to get doodstream link inside this function so I do not have to get again the response
                return url,embed_id
            
async def fast_search(showname,ismovie,client):
    url = f'https://www.tanti.{TF_DOMAIN}/search/{showname}'
    response = await client.get(url, follow_redirects=True)
    soup = BeautifulSoup(response.text, "lxml")
    if ismovie == 1:
        first_link = soup.select_one('#movies .col .list-media')
        url = first_link['href']
        tid= url.split('-')[1]
        return tid,url
    elif ismovie == 0: 
        first_link = soup.select_one('#series .col .list-media')
        base_url = first_link['href']
        url = f'{base_url}-1-season-1-episode'
        response = await client.get(url, follow_redirects=True)
        soup = BeautifulSoup(response.text, 'lxml')
        a_tag = soup.find('a', class_='dropdown-toggle btn-service selected')
        embed_id = a_tag['data-embed']
        return url,embed_id



async def get_protect_link(id,url,client):
        #Get the link where the Iframe is located, which contains the doodstream url kind of. 
        response = await client.get(f"https://p.hdplayer.casa/myadmin/play.php?id={id}", follow_redirects=True)
        soup = BeautifulSoup(response.text, "lxml", parse_only=SoupStrainer('iframe'))
        protect_link = soup.iframe['src'] 
        if "protect" in protect_link:
            return  protect_link
        else:
            #DO this in case the movie has  a 3D version etc
            response = await client.get(url, follow_redirects=True)
            soup = BeautifulSoup(response.text, 'lxml')
            a_tag = soup.find('a', class_='dropdown-toggle btn-service selected')
            embed_id = a_tag['data-embed']
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'Referer': url
            }
            #Parameters needed is the embed ID
            data = {
            'id': embed_id
            }
            ajax_url = f"https://www.tanti.{TF_DOMAIN}/ajax/embed"
            response = await client.post(ajax_url, headers=headers, data=data)
            hdplayer = response.text[43:-27]
            response = await client.get(hdplayer, follow_redirects=True)
            soup = BeautifulSoup(response.text, 'lxml')
            links_dict = {}
            li_tags = soup.select('ul.nav.navbar-nav li.dropdown')
            for li_tag in li_tags:
                a_tag = li_tag.find('a')
                if a_tag:
                    title = a_tag.text.strip() 
                    #Since tantifilm player is broken I just skip it
                    if title == "1" or "Tantifilm" in title:
                        continue # Get the text of the <a> tag
                    href = a_tag['href']  
                    response = await client.get(href, follow_redirects=True)
                    soup = BeautifulSoup(response.text, "lxml", parse_only=SoupStrainer('iframe'))
                    protect_link = soup.iframe['src'] 
                    if "protect" in protect_link:
                        url = true_url(protect_link)
                        links_dict[title] = url
            return  links_dict
                         # Get the value of the href attribute
                    

async def get_nuovo_indirizzo_and_protect_link(url,embed_id,season,episode,client):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Referer': url
    }
    #Parameters needed is the embed ID
    data = {
    'id': embed_id
}
    ajax_url = f"https://www.tanti.{TF_DOMAIN}/ajax/embed"
    response = await client.post(ajax_url, headers=headers, data=data)
    nuovo_indirizzo = response.text[43:-27]
    response = await client.get(nuovo_indirizzo, follow_redirects=True)
    soup = BeautifulSoup(response.text, 'lxml')
    #Get season
    season = season - 1
    li_tags = soup.select('ul.nav.navbar-nav > li.dropdown')
    if len(li_tags) != 1:
        link = li_tags[season].find('a')['href']
        response = await client.get(link, follow_redirects=True)
        soup = BeautifulSoup(response.text, 'lxml')
        option_tag = soup.select(f'select[name="ep_select"] > option:nth-of-type({episode})')[0]
        link = option_tag['value']
        #Let's find protect link now
        response = await client.get(link, follow_redirects=True)
        soup = BeautifulSoup(response.text, "lxml", parse_only=SoupStrainer('iframe'))
        protect_link = soup.iframe['src'] 
        return  protect_link

    else:
        #If there is only one season than 
        option_tag = soup.select('select.dynamic_select > option')[episode]
        link = option_tag['value']
        #Let's find protect link now
        response = await client.get(link, follow_redirects=True)
        soup = BeautifulSoup(response.text, "lxml", parse_only=SoupStrainer('iframe'))
        protect_link = soup.iframe['src'] 
        return  protect_link


async def true_url(protect_link,client):
    print(protect_link)
    # Define headers
    headers = {
        "Range": "bytes=0-",
        "Referer": "https://d000d.com/",
    }
    if HF == "1":
        proxy = PROXY_CREDENTIALS
        proxies = {
            "http": proxy,
            "https": proxy
        }
        response = await client.get(protect_link, proxies=proxies, follow_redirects=True)
    else:
        response = await client.get(protect_link, follow_redirects=True)
    link = response.url
 
    
    if response.status_code == 200:
        # Get unique timestamp for the request      
        real_time = str(int(time.time()))

        # Regular Expression Pattern for the match
        pattern = r"(\/pass_md5\/.*?)'.*(\?token=.*?expiry=)"
        
        # Find the match 
        match = re.search(pattern, response.text, re.DOTALL)

        # If a match was found
        if match:
            # Create real link (match[0] includes all matched elements)
            url =f'https://d000d.com{match[1]}'
            print("MD5: ", url)
            rebobo = await client.get(url, headers=headers, follow_redirects=True)
            real_url = f'{rebobo.text}123456789{match[2]}{real_time}'
            print(real_url)
            return real_url
        else:
            print("No match found in the text.")
            return None
  
    print("Error: Could not get the response.")
    return None



#Get temporaly ID
async def tantifilm(imdb,client):
    urls = None
    try:
        general = is_movie(imdb)
        ismovie = general[0]
        imdb_id = general[1]
        type = "Tuttifilm"
        if ismovie == 0 : 
            season = int(general[2])
            episode = int(general[3])
            if "tt" in imdb:
                if TF_FAST_SEARCH == "0":
                    showname,date = await get_info_imdb(imdb_id,ismovie,type,client)
                    url,embed_id = await search(showname,ismovie,date,client)
                elif TF_FAST_SEARCH == "1":
                    showname = await get_info_imdb(imdb_id,ismovie,type,client)
                    url,embed_id = await fast_search(showname,ismovie,client)
            else:
                    #else just equals them
                    tmdba = imdb_id.replace("tmdb:","")
                    if TF_FAST_SEARCH == "0":
                        showname,date = get_info_tmdb(tmdba,ismovie,type)
                        url,embed_id = await search(showname,ismovie,date,client)
                    elif TF_FAST_SEARCH == "1":
                        showname= get_info_tmdb(tmdba,ismovie,type)
                        url,embed_id = await fast_search(showname,ismovie,client)
            protect_link = await get_nuovo_indirizzo_and_protect_link(url,embed_id,season,episode,client)
            url = await true_url(protect_link,client)
            return url
        elif ismovie == 1:
            if "tt" in imdb:
                #Get showname
                    if TF_FAST_SEARCH == "0":
                        showname,date = await get_info_imdb(imdb_id,ismovie,type,client)
                        tid,url = await search(showname,ismovie,date,client)
                    elif TF_FAST_SEARCH == "1":
                        showname = await get_info_imdb(imdb_id,ismovie,type,client)
                        date = None
                        tid,url = await fast_search(showname,ismovie,client)
            else:
            
                #else just equals themtantifilm("tt2096673")

                if TF_FAST_SEARCH == "0":
                    showname,date = get_info_tmdb(imdb,ismovie,type)
                    tid,url = await search(showname,ismovie,date,client)
                elif TF_FAST_SEARCH == "1":
                    showname = get_info_tmdb(imdb,ismovie,type)
                    tid,url = await fast_search(showname,ismovie,client)
            protect_link = await get_protect_link(tid,url,client)
            if not isinstance(protect_link, str):
                urls = protect_link
                if urls:
                    return urls
                else:
                    print("Tantifilm Error v2")
            else:
                url = await true_url(protect_link,client)
                if url:
                    return url

    except Exception as e:
        print("Tantifilm Error: ", e)
        return None 
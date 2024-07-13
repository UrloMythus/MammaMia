import requests
from bs4 import BeautifulSoup,SoupStrainer
import re
import time
from info import is_movie,get_info_imdb,get_info_tmdb
import config
TF_FAST_SEARCH = config.TF_FAST_SEARCH
TF_DOMAIN = config.TF_DOMAIN


##FOR NOW ONLY MOVIES WORK, I HOPE I CAN FIX SERIES
def search(showname,ismovie,season,episode,date):
    url = f'https://www.tanti.bond/search/{showname}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    if ismovie == 1:
        all_link = soup.select('#movies .col .list-media')
        for link in all_link:
            url = link['href']
            response = requests.get(url)
            pattern = r'Data di rilascio\s*</div>\s*<div class="text">\s*(\d{4})\s*</div>'
            found_date = re.search(pattern, response.text)
            release_date = str(found_date.group(1))
            print(release_date)
            if release_date == date:
                tid= url.split('-')[1]
                print(tid)
                #Return URL and even the soup so I can use it later
                #I try to get doodstream link inside this function so I do not have to get again the response
                print(url)
                return tid
    elif ismovie == 0: 
        all_link = soup.select('#series .col .list-media')
        for link in all_link:
            base_url = link['href']
            url = f'{base_url}-{season}-season-{episode}-episode'
            response = requests.get(url)
            pattern = r'Data di rilascio\s*</div>\s*<div class="text">\s*(\d{4})\s*</div>'
            found_date = re.search(pattern, response.text)
            release_date = str(found_date.group(1))
            if release_date == date:
                print("RELEASE DATE IS EQUAL")
                tid= url.split('-')[1]
                print(tid)
                #I try to get doodstream link inside this function so I do not have to get again the response
                return tid



def get_protect_link(id):
    #Get the link where the Iframe is located, which contains the doodstream url kind of. 
    response = requests.get(f"https://p.hdplayer.casa/myadmin/play.php?id={id}")
    soup = BeautifulSoup(response.text, "lxml", parse_only=SoupStrainer('iframe'))
    print(soup)
    protect_link = soup.iframe['src'] 
    print("HERE PROTECT_LINK",protect_link)
    return  protect_link



def true_url(protect_link):
    # Define headers
    headers = {
        "Range": "bytes=0-",
        "Referer": "https://d000d.com/",
    }
    response = requests.get(protect_link)
    link = response.url
    #Get the ID
    doodstream_id = link.rsplit('/e/', 1)[-1]
    # Make a GET request
    
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
            rebobo = requests.get(url, headers=headers)
            real_url = f'{rebobo.text}123456789{match[2]}{real_time}'
            print(real_url)
            return 
        else:
            print("No match found in the text.")
            return None
  
    print("Error: Could not get the response.")
    return None




#Get temporaly ID
def tuttifilm(imdb):
    general = is_movie(imdb)
    ismovie = general[0]
    imdb_id = general[1]
    type = "Tuttifilm"
    if ismovie == 0 : 
        season = int(general[2])
        episode = int(general[3])
        if "tt" in imdb:
            if TF_FAST_SEARCH == "0":
                showname,date = get_info_imdb(imdb_id,ismovie,type)
            elif TF_FAST_SEARCH == "1":
                showname = get_info_imdb(imdb_id,ismovie,type)
                date = None
        else:
                #else just equals them
                tmdba = imdb_id.replace("tmdb:","")
                if TF_FAST_SEARCH == "0":
                    showname = get_info_tmdb(tmdba,ismovie,type)
                    date = None
    elif ismovie == 1:
        season = None
        episode = None
        if "tt" in imdb:
            #Get showname
                if TF_FAST_SEARCH == "0":
                    showname,date = get_info_imdb(imdb_id,ismovie,type)
                    
                elif TF_FAST_SEARCH == "1":
                    showname = get_info_imdb(imdb_id,ismovie,type)
                    date = None
        else:
            
            #else just equals them
            tmdba = imdb_id.replace("tmdb:","")
            season = None
            episode = None
            if TF_FAST_SEARCH == "0":
                showname,date = get_info_tmdb(tmdba,ismovie,type)
                date = None
            elif TF_FAST_SEARCH == "1":
                showname = get_info_tmdb(tmdba,ismovie,type)
                date = None
    
    tid = search(showname,ismovie,season,episode,date)
    protect_link = get_protect_link(tid)
    url = true_url(protect_link)

tuttifilm("tt16426418")













#OLD SEARC THAT DOESN't CHECK THE DATE
def mamma(showname,ismovie,season,episode):
    url = f'https://www.tanti.bond/search/{showname}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    if ismovie == 1:
        first_link = soup.select_one('#movies .col .list-media')
        url = first_link['href']
        return url
    elif ismovie == 0: 
        first_link = soup.select_one('#series .col .list-media')
        base_url = first_link['href']
        url = f'{base_url}-{season}-{episode}'
        print(url)
        return url
    















def searcht(showname,ismovie,season,episode):
    url = f'https://www.tanti.bond/search/{showname}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    date = "2020"
    if ismovie == 1:
        all_link = soup.select('#movies .col .list-media')
        for link in all_link:
            url = link['href']
            response = requests.get(url)
            info_soup = BeautifulSoup(response.text, "lxml")
            release_date= info_soup.select('div.video-attr div.text')[4].text.strip()
            if release_date == date:
                print("WOW")
                #Return URL and even the soup so I can use it later
                return url,info_soup
    elif ismovie == 0: 
        all_link = soup.select('#series .col .list-media')
        for link in all_link:
            base_url = link['href']
            url = f'{base_url}-{season}-season-{episode}-episode'
            response = requests.get(url)
            info_soup = BeautifulSoup(response.text, "lxml")
            release_date= info_soup.select('div.video-attr div.text')[4].text.strip()
            if release_date == date:
                print("RELEASE DATE IS EQUAL")
                #Return URL and even the soup so I can use it later
                return url,info_soup
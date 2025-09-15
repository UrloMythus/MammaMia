from bs4 import BeautifulSoup
import Src.Utilities.config as config
import logging
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)
tivu = {
    "dazn-zona-a": "801",
}
"""
    "rai-1": "3401",
    "rai-2": "3402",
    "rai-3": "3403",
    "rete-4": "123",
    "canale-5": "122",
    "italia-1": "121",
    "la7": "79",
    "tv8": "7260",
    "nove": "4323",
    "rai-4": "3405",
    "rai-movie": "3406",
    "rai-premium": "8522",
    "mediaset-extra": "129",
    "cielo": "4120",
    "rai-sport": "17714",
    "rai-news": "17711",
    "dmax": "15202",
    "real-time": "15201",
    "focus": "134",
    "giallo": "4322",
    "topcrime": "132",
    "boing": "126",
    "cartoonito": "133",
    "k2": "15204",
    "foodnetwork": "15203",
    "hgtv": "4334",
    "solocalcio": "4996" ,
    "euronews": "2017",
    "rai-4k": "3407",
"""
convert_bho_1 = {
    "euronews": "PlutoEuronews.it",
    "cartoonito": "cartoonito",
    "sky-tg-24": "skytg24",
    "frisbee": "frisbee",
    "hgtv": "hgtv",
    "k2": "k2",
    "supertennis": "supertennis",
    "solocalcio": "sportitaliasolocalcio",
    "sportitalia": "sportitalia",
    "sportitalia24": "RakutenSportItalia.it",
    "rsi-la-2": "rsila2",
    "baby-shark-tv": "RakutenBabySharkTv.it",
    "adrenaline-movies": "RakutenFullMoon.it",
    "adrenaline-movies": "RakutenBizzarroMovies.it",
    "cinema-italiano": "RakutenCinemaItalianoRakutenTv.it",
    "le-vite-degli-altri": "RakutenLeViteDegliAltri.it",
    "dark-matter": "RakutenDarkMatterItNew.it",
    "cine-western": "RakutenWesternEPeplum.it",
    "serie-crime": "RakutenCrimeSeriesItRakutenTv.it",
    "filmrise-sci-fi": "RakutenFuelTvNew.it",
    "doctor-who": "RakutenBbcDoctorWho.it",
    "bbc-drama": "RakutenBbcDrama.it",
    "documentari": "RakutenDocumentaries.it",
    "house-of-docs": "RakutenHouseOfDocs.it",
    "the-asylum": "PlutoTheAsylum.it",
    "western": "PlutoTvWestern.it",
    "consulenze-illegali": "PlutoConsulenzeIllegaliItPlus.it"
    
}


convert_bho_2 = {
    "rai-1": "Rai%201",
    "rai-2": "Rai 2",
    "rai-3": "Rai 3",
    "rai-4": "Rai 4",
    "rai-premium": "Rai Premium",
    "rai-movie": "Rai Movie",
    "rai-sport": "Rai Sport",
    "rete-4": "Rete 4",
    "canale-5": "Canale 5",
    "italia-1": "Italia 1",
    "topcrime": "Top Crime",
    "mediaset-extra": "Mediaset Extra",
    "focus": "Focus",
    "boing": "Boing",
    "history": "History",
    "comedy-central": "Comedy Central",
    "tv8": "TV 8",
    "cielo": "Cielo",
    "sky-cinema-action": "Sky Cinema Action",
    "sky-arte": "Sky Arte FHD",
    "sky-atlantic": "Sky Atlantic",
    "sky-cinema-collection": "Sky Cinema Collection",
    "sky-cinema-comedy": "Sky Cinema Comedy",
    "sky-cinema-drama": "Sky Cinema Drama",
    "sky-cinema-due": "Sky Cinema Due",
    "sky-cinema-family": "Sky Cinema Family",
    "sky-cinema-romance": "Sky Cinema Romance",
    "sky-cinema-suspence": "Sky Cinema Suspence",
    "sky-cinema-uno": "Sky Cinema Uno",
    "sky-uno": "Sky Uno",
    "sky-sport-24": "Sky Sport",
    "sky-sport-uno": "Sky Sport Uno",
    "sky-sport-f1": "Sky Sport F1",
    "sky-sport-motogp": "Sky Sport MotoGP",
    "sky-sport-arena": "Sky Sport Arena",
    "sky-sport-nba": "Sky Sport NBA",
    "eurosport-1": "Eurosport 1",
    "eurosport-2": "Eurosport 2",
    "dmax": "Dmax",
    "foodnetwork": "Food Network",
    "giallo": "Giallo",
    "nove": "Nove",
    "realtime": "Real Time",
}
convert_bho_3 = {
    "la7": "La7",
    "rai-news": "Rai News DTT",
    "sky-crime": "Sky CrimeInvestigation",
    "sky-documentaries": "Sky Documentaries HD",
    "sky-investigation": "Sky Investigation HD",
    "sky-nature": "Sky Nature HD",
    "sky-serie": "Sky Serie HD",
    "sky-sport-golf": "Sky Sport Golf",
    "sky-sport-251": "Sky Sport 251 HD",
    "sky-sport-252": "Sky Sport 252 HD",
    "sky-sport-253": "Sky Sport 253 HD",
    "sky-sport-254": "Sky Sport 254 HD",
    "sky-sport-255": "Sky Sport 255 HD",
    "sky-sport-256": "Sky Sport 256 HD",
    "sky-sport-257": "Sky Sport 257 HD",
    "sky-sport-258": "Sky Sport 258 HD",
    "sky-sport-259": "Sky Sport 259 HD",
    "sky-sport-260": "Sky Sport 260 HD",
    "sky-sport-261": "Sky Sport 261 HD",
    "sky-sport-max": "Sky Sport Max",
    "sky-sport-calcio": "Sky Sport Calcio HD",
    "sky-sport-tennis": "Sky Sport Tennis HD",
}


async def tivu_get(id,client):
    try:
        ik = tivu[id]
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://www.tivu.tv',
            'DNT': '1',
            'Sec-GPC': '1',
            'Connection': 'keep-alive',
            'Referer': 'https://www.tivu.tv/schedasat-rai1.html',
            # 'Cookie': 'ASP.NET_SessionId=p2fk5silp5mjgtx0j5chjrh3',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        data = {
            'ik': ik
        }

        response = await client.post('https://www.tivu.tv/getPrograms.ashx', headers=headers, data=data)
        soup = BeautifulSoup(response.text,'lxml')
        tr_element = soup.find('tr', class_='in_onda')
        hour_range = tr_element.find_all('td')[0].text.strip()
        program_name = tr_element.find_all('td')[1].text.strip()
        description = hour_range + " " + program_name
        return description
    except Exception as e:
        logger.warning(f"EPG {e}")
        description = f'Watch {id}'
        return description



async def epg_guide(id,client):
    try:
        if id in convert_bho_1:
            new_id = convert_bho_1[id]
            new_id = new_id.replace(" ","%20")
            response = await client.get(f"https://lorempizza-boh.hf.space/{new_id}/now")
        elif id in convert_bho_2:
            new_id = convert_bho_2[id]
            new_id = new_id.replace(" ","%20")
            response = await client.get(f"https://aimammam-boh2.hf.space/{new_id}/now")
        elif id in convert_bho_3:
            new_id = convert_bho_3[id]
            new_id = new_id.replace(" ","%20")
            response =  await client.get(f"https://aimammam-boh3.hf.space/{new_id}/now")
        data = response.json()
        description = data['description'].replace("- EPG by epg-guide.com","").replace("No description","")
        title = data['title']
        logger.info("MammaMia: EPG FOUND")
        return description,title   
    except Exception as e:
        logger.debug(e)
        description = f'Watch {id}'
        title = ""
        return description,title



'''
async def test_animeworld():
    async with httpx.AsyncClient() as client:
        test_id = "rai-1"  # Replace with actual ID
        try:
            results = await epg_guide(test_id, client)
            print(results)
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    import httpx
    import asyncio
    asyncio.run(test_animeworld())
'''
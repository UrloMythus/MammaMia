import Src.Utilities.config as config
SKY_DOMAIN = config.SKY_DOMAIN
okru = {
    "rai-1": "https://ok.ru/videoembed/9340203179632?nochat=1", 
    "rai-2": "https://ok.ru/videoembed/9267281010288?nochat=1",
    "canale-5": "https://ok.ru/videoembed/7871149252208?nochat=1",
    "italia-1": "https://ok.ru/videoembed/7393558339184?nochat=1",
    "rai-premium": "https://ok.ru/videoembed/7363152715376?nochat=1",
    "rai-movie": "https://ok.ru/videoembed/7384012693104?nochat=1",
    "tv8": "https://ok.ru/videoembed/8077072998000?nochat=1",
    "rsi-la-2": "https://ok.ru/videoembed/7681648107120?nochat=1",
    "mediaset-extra": "https://ok.ru/videoembed/7363151601264?nochat=1",
    "mediaset-infinity": "https://ok.ru/videoembed/6323249159792%3Fnochat=1"
}

STREAM = {
    "channels": [
        {
            "id": "la7",
            "title": "LA7",
            "name": "HD/FHD",
            "genres": ["La7"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/LA7_-_Logo_2011.svg/1280px-LA7_-_Logo_2011.svg.png",
            "url": "https://d3749synfikwkv.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-74ylxpgd78bpb/Live.m3u8"
        },
        {
            "id": "rai-1",
            "title": "Rai 1",
            "name": "Full HD Http",
            "genres": ["Rai"],
            "poster": "https://i.imgur.com/bb72vqh.jpeg",
            "url": "http://173.208.52.200/rai1/index.m3u8"
        },
        {
            "id": "rai-2",
            "title": "Rai 2",
            "name": "Full HD Http",
            "genres": ["Rai"],
            "poster": "https://i.imgur.com/jX95Qod.jpeg",
            "url": "http://173.208.52.200/rai2/index.m3u8"
        },
        {
            "id": "rai-3",
            "title": "Rai 3",
            "name": "Full HD Http",
            "genres": ["Rai"],
            "poster": "https://i.imgur.com/fgAh9if.jpeg",
            "url": "http://173.208.52.200/rai3/index.m3u8"
        },
        {
            "id": "rai-4",
            "title": "Rai 4",
            "name": "Full HD Http",
            "genres": ["Rai"],
            "poster": "https://i.imgur.com/NryLzhA.jpeg",
            "url": "http://173.208.52.200/rai4/index.m3u8"
        },
        {
            "id": "rai-premium",
            "title": "Rai Premium",
            "name": "Full HD",
            "genres": ["Rai"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/rai-premium_c.png",
            "url": "https://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=746992" 
        },
        {
            "id": "rai-4k",
            "title": "Rai 4K",
            "name": "4K",
            "genres": ["Rai"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Rai_4K_-_Logo_2016.svg/1920px-Rai_4K_-_Logo_2016.svg.png",
            "url": "https://raievent10-elem-live.akamaized.net/hls/live/619189/raievent10/raievent10/playlist.m3u8"

        },
        {
            "id": "rai-news",
            "title": "Rai News",
            "name": "",
            "genres": ["Rai"],
            "poster": "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/31/05/eb/3105eb24-a953-7bb9-876d-0fcfb0a19055/AppIcon-0-0-1x_U007epad-0-10-0-0-85-220.png/1200x630wa.png",
            "url": "https://streamcdnb4-8e7439fdb1694c8da3a0fd63e4dda518.msvdn.net/rainews1/hls/playlist_mo.m3u8"
        },
        {
            "id": "rai-movie",
            "title": "Rai Movie",
            "name": "",
            "genres": ["Rai"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/rai-movie_c.png",
            "url": "https://m3u.iranvids.com/rai-movie/output.m3u8"
        },
        {
            "id": "rai-sport",
            "title": "Rai Sport",
            "name": "",
            "genres": ["Rai"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/rai-sport_c.png",
            "url": "https://m3u.iranvids.com/rai-sport01/output.m3u8"
        },
        {
            "id": "rete-4",
            "title": "Rete 4",
            "name": "Full HD Http",
            "genres": ["Mediaset"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Rete_4_2018.svg/1024px-Rete_4_2018.svg.png",
            "url": "http://173.208.52.200/rete4/index.m3u8"
        },
        {
            "id": "euronews",
            "title": "Euronews",
            "name": "720p",
            "genres": ["Euronews"],
            "poster": "https://yt3.googleusercontent.com/t3slq37NYJRuP2UoEZDoPKyMClKyQULG8-j2DEfzL1XXcBvFpR6z6HD7rtc0wDn8Mqt0OtpU=s900-c-k-c0x00ffffff-no-rj",
            "url": "https://rakuten-euronews-3-it.samsung.wurl.tv/manifest/playlist.m3u8"
        },
        {
            "id": "canale-5",
            "title": "Canale 5",
            "name": "Full HD Http",
            "genres": ["Mediaset"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/canale-5_c.png",
            "url": "http://173.208.52.200/canale5/index.m3u8"
        },
        {
            "id": "italia-1",
            "title": "Italia 1",
            "name": "Full HD Http",
            "genres": ["Mediaset"],
            "poster": "https://upload.wikimedia.org/wikipedia/en/thumb/e/e2/Italia_1.svg/1024px-Italia_1.svg.png",
            "url": "http://173.208.52.200/italia1/index.m3u8"
        },
        {
            "id": "topcrime",
            "title": "Top Crime",
            "name": "HD/FHD",
            "genres": ["Mediaset"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/top-crime_c.png",
            "url": "https://live02-seg.msf.cdn.mediaset.net/live/ch-lt/lt-clr.isml/index.m3u8"
        },
        {
            "id": "mediaset-extra",
            "title": "Mediaset Extra",
            "name": "HD/FHD",
            "genres": ["Mediaset"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/mediaset-extra_c.png",
            "url": "https://live02-seg.msf.cdn.mediaset.net/live/ch-kq/kq-clr.isml/index.m3u8"
        },
        {
            "id": "focus",
            "title": "Focus",
            "name": "HD/FHD",
            "genres": ["Mediaset"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/d/d0/Focus_channel.png",
            "url": "https://live02-seg.msf.cdn.mediaset.net/live/ch-fu/fu-clr.isml/index.m3u8"
        },
        {
            "id": "boing",
            "title": "Boing",
            "name": "HD/FHD",
            "genres": ["Mediaset"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Logo_Boing.png",
            "url": "https://live02-seg.msf.cdn.mediaset.net/live/ch-kb/kb-clr.isml/index.m3u8"
        },
        {
            "id": "cartoonito",
            "title": "Cartoonito",
            "name": "HD/FHD",
            "genres": ["Mediaset"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Cartoonito_-_Logo_2021.svg/1920px-Cartoonito_-_Logo_2021.svg.png",
            "url": "https://live02-seg.msf.cdn.mediaset.net/live/ch-la/la-clr.isml/index.m3u8"
        },
        {
            "id": "history",
            "title": "History",
            "name": "",
            "genres": ["A+E"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/history_c.png"
        },
        {
            "id": "comedy-central",
            "title": "Comedy Central",
            "name": "",
            "genres": ["Paramount"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/comedy-central_c.png"
        },
        {
            "id": "sky-tg-24",
            "title": "Sky TG24",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://images-na.ssl-images-amazon.com/images/I/512j1jeZaHL.png",
            "url": "https://hlslive-web-gcdn-skycdn-it.akamaized.net/TACT/12221/web/master.m3u8?hdnts=st=1701861650~exp=1765449000~acl=/*~hmac=84c9f3f71e57b13c3a67afa8b29a8591ea9ed84bf786524399545d94be1ec04d"
        },
        {
            "id": "tv8",
            "title": "TV8",
            "name": "SD",
            "genres": ["Sky"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/9/9a/TV8_logo.png",
            "url": "https://hlslive-web-gcdn-skycdn-it.akamaized.net/TACT/11223/tv8web/master.m3u8?hdnea=st=1701861650~exp=1765449000~acl=/*~hmac=84c9f3f71e57b13c3a67afa8b29a8591ea9ed84bf786524399545d94be1ec04d"
        },
        {
            "id": "cielo",
            "title": "Cielo",
            "name": "SD",
            "genres": ["Sky"],
            "poster": "https://static.sky.it/static_clientlibs/skycielo/clientlibs/clientlib-site/resources/images/facebook.jpg",
            "url": "https://hlslive-web-gcdn-skycdn-it.akamaized.net/TACT/11219/cieloweb/master.m3u8?hdnea=st=1701861650~exp=1765449000~acl=/*~hmac=84c9f3f71e57b13c3a67afa8b29a8591ea9ed84bf786524399545d94be1ec04d"
        },
        {
            "id": "sky-cinema-action",
            "title": "Sky Cinema Action",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/sky-cinema-action_c.png"
        },
        {
            "id": "sky-arte",
            "title": "Sky Arte",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://www.davinciface.com/wp-content/uploads/2022/07/sky_arte_logo-270x270.jpg"
        },
        {
            "id": "sky-atlantic",
            "title": "Sky Atlantic",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/sky-atlantic_c.png"
        },
        {
            "id": "sky-cinema-collection",
            "title": "Sky Cinema Collection",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/sky-cinema-collection_c.png"
        },
        {
            "id": "sky-cinema-comedy",
            "title": "Sky Cinema Comedy",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/sky-cinema-comedy_c.png"
        },
        {
            "id": "sky-cinema-drama",
            "title": "Sky Cinema Drama",
            "name": "",
            "genres": ["Sky"],
            "poster":"https://i.imgur.com/Z8hr5aR.png"
        },
        {
            "id": "sky-cinema-due",
            "title": "Sky Cinema Due",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://i.imgur.com/xfbZiXs.png"
        },
        {
            "id": "sky-cinema-family",
            "title": "Sky Cinema Family",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/sky-cinema-family_c.png"
        },
        {
            "id": "sky-cinema-romance",
            "title": "Sky Cinema Romance",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/sky-cinema-romance_c.png"
        },
        {
            "id": "sky-cinema-suspence",
            "title": "Sky Cinema Suspence",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://i.imgur.com/vS97bNg.png"
        },
        {
            "id": "sky-cinema-uno",
            "title": "Sky Cinema Uno",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/sky-cinema-1_c.png"
        },
        {
            "id": "sky-crime",
            "title": "Sky Crime",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://i.imgur.com/j2JdQaH.png"
        },
        {
            "id": "sky-documentaries",
            "title": "Sky Documentaries",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://artworks.thetvdb.com/banners/posters/117551-3.jpg"
        },
        {
            "id": "sky-investigation",
            "title": "Sky Investigation",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/sky-investigation_c.png"
        },
        {
            "id": "sky-nature",
            "title": "Sky Nature",
            "name": "",
            "genres": ["Sky"],
            "poster":"https://search.bus-hit.me/image_proxy?url=https%3A%2F%2Fstatic.wikia.nocookie.net%2Flogosfake%2Fimages%2Fa%2Fad%2FSky_Nature_Generic_ID_2020.png%2Frevision%2Flatest%2Fscale-to-width-down%2F1200%3Fcb%3D20200725184630&h=71ab69ffa3abfe2ce6c20912b44f862adff4f10b9d4d761c18d292b7ffa3e9a9"
        },
        {
            "id": "sky-serie",
            "title": "Sky Serie",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://i.imgur.com/FYvSq5T.png"
        },
        {
            "id": "sky-uno",
            "title": "Sky Uno",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://www.miotvonline.com/wp-content/uploads/2020/09/sky-uno-straming-live-miotv.jpg"
        },
        {
            "id": "sky-sport-24",
            "title": "Sky Sport 24",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://img2.sport-tv-guide.live/images/tv-station-sky-sport24-it-356.png"

        },
        {
            "id": "sky-sport-golf",
            "title": "Sky Sport Golf",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://search.bus-hit.me/image_proxy?url=https%3A%2F%2Fencrypted-tbn0.gstatic.com%2Fimages%3Fq%3Dtbn%3AANd9GcRQoDZOK798-OYz0E_NAahzde_JW-hLcHK-PjLm0rCXyVVcj_Y%26s&h=4b1b7a276442b52778daf26f745d06f57ff6c0cf401f4d7f3e371a566247f3ef"
        },
        {
            "id": "sky-sport-251",
            "title": "Sky Sport 251",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png"
        },
        {
            "id": "sky-sport-252",
            "title": "Sky Sport 252",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png"
        },
        {
            "id": "sky-sport-253",
            "title": "Sky Sport 253",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png"
        },
        {
            "id": "sky-sport-254",
            "title": "Sky Sport 254",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png"
        },
        {
            "id": "sky-sport-255",
            "title": "Sky Sport 255",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png"
        },
        {
            "id": "sky-sport-256",
            "title": "Sky Sport 256",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png"
        },
        {
            "id": "sky-sport-257",
            "title": "Sky Sport 257",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png"
        },
        {
            "id": "sky-sport-258",
            "title": "Sky Sport 258",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png"
        },
        {
            "id": "sky-sport-259",
            "title": "Sky Sport 259",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png"            
        },
        {
            "id": "sky-sport-260",
            "title": "Sky Sport 260",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png"
        },
        {
            "id": "sky-sport-261",
            "title": "Sky Sport 261",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png"
        },
        {
            "id": "sky-sport-max",
            "title": "Sky Sport Max",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://i.imgur.com/TWl58VI.png"
        },
        {
            "id": "sky-sport-uno",
            "title": "Sky Sport Uno",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/sky-sport-1_c.png"
        },
        {
            "id": "sky-sport-f1",
            "title": "Sky Sport F1",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://i1.wp.com/cache.pressmailing.net/thumbnail/story_hires/395b1e2f-a1c6-4cf6-9869-02155da4021f/Sky_F1_Logo.jpg.jpg"               
        },
        {
            "id": "sky-sport-motogp",
            "title": "Sky Sport MotoGP",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://img2.sport-tv-guide.live/images/tv-station-sky-sport-motogp-360.png"
        },
        {
            "id": "sky-sport-calcio",
            "title": "Sky Sport Calcio",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/sky-sport-2_c.png"
        },
        {
            "id": "sky-sport-arena",
            "title": "Sky Sport Arena",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://img2.sport-tv-guide.live/images/tv-station-sky-sport-arena-354.png"
        },
        {
            "id": "sky-sport-tennis",
            "title": "Sky Sport Tennis",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://pbs.twimg.com/profile_images/1752313472325431296/jr-YrkR6_400x400.png"
        },
        {
            "id": "sky-sport-nba",
            "title": "Sky Sport NBA",
            "name": "",
            "genres": ["Sky"],
            "poster": "https://www.nbareligion.com/wp-content/uploads/2019/09/sky-sport-nba.jpg"
        },
        {
            "id": "dazn-zona-a",
            "title": "DAZN Zona A",
            "name": "",
            "genres": ["DAZN"],
            "poster": "https://i.ytimg.com/vi/0cEfGLq-tz4/maxresdefault.jpg"
        },
        {
            "id": "dazn-1",
            "title": "DAZN 1",
            "name": "",
            "genres": ["DAZN"],
            "poster": "https://i.ytimg.com/vi/0cEfGLq-tz4/maxresdefault.jpg"
        },
        {
            "id": "eurosport-1",
            "title": "Eurosport 1",
            "name": "",
            "genres": ["Warner Bros"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/eurosport-1_c.png"
        },
        {
            "id": "eurosport-2",
            "title": "Eurosport 2",
            "name": "",
            "genres": ["Warner Bros"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/eurosport-2_c.png"
        },
        {
            "id": "dmax",
            "title": "DMAX",
            "name": "",
            "genres": ["Warner Bros"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/d-max_c.png",
            "url": "https://amg16146-wbdi-amg16146c8-samsung-it-1841.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-dmax-samsungit/playlist.m3u8"
        },
        {
            "id": "foodnetwork",
            "title": "Food Network",
            "name": "",
            "genres": ["Warner Bros"],
            "poster":"https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Food_Network_logo.svg/1024px-Food_Network_logo.svg.png",
            "url": "https://amg16146-wbdi-amg16146c3-samsung-it-1836.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-foodnetwork-samsungit/playlist.m3u8"
        },
        {
            "id": "frisbee",
            "title": "Frisbee",
            "name": "",
            "genres": ["Warner Bros"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/FRISBEE_LOGO_2015.png/1280px-FRISBEE_LOGO_2015.png",
            "url": "https://amg16146-wbdi-amg16146c7-samsung-it-1840.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-frisbee-samsungit/playlist.m3u8"
        },
        {
            "id": "giallo",
            "title": "Giallo",
            "name": "",
            "genres": ["Warner Bros"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/giallo_c.png",
            "url": "https://amg16146-wbdi-amg16146c5-samsung-it-1838.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-giallo-samsungit/playlist.m3u8"
        },
        {
            "id": "hgtv",
            "title": "HGTV",
            "name": "",
            "genres": ["Warner Bros"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/HGTV_2010.svg/1920px-HGTV_2010.svg.png",
            "url": "https://amg16146-wbdi-amg16146c9-samsung-it-1842.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-hgtv-samsungit/playlist.m3u8"
        },
        {
            "id": "k2",
            "title": "K2",
            "name": "",
            "genres": ["Warner Bros"],
            "poster": "https://upload.wikimedia.org/wikipedia/it/thumb/7/70/K2_logo_%282013%29.svg/800px-K2_logo_%282013%29.svg.png",
            "url": "https://amg16146-wbdi-amg16146c6-samsung-it-1839.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-k2-samsungit/playlist.m3u8"
        },
        {
            "id": "nove",
            "title": "Nove",
            "name": "",
            "genres": ["Warner Bros"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/nove_c.png",
            "url": "https://amg16146-wbdi-amg16146c1-samsung-it-1831.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-nove-samsungit/playlist.m3u8"
        },

        {
            "id": "realtime",
            "title": "Real Time",
            "name": "",
            "genres": ["Warner Bros"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/real-time_c.png",
            "url": "https://amg16146-wbdi-amg16146c2-samsung-it-1835.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-realtime-samsungit/playlist.m3u8"
        },
        {
            "id": "supertennis",
            "title": "Super Tennis",
            "name": "",
            "genres": ["FIT"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/0/02/SUPERTENNIS_HD.png",
            "url": "https://live-embed.supertennix.hiway.media/restreamer/supertennix_client/gpu-a-c0-16/restreamer/rtmp/hls/h24_supertennix/manifest.m3u8"
        },
        {
            "id": "solocalcio",
            "title": "Solo Calcio",
            "name": "",
            "genres": ["Sportitalia"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/SI_Live_24_logo_%282019%29.svg/1280px-SI_Live_24_logo_%282019%29.svg.png",  
            "url": "https://di-kzbhv8pw.vo.lswcdn.net/sportitalia/sisolocalcio/playlist.m3u8" 
        },
        {
            "id": "sportitalia",
            "title": "Sportitalia",
            "name": "",
            "genres": ["Sportitalia"],
            "poster": "https://upload.wikimedia.org/wikipedia/en/5/55/Sportitalia.jpg",
            "url": "https://di-kzbhv8pw.vo.lswcdn.net/sportitalia/sihd/playlist.m3u8"
        },
        {
            "id": "sportitalia24",
            "title": "Sportitalia 24",
            "name": "",
            "genres": ["Sportitalia"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/SI_Live_24_logo_%282019%29.svg/1280px-SI_Live_24_logo_%282019%29.svg.png",
            "url": "https://di-kzbhv8pw.vo.lswcdn.net/sportitalia/sihd/playlist.m3u8"
        },
        {
            "id": "rsi-la-2",
            "title": "RSI LA 2",
            "name": "",
            "genres": ["RSI"],
            "poster": "https://livehere.one/img/rsi.png"    
        },
        {
            "id": "baby-shark-tv",
            "title": "Baby Shark TV",
            "name": "",
            "genres": ["Rakuten"],
            "poster": "https://flxt.tmsimg.com/assets/p19459897_b_v13_aa.jpg",
            "url": "https://c0c65b821b3542c3a4dca92702f59944.mediatailor.us-east-1.amazonaws.com/v1/master/04fd913bb278d8775298c26fdca9d9841f37601f/RakutenTV-eu_BabySharkTV/playlist.m3u8?ads.content_classification=6&ads.device_lmt=1&ads.device_make=&ads.device_model=&ads.device_type=web&ads.device_year=&ads.env=prod&ads.gdpr_consent=&ads.market=it&ads.player_height=&ads.player_width=&ads.pod_type=playerpage_midroll&ads.ppid=&ads.rtv_content_id=3623&ads.rtv_content_language=eng&ads.rtvid=271861&ads.streaming_id=17ded124-30eb-47bc-ab57-ddfce3a16599&ads.user_type=visitor&ads.wurl_channel=696"
        },
        {
            "id": "adrenaline-movies",
            "title": "Rakuten Adrenaline Movies",
            "name": "",
            "genres": ["Rakuten"],
            "poster": "https://tvpnlogopeu.samsungcloud.tv/platform/image/sourcelogo/vc/00/02/34/ITBC11000050E_20231213T033148SQUARE.png_20231213033148.png",
            "url": "https://minerva-fullmoon-1-eu.plex.wurl.tv/4300.m3u8"
        },
        {
            "id": "bizzarro-movies",
            "title": "Bizzarro Movies",
            "name": "",
            "genres": ["Rakuten"],
            "poster": "https://tvpnlogopeu.samsungcloud.tv/platform/image/sourcelogo/vc/00/02/34/ITBA3300024IU_20240214T034959SQUARE.png_20240214034959.png",
            "url": "https://minerva-bizzarromovies-1-eu.plex.wurl.tv/4300.m3u8"
        },
        {
            "id": "cinema-italiano",
            "title": "Cinema Italiano",
            "name": "",
            "genres": ["Rakuten"],
            "poster": "https://tvpnlogopeu.samsungcloud.tv/platform/image/sourcelogo/vc/00/02/34/ITBA33000238E_20240313T074122SQUARE.png",
            "url": "https://minerva-cinemasegreto-1-eu.plex.wurl.tv/4300.m3u8"
        },
        {
            "id": "le-vite-degli-altri",
            "title": "Le Vite Degli Altri",
            "name": "",
            "genres": ["Rakuten"],
            "poster": "https://tvpnlogopeu.samsungcloud.tv/platform/image/sourcelogo/vc/00/02/34/ITBD3200002DU_20230913T031625SQUARE.png_20230913031625.png",
            "url": "https://amg02512-nexodigital-amg02512c2-wedotv-eu-869.playouts.now.amagi.tv/playlist/amg02512-nexodigital-levitedeglialtri-wedotveu/playlist.m3u8"
        },
        {
            "id": "dark-matter",
            "title": "Dark Matter",
            "name": "",
            "genres": ["Rakuten"],
            "poster": "https://tvpnlogopeu.samsungcloud.tv/platform/image/sourcelogo/vc/00/02/34/ITBC400001LX_20220404T005859SQUARE.png_20220404005901.png",
            "url": "https://d39g1vxj2ef6in.cloudfront.net/v1/master/3fec3e5cac39a52b2132f9c66c83dae043dc17d4/prod-rakuten-stitched/master.m3u8?ads.xumo_channelId=88883020&ads.xumo_contentId=3480"
        },
        {
            "id": "cine-western",
            "title": "Cine Western",
            "name": "",
            "genres": ["Rakuten"],
            "poster": "https://tvpnlogopeu.samsungcloud.tv/platform/image/sourcelogo/vc/00/02/34/ITBB20000072M_20240214T035001SQUARE.png_20240214035002.png",
            "url": "https://minerva-wp-1-eu.plex.wurl.tv/4300.m3u8"
        },
        {
            "id": "serie-crime",
            "title": "Serie Crime",
            "name": "",
            "genres": ["Rakuten"],
            "poster": "https://images-2.rakuten.tv/storage/global-live-channel/translation/artwork-negative/0e0a6638-7c4c-4065-82d7-a34d818388ee-width500.png",
            "url": "https://rakuten-seriecrime-6-it.xiaomi.wurl.tv/4300.m3u8"
        },
        {
            "id": "filmrise-sci-fi",
            "title": "Filmrise Sci-Fi",
            "name": "",
            "genres": ["Rakuten"],
            "poster": "https://images-3.rakuten.tv/storage/global-live-channel/translation/artwork_negative/ba0fa0a9-7e17-497e-abcc-9405dbb3a7f5-filmrise-sci-fi-1643623368-quality100.png",
            "url": "https://d39g1vxj2ef6in.cloudfront.net/v1/master/3fec3e5cac39a52b2132f9c66c83dae043dc17d4/prod-rakuten-stitched/master.m3u8?ads.xumo_channelId=9991764"
        },
        {
            "id": "doctor-who",
            "title": "Doctor Who",
            "name": "",
            "genres": ["Rakuten"],
            "poster": "https://images.pluto.tv/channels/62e7f8db27ce19000732d1aa/colorLogoPNG.png",
            "url": "https://bbceu-doctorwho-1-it.rakuten.wurl.tv/3000.m3u8"
        },
        {
            "id": "bbc-drama",
            "title": "BBC Drama",
            "name": "",
            "genres": ["Rakuten"],
            "poster": "https://images.pluto.tv/channels/62e7fa5ab5062e0007dcf97d/colorLogoPNG.png",
            "url": "https://bbceu-bbcdrama-2-it.rakuten.wurl.tv/3000.m3u8"
        },
        {
            "id": "documentari",
            "title": "Documentari (Grandi Documentari)",
            "name": "",
            "genres": ["Rakuten"],
            "poster": "https://tvpnlogopeu.samsungcloud.tv/platform/image/sourcelogo/vc/00/02/34/ITBC35000016T_20230208T013151SQUARE.png_20230208013152.png",
            "url": "https://videosolutions-wedobigstories-rakuten.amagi.tv/playlist1080p.m3u8"
        },
        {
            "id": "house-of-docs",
            "title": "House of Docs",
            "name": "",
            "genres": ["Rakuten"],
            "poster": "https://tvpnlogopeu.samsungcloud.tv/platform/image/sourcelogo/vc/00/02/34/ITBD1100001B7_20230412T042554SQUARE.png_20230412042554.png",
            "url": "https://amg02512-nexodigital-amg02512c1-wedotv-eu-871.playouts.now.amagi.tv/playlist/amg02512-nexodigital-houseofdocs-wedotveu/playlist.m3u8"
        },
        {
            "id": "pluto-matrimoni",
            "title": "Pluto TV Matrimoni",
            "name": "",
            "genres": ["Pluto"],
            "poster": "https://images.pluto.tv/channels/661f8f2506839f0008b864e9/colorLogoPNG.png",
            "url": "http://stitcher.pluto.tv/v1/stitch/embed/hls/channel/661f8f2506839f0008b864e9/master.m3u8?deviceId=0&deviceModel=samsung&deviceVersion=0&appVersion=0&deviceType=samsung&deviceMake=samsung&deviceDNT=true"
        },
        {
            "id": "the-asylum",
            "title": "The Asylum",
            "name": "",
            "genres": ["Pluto"],
            "poster": "https://images.pluto.tv/channels/62e8d5369e48940007fc1dc1/colorLogoPNG.png",
            "url": "http://stitcher.pluto.tv/v1/stitch/embed/hls/channel/62e8d5369e48940007fc1dc1/master.m3u8?deviceType=samsung-tvplus&deviceMake=samsung&deviceModel=samsung&deviceVersion=unknown&appVersion=unknown&deviceLat=0&deviceLon=0&deviceDNT=%7BTARGETOPT%7D&deviceId=%7BPSID%7D&advertisingId=%7BPSID%7D&us_privacy=1YNY&samsung_app_domain=%7BAPP_DOMAIN%7D&samsung_app_name=%7BAPP_NAME%7D&profileLimit=&profileFloor=&embedPartner=samsung-tvplus"
        },
        {
            "id": "western",
            "title": "Western",
            "name": "",
            "genres": ["Pluto"],
            "poster": "https://images.pluto.tv/channels/62e7fb67478a5b0007e6c50c/colorLogoPNG.png",
            "url": "http://stitcher.pluto.tv/v1/stitch/embed/hls/channel/62e7fb67478a5b0007e6c50c/master.m3u8?deviceType=samsung-tvplus&deviceMake=samsung&deviceModel=samsung&deviceVersion=unknown&appVersion=unknown&deviceLat=0&deviceLon=0&deviceDNT=%7BTARGETOPT%7D&deviceId=%7BPSID%7D&advertisingId=%7BPSID%7D&us_privacy=1YNY&samsung_app_domain=%7BAPP_DOMAIN%7D&samsung_app_name=%7BAPP_NAME%7D&profileLimit=&profileFloor=&embedPartner=samsung-tvplus"
        },
        {
            "id": "consulenze-illegali",
            "title": "Consulenze Illegali",
            "name": "",
            "genres": ["Pluto"],
            "poster": "https://images.pluto.tv/channels/60b9dc99521a1400079bdfba/colorLogoPNG.png"
            # URL rimosso perché sarà dinamico
        },
        # Canali da OMGTV (script_with_noepg.py integrato)
        {
            "id": "omgtv-vavoo-eurosport-1",
            "title": "EUROSPORT 1 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-canale-5",
            "title": "CANALE 5 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-1",
            "title": "RAI 1 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/rai-1-it.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-24-live-during-events-only",
            "title": "SKY SPORT 24 [LIVE DURING EVENTS ONLY] (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-cinema-action",
            "title": "SKY CINEMA ACTION (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-24",
            "title": "SKY SPORT 24 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sports-f1",
            "title": "SKY SPORTS F1 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-moto-gp",
            "title": "SKY SPORT MOTO GP (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-cinema-collection",
            "title": "SKY CINEMA COLLECTION (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-uno",
            "title": "SKY SPORT UNO (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-tennis",
            "title": "SKY SPORT TENNIS (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-dmax",
            "title": "DMAX (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Discovery", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-italia-1",
            "title": "ITALIA 1 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-canale-5-2",
            "title": "CANALE 5 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-20-mediaset",
            "title": "20 MEDIASET (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-3",
            "title": "RAI 3 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-cinema-drama",
            "title": "SKY CINEMA DRAMA (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-arena",
            "title": "SKY SPORT ARENA (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-cinema-uno",
            "title": "SKY CINEMA UNO (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-atlantic",
            "title": "SKY ATLANTIC (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-cinema-suspense",
            "title": "SKY CINEMA SUSPENSE (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-cinema-family",
            "title": "SKY CINEMA FAMILY (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-cinema-due",
            "title": "SKY CINEMA DUE (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-5",
            "title": "SKY PRIMAFILA 5 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-eurosport-2",
            "title": "EUROSPORT 2 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-cinema-action-2",
            "title": "SKY CINEMA ACTION (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-cinema-suspense-2",
            "title": "SKY CINEMA SUSPENSE (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-serie",
            "title": "SKY SERIE (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-cinema-comedy",
            "title": "SKY CINEMA COMEDY (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-la-7",
            "title": "LA 7 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Altro", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-cinema-comedy-2",
            "title": "SKY CINEMA COMEDY (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-4",
            "title": "RAI 4 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-arte",
            "title": "SKY ARTE (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Documentari", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-eurosport-1-2",
            "title": "EUROSPORT 1 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-cinema-uno-24",
            "title": "SKY CINEMA UNO +24 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-cartoon-network",
            "title": "CARTOON NETWORK (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Bambini", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-football-live-during-events-only",
            "title": "SKY SPORT FOOTBALL [LIVE DURING EVENTS ONLY] (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-tennis-2",
            "title": "SKY SPORT TENNIS (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-motogp",
            "title": "SKY SPORT MOTOGP (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-nba",
            "title": "SKY SPORT NBA (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-sport-live-during-events-only",
            "title": "RAI SPORT [LIVE DURING EVENTS ONLY] (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-calcio",
            "title": "SKY SPORT CALCIO (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-news-24",
            "title": "RAI NEWS 24 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Notizie", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-zona-dazn",
            "title": "ZONA DAZN (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-tg-24",
            "title": "SKY TG 24 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Notizie", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-10",
            "title": "SKY PRIMAFILA 10 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-tg-com-24",
            "title": "TG COM 24 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Notizie", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-8",
            "title": "SKY PRIMAFILA 8 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-arena-2",
            "title": "SKY SPORT ARENA (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rete-4",
            "title": "RETE 4 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-calcio-2",
            "title": "SKY SPORT CALCIO (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-2",
            "title": "RAI 2 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-cinema-uno-2",
            "title": "SKY CINEMA UNO (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-2-2",
            "title": "RAI 2 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-dmax-2",
            "title": "DMAX (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Discovery", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-cielo",
            "title": "CIELO (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-mediaset-extra",
            "title": "MEDIASET EXTRA (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-cinema-romance",
            "title": "SKY CINEMA ROMANCE (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-4-2",
            "title": "RAI 4 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-la-5",
            "title": "LA 5 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Altro", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-cielo-2",
            "title": "CIELO (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-italia-2",
            "title": "ITALIA 2 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-8-2",
            "title": "SKY PRIMAFILA 8 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-sport",
            "title": "RAI SPORT (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-top-crime",
            "title": "TOP CRIME (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Discovery", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-dazn-1",
            "title": "DAZN 1 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-uno-2",
            "title": "SKY SPORT UNO (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-7",
            "title": "SKY PRIMAFILA 7 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-golf",
            "title": "SKY SPORT GOLF (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-uno",
            "title": "SKY UNO (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sky", "Vavoo"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-uno-it.png"
        },
        {
            "id": "omgtv-vavoo-boing-plus",
            "title": "BOING PLUS (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Bambini", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-nick-jr",
            "title": "NICK JR (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Bambini", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-cinema-romance-2",
            "title": "SKY CINEMA ROMANCE (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-4k",
            "title": "RAI 4K (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rsi-la-1",
            "title": "RSI LA 1 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Altro", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-italia",
            "title": "RAI ITALIA (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rsi-la-2",
            "title": "RSI LA 2 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Altro", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-tv-8",
            "title": "TV 8 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-atlantic-2",
            "title": "SKY ATLANTIC (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-deejay-tv",
            "title": "DEEJAY TV (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Altro", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-9",
            "title": "SKY PRIMAFILA 9 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-yoyo",
            "title": "RAI YOYO (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-cinema-due-2",
            "title": "SKY CINEMA DUE (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-6",
            "title": "SKY PRIMAFILA 6 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-arte-2",
            "title": "SKY ARTE (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Documentari", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-news-24-2",
            "title": "RAI NEWS 24 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Notizie", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-1",
            "title": "SKY PRIMAFILA 1 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-4",
            "title": "SKY PRIMAFILA 4 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-golf-2",
            "title": "SKY SPORT GOLF (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-nba-2",
            "title": "SKY SPORT NBA (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-f1",
            "title": "SKY SPORT F1 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-discovery-nove",
            "title": "DISCOVERY NOVE (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Documentari", "Discovery", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-2",
            "title": "SKY PRIMAFILA 2 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-hgtv",
            "title": "HGTV (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Discovery", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-1-2",
            "title": "SKY PRIMAFILA 1 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-cinema-action-backup",
            "title": "SKY CINEMA ACTION (BACKUP) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-5",
            "title": "RAI 5 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-5-2",
            "title": "SKY PRIMAFILA 5 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-premium",
            "title": "RAI PREMIUM (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-super",
            "title": "SUPER! (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Altro", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-food-network",
            "title": "FOOD NETWORK (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Discovery", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-5-2",
            "title": "RAI 5 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-tennis-channel",
            "title": "TENNIS CHANNEL (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-hgtv-2",
            "title": "HGTV (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Discovery", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-giallo",
            "title": "GIALLO (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Altro", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-dazn",
            "title": "DAZN (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-17",
            "title": "SKY PRIMAFILA 17 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-k2",
            "title": "K2 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Bambini", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-27-twentyseven",
            "title": "27 TWENTYSEVEN (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Altro", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-16",
            "title": "SKY PRIMAFILA 16 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-crime-investigation",
            "title": "CRIME+ INVESTIGATION (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Discovery", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-comedy-central",
            "title": "COMEDY CENTRAL (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sky", "Vavoo"],
            "poster": "https://yt3.googleusercontent.com/FPzu1EWCI54fIh2j9JEp0NOzwoeugjL4sZTQCdoxoQY1U4QHyKx2L3wPSw27IueuZGchIxtKfv8=s900-c-k-c0x00ffffff-no-rj"
        },
        {
            "id": "omgtv-vavoo-history",
            "title": "HISTORY (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Documentari", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-giallo-2",
            "title": "GIALLO (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Altro", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-history-2",
            "title": "HISTORY (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Documentari", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-gulp",
            "title": "RAI GULP (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-nickelodeon",
            "title": "NICKELODEON (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Bambini", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-dazn-2",
            "title": "DAZN 2 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-1-2",
            "title": "RAI 1 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/rai-1-it.png"
        },
        {
            "id": "omgtv-vavoo-animal-planet",
            "title": "ANIMAL PLANET (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-cine-34-mediaset",
            "title": "CINE 34 MEDIASET (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rete-4-2",
            "title": "RETE 4 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-cinema-family-2",
            "title": "SKY CINEMA FAMILY (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-3-2",
            "title": "RAI 3 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-football",
            "title": "SKY SPORT FOOTBALL (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-premium-2",
            "title": "RAI PREMIUM (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-iris",
            "title": "IRIS (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-k2-2",
            "title": "K2 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Bambini", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-real-time",
            "title": "REAL TIME (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Discovery", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-mediaset-20",
            "title": "MEDIASET 20 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-la-5-2",
            "title": "LA 5 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Altro", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-food-network-2",
            "title": "FOOD NETWORK (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Discovery", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-uno-2",
            "title": "SKY UNO (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sky", "Vavoo"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-uno-it.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-3",
            "title": "SKY PRIMAFILA 3 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-discovery-nove-2",
            "title": "DISCOVERY NOVE (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Documentari", "Discovery", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-real-time-2",
            "title": "REAL TIME (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Discovery", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-2-2",
            "title": "SKY PRIMAFILA 2 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-movie",
            "title": "RAI MOVIE (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-10-2",
            "title": "SKY PRIMAFILA 10 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-max",
            "title": "SKY SPORT MAX (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-movie-2",
            "title": "RAI MOVIE (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-mediaset-1",
            "title": "MEDIASET 1 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-eurosport-2-2",
            "title": "EUROSPORT 2 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-mediaset-iris",
            "title": "MEDIASET IRIS (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-super-tennis",
            "title": "SKY SUPER TENNIS (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-cartoon-network-2",
            "title": "CARTOON NETWORK (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Bambini", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-4-2",
            "title": "SKY PRIMAFILA 4 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-discovery-channel",
            "title": "DISCOVERY CHANNEL (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Documentari", "Discovery", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-cine-34",
            "title": "CINE 34 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-9-2",
            "title": "SKY PRIMAFILA 9 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-storia",
            "title": "RAI STORIA (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-focus",
            "title": "FOCUS (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-27-twenty-seven",
            "title": "27 TWENTY SEVEN (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-scuola",
            "title": "RAI SCUOLA (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-6-2",
            "title": "SKY PRIMAFILA 6 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-la-7-2",
            "title": "LA 7 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Altro", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-focus-2",
            "title": "FOCUS (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-frisbee",
            "title": "FRISBEE (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Bambini", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-discovery-channel-2",
            "title": "DISCOVERY CHANNEL (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Documentari", "Discovery", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-7-2",
            "title": "SKY PRIMAFILA 7 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-deejay-tv-2",
            "title": "DEEJAY TV (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Altro", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-top-crime-2",
            "title": "TOP CRIME (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Discovery", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-cartoonito",
            "title": "CARTOONITO (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Bambini", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-premium-crime",
            "title": "PREMIUM CRIME (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-boing",
            "title": "BOING (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Bambini", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-super-2",
            "title": "SUPER! (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Altro", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rsi-la-1-2",
            "title": "RSI LA 1 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Altro", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-boing-2",
            "title": "BOING (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Bambini", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-tv-8-2",
            "title": "TV 8 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-storia-2",
            "title": "RAI STORIA (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-discovery-focus",
            "title": "DISCOVERY FOCUS (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-mediaset-italia",
            "title": "MEDIASET ITALIA (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-yoyo-2",
            "title": "RAI YOYO (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-cartoonito-backup",
            "title": "CARTOONITO (BACKUP) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Bambini", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-3-2",
            "title": "SKY PRIMAFILA 3 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-super-tennis",
            "title": "SUPER TENNIS (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-comedy-central-2",
            "title": "COMEDY CENTRAL (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sky", "Vavoo"],
            "poster": "https://yt3.googleusercontent.com/FPzu1EWCI54fIh2j9JEp0NOzwoeugjL4sZTQCdoxoQY1U4QHyKx2L3wPSw27IueuZGchIxtKfv8=s900-c-k-c0x00ffffff-no-rj"
        },
        {
            "id": "omgtv-vavoo-rai-scuola-2",
            "title": "RAI SCUOLA (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-gulp-2",
            "title": "RAI GULP (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-wwe-channel",
            "title": "WWE CHANNEL (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Discovery", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sport-italia-backup",
            "title": "SPORT ITALIA (BACKUP) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-mediaset-italia-2",
            "title": "MEDIASET ITALIA 2 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-nature",
            "title": "SKY NATURE (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Documentari", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-14",
            "title": "SKY PRIMAFILA 14 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-18",
            "title": "SKY PRIMAFILA 18 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-cartoonito-2",
            "title": "CARTOONITO (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Bambini", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rsi-la-2-2",
            "title": "RSI LA 2 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Altro", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-super-tennis-2",
            "title": "SUPER TENNIS (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sport-italia",
            "title": "SPORT ITALIA (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sportitalia-solocalcio",
            "title": "SPORTITALIA SOLOCALCIO (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sport-italia-solo-calcio-live-during-events-only",
            "title": "SPORT ITALIA SOLO CALCIO [LIVE DURING EVENTS ONLY] (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-sport",
            "title": "RAI SPORT+ (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-tg-24-2",
            "title": "SKY TG 24 (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Notizie", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport",
            "title": "SKY SPORT (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-sport-serie-a",
            "title": "SKY SPORT SERIE A (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-12",
            "title": "SKY PRIMAFILA 12 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-discovery-k2",
            "title": "DISCOVERY K2 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Bambini", "Discovery", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-primafila-15",
            "title": "SKY PRIMAFILA 15 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sportitalia-plus",
            "title": "SPORTITALIA PLUS (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sport", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-nat-geo-wild",
            "title": "NAT GEO WILD (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Documentari", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rai-italia-2",
            "title": "RAI ITALIA (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Rai Tv", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-la-7-d",
            "title": "LA 7 D (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Altro", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-nat-geo",
            "title": "NAT GEO (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Documentari", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-documentaries",
            "title": "SKY DOCUMENTARIES (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-fox",
            "title": "FOX (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-nat-geo-2",
            "title": "NAT GEO (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Documentari", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-warner-tv",
            "title": "WARNER TV (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Discovery", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-mediaset-infinity-1",
            "title": "MEDIASET INFINITY+ 1 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-disney-film",
            "title": "DISNEY+ FILM (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-sky-cinema-due-24",
            "title": "SKY CINEMA DUE +24 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-nat-geo-wild-2",
            "title": "NAT GEO WILD (2) (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Documentari", "Sky", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-tgcom-24",
            "title": "TGCOM 24 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Notizie", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rakuten-action-movies",
            "title": "RAKUTEN ACTION MOVIES (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Rakuten", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-mediaset-infinity-2",
            "title": "MEDIASET INFINITY+ 2 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-catfish",
            "title": "CATFISH (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Altro", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-mediaset-infinity-5",
            "title": "MEDIASET INFINITY+ 5 (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Intrattenimento", "Mediaset", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rakuten-drama",
            "title": "RAKUTEN DRAMA (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Rakuten", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rakuten-tv-shows",
            "title": "RAKUTEN TV SHOWS (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Rakuten", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rakuten-family",
            "title": "RAKUTEN FAMILY (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Rakuten", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rakuten-comedy-movies",
            "title": "RAKUTEN COMEDY MOVIES (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Film", "Rakuten", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-vavoo-rakuten-top-free",
            "title": "RAKUTEN TOP FREE (V)",
            "name": "OMGTV - Vavoo",
            "genres": ["OMGTV", "Rakuten", "Vavoo"],
            "poster": "https://www.vavoo.tv/software/images/logo.png"
        },
        {
            "id": "omgtv-247ita-eurosport-1",
            "title": "EuroSport 1 (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sport", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/spain/eurosport-1-es.png"
        },
        {
            "id": "omgtv-247ita-eurosport-2",
            "title": "EuroSport 2 (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sport", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/spain/eurosport-2-es.png"
        },
        {
            "id": "omgtv-247ita-italia-1",
            "title": "Italia 1 (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Mediaset", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/italia1-it.png"
        },
        {
            "id": "omgtv-247ita-la7",
            "title": "La7 (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Tv Italia", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/la7-it.png"
        },
        {
            "id": "omgtv-247ita-la7d",
            "title": "LA7d (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Tv Italia", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/la7-it.png"
        },
        {
            "id": "omgtv-247ita-rai-1",
            "title": "Rai 1 (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Rai Tv", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/rai-1-it.png"
        },
        {
            "id": "omgtv-247ita-rai-2",
            "title": "Rai 2 (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Rai Tv", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/rai-2-it.png"
        },
        {
            "id": "omgtv-247ita-rai-3",
            "title": "Rai 3 (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Rai Tv", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/rai-3-it.png"
        },
        {
            "id": "omgtv-247ita-rai-sport",
            "title": "Rai Sport (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sport", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/rai-sport-it.png"
        },
        {
            "id": "omgtv-247ita-rai-premium",
            "title": "Rai Premium (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Rai Tv", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/rai-premium-it.png"
        },
        {
            "id": "omgtv-247ita-sky-sports-golf",
            "title": "Sky Sports Golf (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sport", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-sport-golf-it.png"
        },
        {
            "id": "omgtv-247ita-sky-sport-motogp",
            "title": "Sky Sport MotoGP (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sport", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-sport-motogp-it.png"
        },
        {
            "id": "omgtv-247ita-sky-sport-tennis",
            "title": "Sky Sport Tennis (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sport", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-sport-tennis-it.png"
        },
        {
            "id": "omgtv-247ita-sky-sport-f1",
            "title": "Sky Sport F1 (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sport", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-sport-f1-it.png"
        },
        {
            "id": "omgtv-247ita-sky-sport-football",
            "title": "Sky Sport Football (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sport", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-sport-football-it.png"
        },
        {
            "id": "omgtv-247ita-sky-sport-uno",
            "title": "Sky Sport UNO (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sport", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-sport-uno-it.png"
        },
        {
            "id": "omgtv-247ita-sky-sport-arena",
            "title": "Sky Sport Arena (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sport", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-sport-arena-it.png"
        },
        {
            "id": "omgtv-247ita-sky-uno",
            "title": "Sky UNO (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sky", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-uno-it.png"
        },
        {
            "id": "omgtv-247ita-sky-cinema-collection",
            "title": "Sky Cinema Collection (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sky", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-cinema-collection-it.png"
        },
        {
            "id": "omgtv-247ita-sky-cinema-uno",
            "title": "Sky Cinema Uno (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sky", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-cinema-uno-it.png"
        },
        {
            "id": "omgtv-247ita-sky-cinema-action",
            "title": "Sky Cinema Action (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sky", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-cinema-action-it.png"
        },
        {
            "id": "omgtv-247ita-sky-cinema-comedy",
            "title": "Sky Cinema Comedy (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sky", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-cinema-comedy-it.png"
        },
        {
            "id": "omgtv-247ita-sky-cinema-uno-24",
            "title": "Sky Cinema Uno +24 (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sky", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-cinema-uno-it.png"
        },
        {
            "id": "omgtv-247ita-sky-cinema-romance",
            "title": "Sky Cinema Romance (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sky", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-cinema-romance-it.png"
        },
        {
            "id": "omgtv-247ita-sky-cinema-family",
            "title": "Sky Cinema Family (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sky", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-cinema-family-it.png"
        },
        {
            "id": "omgtv-247ita-sky-cinema-due-24",
            "title": "Sky Cinema Due +24 (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sky", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-cinema-due-plus24-it.png"
        },
        {
            "id": "omgtv-247ita-sky-cinema-drama",
            "title": "Sky Cinema Drama (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sky", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-cinema-drama-it.png"
        },
        {
            "id": "omgtv-247ita-sky-cinema-suspense",
            "title": "Sky Cinema Suspense (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sky", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-cinema-suspense-it.png"
        },
        {
            "id": "omgtv-247ita-sky-sport-24",
            "title": "Sky Sport 24 (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sport", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-sport-24-it.png"
        },
        {
            "id": "omgtv-247ita-sky-sport-calcio",
            "title": "Sky Sport Calcio (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sport", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-sport-calcio-it.png"
        },
        {
            "id": "omgtv-247ita-sky-calcio-1",
            "title": "Sky Calcio 1 (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sport", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/germany/sky-select-1-alt-de.png"
        },
        {
            "id": "omgtv-247ita-sky-calcio-2",
            "title": "Sky Calcio 2 (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sport", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/germany/sky-select-2-alt-de.png"
        },
        {
            "id": "omgtv-247ita-sky-calcio-3",
            "title": "Sky Calcio 3 (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sport", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/germany/sky-select-3-alt-de.png"
        },
        {
            "id": "omgtv-247ita-sky-calcio-4",
            "title": "Sky Calcio 4 (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sport", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/germany/sky-select-4-alt-de.png"
        },
        {
            "id": "omgtv-247ita-sky-calcio-5",
            "title": "Sky Calcio 5 (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sport", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/germany/sky-select-5-alt-de.png"
        },
        {
            "id": "omgtv-247ita-sky-calcio-6",
            "title": "Sky Calcio 6 (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sport", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/germany/sky-select-6-alt-de.png"
        },
        {
            "id": "omgtv-247ita-sky-calcio-7",
            "title": "Sky Calcio 7 (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sport", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/germany/sky-select-7-alt-de.png"
        },
        {
            "id": "omgtv-247ita-sky-serie",
            "title": "Sky Serie (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sky", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-serie-it.png"
        },
        {
            "id": "omgtv-247ita-20-mediaset",
            "title": "20 Mediaset (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Mediaset", "247ita"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/20-it.png"
        },
        {
            "id": "omgtv-247ita-dazn-1",
            "title": "DAZN 1 (D)",
            "name": "OMGTV - 247ita",
            "genres": ["OMGTV", "Sport", "247ita"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/DAZN_1_Logo.svg/774px-DAZN_1_Logo.svg.png"
        },
        {
            "id": "omgtv-sportstreaming-sport-24",
            "title": "Sport 24 (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://sportstreaming.net/assets/img/live/perma/live1.png"
        },
        {
            "id": "omgtv-sportstreaming-formula-1",
            "title": "Formula 1 (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://sportstreaming.net/assets/img/live/perma/live2.png"
        },
        {
            "id": "omgtv-sportstreaming-moto-gp",
            "title": "Moto GP (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://sportstreaming.net/assets/img/live/perma/live3.png"
        },
        {
            "id": "omgtv-sportstreaming-nba",
            "title": "NBA (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://sportstreaming.net/assets/img/live/perma/live4.png"
        },
        {
            "id": "omgtv-sportstreaming-tennis",
            "title": "Tennis (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://sportstreaming.net/assets/img/live/perma/live5.png"
        },
        {
            "id": "omgtv-sportstreaming-golf",
            "title": "Golf (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-sport-uno",
            "title": "Sport Uno (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-sport-calcio",
            "title": "Sport Calcio (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-sport-max",
            "title": "Sport Max (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-sport-arena",
            "title": "Sport Arena (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-cinema-uno",
            "title": "Cinema Uno (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-cinema-due",
            "title": "Cinema Due (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-cinema-collection",
            "title": "Cinema Collection (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-cinema-family",
            "title": "Cinema Family (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-cinema-action",
            "title": "Cinema Action (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-cinema-suspense",
            "title": "Cinema Suspense (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-cinema-romance",
            "title": "Cinema Romance (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-cinema-drama",
            "title": "Cinema Drama (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-cinema-comedy",
            "title": "Cinema Comedy (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-uno",
            "title": "Uno (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-atlantic",
            "title": "Atlantic (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-serie",
            "title": "Serie (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-investigation",
            "title": "Investigation (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-comedy-central",
            "title": "Comedy Central (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-arte",
            "title": "Arte (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-documentaries",
            "title": "Documentaries (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-nature",
            "title": "Nature (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-sportstreaming-crime",
            "title": "Crime (SpS)",
            "name": "OMGTV - Sportstreaming",
            "genres": ["OMGTV", "SportStreaming"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Sky_italia_2018.png/500px-Sky_italia_2018.png"
        },
        {
            "id": "omgtv-calcio-comedy-central",
            "title": "Comedy Central (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sky", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-dazn-1",
            "title": "DAZN 1 (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-eurosport-1",
            "title": "Eurosport 1 (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-eurosport-2",
            "title": "Eurosport 2 (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-formula-1",
            "title": "Formula 1 (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-history",
            "title": "History (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-rai-sport",
            "title": "Rai Sport (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-serie-a",
            "title": "Serie A (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sky", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-serie-a-1",
            "title": "Serie A 1 (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sky", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-258",
            "title": "Sky 258 (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-259",
            "title": "Sky 259 (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-arte",
            "title": "Sky Arte (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sky", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-atlantic",
            "title": "Sky Atlantic (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sky", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-cinema-action",
            "title": "Sky Cinema Action (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sky", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-cinema-collection",
            "title": "Sky Cinema Collection (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sky", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-cinema-comedy",
            "title": "Sky Cinema Comedy (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sky", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-cinema-drama",
            "title": "Sky Cinema Drama (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sky", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-cinema-due",
            "title": "Sky Cinema Due (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sky", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-cinema-family",
            "title": "Sky Cinema Family (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sky", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-cinema-romance",
            "title": "Sky Cinema Romance (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sky", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-cinema-suspense",
            "title": "Sky Cinema Suspense (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sky", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-cinema-uno",
            "title": "Sky Cinema Uno (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sky", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-crime",
            "title": "Sky Crime (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sky", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-documentaries",
            "title": "Sky Documentaries (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sky", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-investigation",
            "title": "Sky Investigation (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sky", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-nature",
            "title": "Sky Nature (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sky", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-serie",
            "title": "Sky Serie (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sky", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-sport-24",
            "title": "Sky Sport 24 (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-sport-251",
            "title": "Sky Sport 251 (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-sport-252",
            "title": "Sky Sport 252 (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-sport-253",
            "title": "Sky Sport 253 (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-sport-254",
            "title": "Sky Sport 254 (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-sport-255",
            "title": "Sky Sport 255 (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-sport-256",
            "title": "Sky Sport 256 (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-sport-257",
            "title": "Sky Sport 257 (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-sport-arena",
            "title": "Sky Sport Arena (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-sport-calcio",
            "title": "Sky Sport Calcio (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-sport-f1",
            "title": "Sky Sport F1 (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-sport-golf",
            "title": "Sky Sport Golf (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-sport-max",
            "title": "Sky Sport Max (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-sport-motogp",
            "title": "Sky Sport MotoGP (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-sport-nba",
            "title": "Sky Sport NBA (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-sport-tennis",
            "title": "Sky Sport Tennis (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-sport-uno",
            "title": "Sky Sport Uno (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sky-uno",
            "title": "Sky Uno (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sky", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-solo-calcio",
            "title": "Solo Calcio (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-spezia",
            "title": "Spezia (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-sportitalia",
            "title": "Sportitalia (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-zona-b",
            "title": "Zona B (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        },
        {
            "id": "omgtv-calcio-zona-dazn",
            "title": "Zona DAZN (CT1)",
            "name": "OMGTV - Calcio",
            "genres": ["OMGTV", "Sport", "Calcio TOP1", "Calcio"],
            "poster": "https://i.postimg.cc/NFGs2Ptq/photo-2025-03-12-12-36-48.png"
        }
    ]
}




webru_vary = {
    "sky-cinema-action": "calcioXac",
    "comedy-central": "calcioXcomedycentral",
    "history": "calcioXhistory",
    "sky-arte": "calcioXskyarte",
    "sky-atlantic": "calcioXskyatlantic",
    "sky-cinema-collection": "calcioXskycinemacollection",
    "sky-cinema-comedy": "calcioXskycinemacomedy",
    "sky-cinema-drama": "calcioXskycinemadrama",
    "sky-cinema-due": "calcioXskycinemadue",
    "sky-cinema-family": "calcioXskycinemafamily",
    "sky-cinema-romance": "calcioXskycinemaromance",
    "sky-cinema-suspence": "calcioXskycinemasuspence",
    "sky-cinema-uno": "calcioXskycinemauno",
    "sky-crime": "calcioXskycrime",
    "sky-documentaries": "calcioXskydocumentaries",
    "sky-investigation": "calcioXskyinvestigation",
    "sky-nature": "calcioXskynature",
    "sky-serie": "calcioXskyserie",
    "sky-uno": "calcioXskyuno",
    "sky-sport-24": "calcioXskysport24",  
    "sky-sport-golf": "calcioXskysportgolf",
    "sky-sport-251": "calcioXskysport251",
    "sky-sport-253": "calcioXskysport253",
    "sky-sport-max": "calcioXskysportmax",
    "sky-sport-255": "calcioXskysport255",
    "sky-sport-259": "calcioXsky259",
    "sky-sport-252": "calcioXskysport252",
    "sky-sport-254": "calcioXskysport254",
    "sky-sport-256": "calcioXskysport256",
    "sky-sport-257": "calcioXskysport257",
    "sky-sport-258": "calcioXsky258",
    "sky-sport-259": "calcioXsky259",
    "sky-sport-260": "calcioXsky260",
    "sky-sport-261": "calcioXsky261",
    "eurosport-1": "calcioXeurosport1",
    "eurosport-2": "calcioXeurosport2",
    "sky-sport-uno": "calcioXskysportuno",
    "sky-sport-f1": "calcioXskysportf1",
    "sky-sport-motogp": "calcioXskysportmotogp",
    "sky-sport-calcio": "calcioXskysportcalcio",
    "sky-sport-arena": "calcioXskysportarena",
    "sky-sport-tennis": "calcioXskysporttennis",
    "sky-sport-nba": "calcioXskysportnba", 
    "dazn-1": "Xserie"
}
#"dazn-zona-a": "https://webuit.mizhls.ru/lb/calcioXzona/index.m3u8"
webru_dlhd = {
    "sky-sport-tennis": "premium576",
    "sky-sport-uno": "premium461",
    "sky-cinema-collection": "premium859",
    "sky-cinema-romance": "premium864",
    "sky-sport-24": "premium869",
    "sky-sport-254": "premium874",
    "sky-sport-f1": "premium577",
    "sky-sport-arena": "premium462",
    "sky-cinema-uno": "premium860",
    "sky-cinema-family": "premium865",
    "sky-sport-calcio": "premium870",
    "sky-sport-255": "premium875",
    "sky-cinema-action": "premium861",
    "sky-cinema-due": "premium866",
    "sky-sport-251": "premium871",
    "sky-sport-256": "premium876",
    "sky-sport-golf": "premium574",
    "sky-uno": "premium881",
    "sky-cinema-comedy": "premium862",
    "sky-cinema-drama": "premium867",
    "sky-sport-252": "premium872",
    "sky-sport-257": "premium877",
    "sky-sport-motogp": "premium575",
    "sky-sport-football": "premium460",
    "sky-cinema-uno-24": "premium863",
    "sky-cinema-suspence": "premium868",
    "sky-sport-253": "premium873",
    "sky-serie": "premium880",
    "dazn-1": "premium877",
    "rai-1": "premium850",
    "rai-2": "premium851",
    "rai-3": "premium852",
    "canale-5": "premium853",
    "rai-sport": "premium882",
    "rai-premium": "premium858",
    "italia-1" : "premium854",
    "la7": "premium855",
    "la7d": "premium856",
    "mediaset-20": "premium857",
    "la5": "premium856",

}
extra_sources = {
    "rai-1": ["https://m3u.iranvids.com/rai01/output.m3u8"],
    "rai-2": ["https://m3u.iranvids.com/rai02/output.m3u8"],
    "rai-3": ["https://dash2.antik.sk/live/test_rai_tre_tizen/playlist.m3u8","https://wzstreaming.rai.it/TVlive/liveStream/playlist.m3u8","https://list.iptvcat.com/my_list/s/1f22856f68f2fba4a993c47f47c78a64.m3u8","https://list.iptvcat.com/my_list/s/a372048a4fb440e752aec141aa02885f.m3u8","https://list.iptvcat.com/my_list/s/c7efe17aa0dc8096561967bfb828d4f3.m3u8","https://list.iptvcat.com/my_list/s/2d1f14bbb3370d263d8d3f0d9f5128e0.m3u8"],
    "rete-4":["https://tvit.leicaflorianrobert.dev/mediaset/rete-4/stream.m3u8","https://live02-seg.msf.cdn.mediaset.net/live/ch-r4/r4-clr.isml/index.m3u8"],
    "canale-5":["https://live02-seg.msf.cdn.mediaset.net/live/ch-c5/c5-clr.isml/index.m3u8","https://tvit.leicaflorianrobert.dev/mediaset/canale-5/stream.m3u8"],
    "italia-1":["https://tvit.leicaflorianrobert.dev/mediaset/italia-1/stream.m3u8","https://live02-seg.msf.cdn.mediaset.net/live/ch-i1/i1-clr.isml/index.m3u8"],
    "rai-4k": ["https://list.iptvcat.com/my_list/s/fbf04fbd9694eee71b5af9f12e49538d.m3u8"],
    "rai-news":["https://8e7439fdb1694c8da3a0fd63e4dda518.msvdn.net/rainews1/hls/playlist_mo.m3u8"],
    "topcrime": ["https://tvit.leicaflorianrobert.dev/mediaset/top-crime/stream.m3u8"],
    "mediaset-extra": ["https://tvit.leicaflorianrobert.dev/mediaset/mediaset-extra/stream.m3u8"],
    "focus": ["https://tvit.leicaflorianrobert.dev/mediaset/focus/stream.m3u8"],
    "boing": ["https://tvit.leicaflorianrobert.dev/mediaset/boing/stream.m3u8"],
    "cartoonito": ["https://tvit.leicaflorianrobert.dev/mediaset/cartoonito/stream.m3u8"],
    "tv8": ["https://tvit.leicaflorianrobert.dev/sky/tv8/stream.m3u8"],
    "cielo": ["https://tvit.leicaflorianrobert.dev/sky/cielo/stream.m3u8"],
    "dmax": ["https://tvit.leicaflorianrobert.dev/discovery/dmax/stream.m3u8"],
    "nove": ["https://tvit.leicaflorianrobert.dev/discovery/nove/stream.m3u8"],
    "euronews": ["https://amg00882-amg00882c4-wedotv-eu-4536.playouts.now.amagi.tv/playlist/amg00882-euronewsfast-euronewsita-wedotveu/playlist.m3u8?app_bundle=&app_name=wedotv&app_store_url=https://wedotv.com&url=https://wedotv.com&gdpr=1&channel_name=Euronews - Italiano&content_custom_1_param=Euronews - Italiano"],
    "doctor-who": ["https://amg00793-amg00793c17-samsung-it-4577.playouts.now.amagi.tv/playlist/amg00793-bbcstudios-drwhoitaly-samsungit/playlist.m3u8"],
    "supertennis": ["https://live-embed.supertennix.hiway.media/restreamer/supertennix_client/gpu-a-c0-16/restreamer/outgest/h24_supertennix/manifest.m3u8"]
}
skystreaming ={
    "sky-sport-tennis": f"{SKY_DOMAIN}/embed/MKCKP",
    "sky-sport-24": f"{SKY_DOMAIN}/embed/GB7zq",
    "sky-sport-251": f"{SKY_DOMAIN}/embed/drHbM",
    "sky-sport-252": f"{SKY_DOMAIN}/embed/m5kfg",
    "sky-sport-253": f"{SKY_DOMAIN}/embed/YprHf",
    "sky-sport-254": f"{SKY_DOMAIN}/embed/wroRV",
    "sky-sport-255": f"{SKY_DOMAIN}/embed/0TixN",
    "sky-sport-256": f"{SKY_DOMAIN}/embed/8g8bh",
    "sky-sport-257": f"{SKY_DOMAIN}/embed/ri859",
    "sky-sport-258": f"{SKY_DOMAIN}/embed/UoJuW",
    "sky-sport-259": f"{SKY_DOMAIN}/embed/squCy",
    "sky-sport-260": f"{SKY_DOMAIN}/embed/Z5h2e",
    "sky-sport-261": f"{SKY_DOMAIN}/embed/Hz9FW",
    "sky-sport-uno": f"{SKY_DOMAIN}/embed/tb1np",
    "sky-sport-f1": f"{SKY_DOMAIN}/embed/MLkym",
    "sky-sport-motogp": f"{SKY_DOMAIN}/embed/ARFFv",
    "sky-sport-calcio": f"{SKY_DOMAIN}/embed/STOZT",
    "sky-sport-arena": f"{SKY_DOMAIN}/embed/NkEda",
    "sky-sport-max": f"{SKY_DOMAIN}/embed/4QzWz",
    "sky-sport-nba": f"{SKY_DOMAIN}/embed/saR8j",
    "sky-sport-golf": f"{SKY_DOMAIN}/embed/s9L5f",
    "eurosport-1": f"{SKY_DOMAIN}/embed/Vyv99",
    "eurosport-2": f"{SKY_DOMAIN}/embed/um8E5",
    "dazn-zona-a": ["https://hls.kangal.sbs/hls/serie/index.m3u8","https://hls.kangal.sbs/hls/serie/index.m3u8"],
    "sportitalia": "https://hls.kangal.sbs/hls/sportitalia/index.m3u8",
}
huhu = {
    "canale-5": "1101559666",
    "sky-sport-motogp": "2090703806",
    "rai-1": "1225653759",
    "sky-cinema-drama": "1235530177",
    "sky-cinema-action": "3812796171",
    "Dazn": "2745635299",
    "sky-sport-uno": "3192996672",
    "canale-5": "1534161807",
    "mediaset-extra": "477466531",
    "Dazn-1": "1376440573",
    "sky-sport-24": "2775802255",
    "sky-sport-24": "3445562519",
}
provider_map = {
        'SC': 'STREAMINGCOMMUNITY',
        'SC_FS': 'SC_FAST_SEARCH',
        'LC': 'LORDCHANNEL',
        'SW': 'STREAMINGWATCH',
        'TF_FS': 'TF_FAST_SEARCH',
        'TF': 'TANTIFILM',  # Assuming 'TF' should also be handled
        'FT': 'FILMPERTUTTI',
        'AW': 'ANIMEWORLD',
        'DDL': 'DDLSTREAM',
        'CB': 'CB01',
        "GS": "GUARDASERIE",
        "GHD": "GUARDAHD",
        "OST": "ONLINESERIETV",
    }

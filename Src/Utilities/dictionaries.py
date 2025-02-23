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
            "poster": "https://images.pluto.tv/channels/60b9dc99521a1400079bdfba/colorLogoPNG.png",
            "url": "http://stitcher.pluto.tv/v1/stitch/embed/hls/channel/60b9dc99521a1400079bdfba/master.m3u8?deviceType=samsung-tvplus&deviceMake=samsung&deviceModel=samsung&deviceVersion=unknown&appVersion=unknown&deviceLat=0&deviceLon=0&deviceDNT=%7BTARGETOPT%7D&deviceId=%7BPSID%7D&advertisingId=%7BPSID%7D&us_privacy=1YNY&samsung_app_domain=%7BAPP_DOMAIN%7D&samsung_app_name=%7BAPP_NAME%7D&profileLimit=&profileFloor=&embedPartner=samsung-tvplus"
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
    }
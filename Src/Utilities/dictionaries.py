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
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Rete_4_-_Logo_2018.svg/1024px-Rete_4_-_Logo_2018.svg.png"
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
            "id": "italia-2",
            "title": "ITALIA 2",
            "name": "",
            "genres": ["Mediaset"],
            "poster": "https://upload.wikimedia.org/wikipedia/it/thumb/c/c5/Logo_Italia2.svg/520px-Logo_Italia2.svg.png"
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
            "genres": ["Sky"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/history_c.png"
        },
        {
            "id": "comedy-central",
            "title": "Comedy Central",
            "name": "",
            "genres": ["Intrattenimento", "Sky"],
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
            "genres": ["Intrattenimento", "Sky"],
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
            "genres": ["Film & Serie", "Sky"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/sky-cinema-action_c.png"
        },
        {
            "id": "sky-arte",
            "title": "Sky Arte",
            "name": "",
            "genres": ["Documentari", "Sky"],
            "poster": "https://www.davinciface.com/wp-content/uploads/2022/07/sky_arte_logo-270x270.jpg"
        },
        {
            "id": "sky-atlantic",
            "title": "Sky Atlantic",
            "name": "",
            "genres": ["Film & Serie", "Sky"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/sky-atlantic_c.png"
        },
        {
            "id": "sky-cinema-collection",
            "title": "Sky Cinema Collection",
            "name": "",
            "genres": ["Film & Serie", "Sky"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/sky-cinema-collection_c.png"
        },
        {
            "id": "sky-cinema-comedy",
            "title": "Sky Cinema Comedy",
            "name": "",
            "genres": ["Film & Serie", "Sky"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/sky-cinema-comedy_c.png"
        },
        {
            "id": "sky-cinema-drama",
            "title": "Sky Cinema Drama",
            "name": "",
            "genres": ["Film & Serie", "Sky"],
            "poster":"https://i.imgur.com/Z8hr5aR.png"
        },
        {
            "id": "sky-cinema-due",
            "title": "Sky Cinema Due",
            "name": "",
            "genres": ["Film & Serie", "Sky"],
            "poster": "https://i.imgur.com/xfbZiXs.png"
        },
        {
            "id": "sky-cinema-due-24",
            "title": "SKY CINEMA DUE +24",
            "name": "",
            "genres": ["Film & Serie",  "Sky"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-cinema-due-plus24-it.png"
        },
        {
            "id": "sky-cinema-family",
            "title": "Sky Cinema Family",
            "name": "",
            "genres": ["Film & Serie", "Sky"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/sky-cinema-family_c.png"
        },
        {
            "id": "sky-cinema-romance",
            "title": "Sky Cinema Romance",
            "name": "",
            "genres": ["Film & Serie", "Sky"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/sky-cinema-romance_c.png"
        },
        {
            "id": "sky-cinema-suspence",
            "title": "Sky Cinema Suspence",
            "name": "",
            "genres": ["Film & Serie", "Sky"],
            "poster": "https://i.imgur.com/vS97bNg.png"
        },
        {
            "id": "sky-cinema-uno",
            "title": "Sky Cinema Uno",
            "name": "",
            "genres": ["Film & Serie", "Sky"],
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
            "genres": ["Documentari", "Sky"],
            "poster": "https://artworks.thetvdb.com/banners/posters/117551-3.jpg"
        },
        {
            "id": "sky-investigation",
            "title": "Sky Investigation",
            "name": "",
            "genres": ["Documentari", "Sky"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/sky-investigation_c.png"
        },
        {
            "id": "sky-nature",
            "title": "Sky Nature",
            "name": "",
            "genres": ["Documentari", "Sky"],
            "poster":"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Sky_Nature.svg/1024px-Sky_Nature.svg.png"
        },
        {
            "id": "nat-geo-wild",
            "title": "NAT GEO WILD",
            "name": "",
            "genres": ["Documentari", "Sky"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/national-geographic-wild-it.png"
        },
        {
            "id": "discovery-channel",
            "title": "DISCOVERY CHANNEL",
            "name": "",
            "genres": ["Documentari", "Discovery"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/discovery-channel-it.png"
        },
        {
            "id": "sky-serie",
            "title": "Sky Serie",
            "name": "",
            "genres": ["Film & Serie", "Sky"],
            "poster": "https://i.imgur.com/FYvSq5T.png"
        },
        {
            "id": "sky-uno",
            "title": "Sky Uno",
            "name": "",
            "genres": ["Intrattenimento", "Sky"],
            "poster": "https://www.miotvonline.com/wp-content/uploads/2020/09/sky-uno-straming-live-miotv.jpg"
        },
        {
            "id": "sky-sport-24",
            "title": "Sky Sport 24",
            "name": "",
            "genres": ["Sport", "Sky"],
            "poster": "https://img2.sport-tv-guide.live/images/tv-station-sky-sport24-it-356.png"

        },
        {
            "id": "sky-sport-golf",
            "title": "Sky Sport Golf",
            "name": "",
            "genres": ["Sport", "Sky"],
            "poster": "https://scontent-fra3-2.xx.fbcdn.net/v/t39.30808-6/355705088_762776855850002_5111452123456427866_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=-ubj97H2ENQQ7kNvwHHc7MR&_nc_oc=AdnsmV9fNun-N4tN-_GssiC3OT73gcJ0z9O2DeeXXm7u9eXHcQVxbtPbYLZCxTIno4E&_nc_zt=23&_nc_ht=scontent-fra3-2.xx&_nc_gid=88vxLZNCS4S7cHdsvcAUFw&oh=00_AfNhylOoB327G41AAUeFW47Z5RtGJ1rTXxCcfxUHfrxwWA&oe=6850675F"
        },
        {
            "id": "sky-sport-251",
            "title": "Sky Sport 251",
            "name": "",
            "genres": ["Sport", "Sky"],
            "poster": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png"
        },
        {
            "id": "sky-sport-252",
            "title": "Sky Sport 252",
            "name": "",
            "genres": ["Sport", "Sky"],
            "poster": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png"
        },
        {
            "id": "sky-sport-253",
            "title": "Sky Sport 253",
            "name": "",
            "genres": ["Sport", "Sky"],
            "poster": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png"
        },
        {
            "id": "sky-sport-254",
            "title": "Sky Sport 254",
            "name": "",
            "genres": ["Sport", "Sky"],
            "poster": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png"
        },
        {
            "id": "sky-sport-255",
            "title": "Sky Sport 255",
            "name": "",
            "genres": ["Sport", "Sky"],
            "poster": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png"
        },
        {
            "id": "sky-sport-256",
            "title": "Sky Sport 256",
            "name": "",
            "genres": ["Sport", "Sky"],
            "poster": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png"
        },
        {
            "id": "sky-sport-257",
            "title": "Sky Sport 257",
            "name": "",
            "genres": ["Sport", "Sky"],
            "poster": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png"
        },
        {
            "id": "sky-sport-258",
            "title": "Sky Sport 258",
            "name": "",
            "genres": ["Sport", "Sky"],
            "poster": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png"
        },
        {
            "id": "sky-sport-259",
            "title": "Sky Sport 259",
            "name": "",
            "genres": ["Sport", "Sky"],
            "poster": "https://logodownload.org/wp-content/uploads/2020/06/sky-sports-logo-0-1.png"            
        },
        {
            "id": "sky-sport-260",
            "title": "Sky Sport 260",
            "name": "",
            "genres": ["Sport", "Sky"],
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
            "genres": ["Sport", "Sky"],
            "poster": "https://i.imgur.com/TWl58VI.png"
        },
        {
            "id": "sky-sport-uno",
            "title": "Sky Sport Uno",
            "name": "",
            "genres": ["Sport", "Sky"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/sky-sport-1_c.png"
        },
        {
            "id": "sky-sport-f1",
            "title": "Sky Sport F1",
            "name": "",
            "genres": ["Sport", "Sky"],
            "poster": "https://i1.wp.com/cache.pressmailing.net/thumbnail/story_hires/395b1e2f-a1c6-4cf6-9869-02155da4021f/Sky_F1_Logo.jpg.jpg"               
        },
        {
            "id": "sky-sport-motogp",
            "title": "Sky Sport MotoGP",
            "name": "",
            "genres": ["Sport", "Sky"],
            "poster": "https://img2.sport-tv-guide.live/images/tv-station-sky-sport-motogp-360.png"
        },
        {
            "id": "sky-sport-calcio",
            "title": "Sky Sport Calcio",
            "name": "",
            "genres": ["Sport", "Sky"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/sky-sport-2_c.png"
        },
        {
            "id": "sky-sport-arena",
            "title": "Sky Sport Arena",
            "name": "",
            "genres": ["Sport", "Sky"],
            "poster": "https://img2.sport-tv-guide.live/images/tv-station-sky-sport-arena-354.png"
        },
        {
            "id": "sky-sport-tennis",
            "title": "Sky Sport Tennis",
            "name": "",
            "genres": ["Sport", "Sky"],
            "poster": "https://pbs.twimg.com/profile_images/1752313472325431296/jr-YrkR6_400x400.png"
        },
        {
            "id": "sky-sport-nba",
            "title": "Sky Sport NBA",
            "name": "",
            "genres": ["Sport", "Sky"],
            "poster": "https://www.nbareligion.com/wp-content/uploads/2019/09/sky-sport-nba.jpg"
        },
        {
            "id": "dazn-zona-a",
            "title": "DAZN Zona A",
            "name": "",
            "genres": ["Sport", "DAZN"],
            "poster": "https://i.ytimg.com/vi/0cEfGLq-tz4/maxresdefault.jpg"
        },
        {
            "id": "zona-dazn",
            "title": "ZONA DAZN",
            "name": "",
            "genres": ["Sport", "DAZN"],
            "poster": "https://www.digital-news.it/img/palinsesti/2023/12/1701423631-zona-dazn.webp"
        },
        {
            "id": "dazn-1",
            "title": "DAZN 1",
            "name": "",
            "genres": ["Sport", "DAZN"],
            "poster": "https://i.ytimg.com/vi/0cEfGLq-tz4/maxresdefault.jpg"
        },
        {
            "id": "dazn-2",
            "title": "DAZN 2",
            "name": "",
            "genres": ["Sport", "DAZN"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/DAZN_2.svg/882px-DAZN_2.svg.png"
        },
        {
            "id": "eurosport-1",
            "title": "Eurosport 1",
            "name": "",
            "genres": ["Sport", "Discovery"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/eurosport-1_c.png"
        },
        {
            "id": "eurosport-2",
            "title": "Eurosport 2",
            "name": "",
            "genres": ["Sport", "Discovery"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/eurosport-2_c.png"
        },
        {
            "id": "dmax",
            "title": "DMAX",
            "name": "",
            "genres": ["Discovery"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/d-max_c.png",
            "url": "https://amg16146-wbdi-amg16146c8-samsung-it-1841.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-dmax-samsungit/playlist.m3u8"
        },
        {
            "id": "foodnetwork",
            "title": "Food Network",
            "name": "",
            "genres": ["Discovery"],
            "poster":"https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Food_Network_logo.svg/1024px-Food_Network_logo.svg.png",
            "url": "https://amg16146-wbdi-amg16146c3-samsung-it-1836.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-foodnetwork-samsungit/playlist.m3u8"
        },
        {
            "id": "frisbee",
            "title": "Frisbee",
            "name": "",
            "genres": ["Discovery"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/FRISBEE_LOGO_2015.png/1280px-FRISBEE_LOGO_2015.png",
            "url": "https://amg16146-wbdi-amg16146c7-samsung-it-1840.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-frisbee-samsungit/playlist.m3u8"
        },
        {
            "id": "giallo",
            "title": "Giallo",
            "name": "",
            "genres": ["Discovery"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/giallo_c.png",
            "url": "https://amg16146-wbdi-amg16146c5-samsung-it-1838.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-giallo-samsungit/playlist.m3u8"
        },
        {
            "id": "hgtv",
            "title": "HGTV",
            "name": "",
            "genres": ["Discovery"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/HGTV_2010.svg/1920px-HGTV_2010.svg.png",
            "url": "https://amg16146-wbdi-amg16146c9-samsung-it-1842.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-hgtv-samsungit/playlist.m3u8"
        },
        {
            "id": "k2",
            "title": "K2",
            "name": "",
            "genres": ["Discovery"],
            "poster": "https://upload.wikimedia.org/wikipedia/it/thumb/7/70/K2_logo_%282013%29.svg/800px-K2_logo_%282013%29.svg.png",
            "url": "https://amg16146-wbdi-amg16146c6-samsung-it-1839.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-k2-samsungit/playlist.m3u8"
        },
        {
            "id": "nove",
            "title": "Nove",
            "name": "",
            "genres": ["Discovery"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/nove_c.png",
            "url": "https://amg16146-wbdi-amg16146c1-samsung-it-1831.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-nove-samsungit/playlist.m3u8"
        },

        {
            "id": "realtime",
            "title": "Real Time",
            "name": "",
            "genres": ["Discovery"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/real-time_c.png",
            "url": "https://amg16146-wbdi-amg16146c2-samsung-it-1835.playouts.now.amagi.tv/playlist/amg16146-warnerbrosdiscoveryitalia-realtime-samsungit/playlist.m3u8"
        },
        {
            "id": "supertennis",
            "title": "Super Tennis",
            "name": "",
            "genres": ["Sport"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/0/02/SUPERTENNIS_HD.png",
            "url": "https://live-embed.supertennix.hiway.media/restreamer/supertennix_client/gpu-a-c0-16/restreamer/rtmp/hls/h24_supertennix/manifest.m3u8"
        },
        {
            "id": "solocalcio",
            "title": "Solo Calcio",
            "name": "",
            "genres": ["Sport"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/SI_Live_24_logo_%282019%29.svg/1280px-SI_Live_24_logo_%282019%29.svg.png",  
            "url": "https://di-kzbhv8pw.vo.lswcdn.net/sportitalia/sisolocalcio/playlist.m3u8" 
        },
        {
            "id": "sportitalia",
            "title": "Sportitalia",
            "name": "",
            "genres": ["Sport"],
            "poster": "https://upload.wikimedia.org/wikipedia/en/5/55/Sportitalia.jpg",
            "url": "https://di-kzbhv8pw.vo.lswcdn.net/sportitalia/sihd/playlist.m3u8"
        },
        {
            "id": "sportitalia24",
            "title": "Sportitalia 24",
            "name": "",
            "genres": ["Sport"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/SI_Live_24_logo_%282019%29.svg/1280px-SI_Live_24_logo_%282019%29.svg.png",
            "url": "https://di-kzbhv8pw.vo.lswcdn.net/sportitalia/sihd/playlist.m3u8"
        },
        {
            "id": "rsi-la-1",
            "title": "RSI LA 1",
            "name": "",
            "genres": ["RSI"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/RSI_La_1_2012.svg/2880px-RSI_La_1_2012.svg.png"
        },
        {
            "id": "rsi-la-2",
            "title": "RSI LA 2",
            "name": "",
            "genres": ["RSI"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/RSI_La_2_2012.svg/2880px-RSI_La_2_2012.svg.png"    
        },
        {
            "id": "sky-primafila-1",
            "title": "SKY PRIMAFILA 1",
            "name": "",
            "genres": ["Film", "Sky"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-primafila-it.png"
        },
        {
            "id": "sky-primafila-2",
            "title": "SKY PRIMAFILA 2",
            "name": "",
            "genres": ["Film", "Sky"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-primafila-it.png"
        },
        {
            "id": "sky-primafila-3",
            "title": "SKY PRIMAFILA 3",
            "name": "",
            "genres": ["Film", "Sky"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-primafila-it.png"
        },
        {
            "id": "sky-primafila-4",
            "title": "SKY PRIMAFILA 4",
            "name": "",
            "genres": ["Film", "Sky"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-primafila-it.png"
        },
        {
            "id": "sky-primafila-5",
            "title": "SKY PRIMAFILA 5",
            "name": "",
            "genres": ["Film", "Sky"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-primafila-it.png"
        },
        {
            "id": "sky-primafila-6",
            "title": "SKY PRIMAFILA 6",
            "name": "",
            "genres": ["Film", "Sky"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-primafila-it.png"
        },
        {
            "id": "sky-primafila-7",
            "title": "SKY PRIMAFILA 7",
            "name": "",
            "genres": ["Film", "Sky"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-primafila-it.png"
        },
        {
            "id": "sky-primafila-8",
            "title": "SKY PRIMAFILA 8",
            "name": "",
            "genres": ["Film", "Sky"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-primafila-it.png"
        },
        {
            "id": "sky-primafila-9",
            "title": "SKY PRIMAFILA 9",
            "name": "",
            "genres": ["Film", "Sky"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-primafila-it.png"
        },
        {
            "id": "sky-primafila-10",
            "title": "SKY PRIMAFILA 10",
            "name": "",
            "genres": ["Film", "Sky"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-primafila-it.png"
        },
        {
            "id": "sky-primafila-11",
            "title": "SKY PRIMAFILA 11",
            "name": "",
            "genres": ["Film", "Sky"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-primafila-it.png"
        },
        {
            "id": "sky-primafila-12",
            "title": "SKY PRIMAFILA 12",
            "name": "",
            "genres": ["Film", "Sky"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-primafila-it.png"
        },
        {
            "id": "sky-primafila-13",
            "title": "SKY PRIMAFILA 13",
            "name": "",
            "genres": ["Film", "Sky"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-primafila-it.png"
        },
        {
            "id": "sky-primafila-14",
            "title": "SKY PRIMAFILA 14",
            "name": "",
            "genres": ["Film", "Sky"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-primafila-it.png"
        },
        {
            "id": "sky-primafila-15",
            "title": "SKY PRIMAFILA 15",
            "name": "",
            "genres": ["Film", "Sky"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-primafila-it.png"
        },
        {
            "id": "sky-primafila-16",
            "title": "SKY PRIMAFILA 16",
            "name": "",
            "genres": ["Film", "Sky"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-primafila-it.png"
        },
        {
            "id": "sky-primafila-17",
            "title": "SKY PRIMAFILA 17",
            "name": "",
            "genres": ["Film", "Sky"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-primafila-it.png"
        },
        {
            "id": "sky-primafila-18",
            "title": "SKY PRIMAFILA 18",
            "name": "",
            "genres": ["Film", "Sky"],
            "poster": "https://raw.githubusercontent.com/tv-logo/tv-logos/main/countries/italy/sky-primafila-it.png"
        },
        {
            "id": "top-gear",
            "title": "Top Gear TV",
            "name": "",
            "genres": ["Pluto"],
            "poster": "https://upload.wikimedia.org/wikipedia/de/b/b9/TopGearLogo.jpg",
            "url": "https://service-stitcher.clusters.pluto.tv/v1/stitch/embed/hls/channel/64c109a4798def0008a6e03e/master.m3u8?deviceId=channel&deviceModel=web&deviceVersion=1.0&appVersion=1.0&deviceType=rokuChannel&deviceMake=rokuChannel&deviceDNT=1&advertisingId=channel&embedPartner=rokuChannel&appName=rokuchannel&is_lat=1&bmodel=bm1&content=channel&platform=web&tags=ROKU_CONTENT_TAGS&coppa=false&content_type=livefeed&rdid=channel&genre=ROKU_ADS_CONTENT_GENRE&content_rating=ROKU_ADS_CONTENT_RATING&studio_id=viacom&channel_id=channel"
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

STATIC_CHANNELS_DATA = [
    {
        "id": "sky-uno", # ID originale del canale
        "title": "Sky Uno",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skyuno)/master_2hr-aac.mpd&key_id=1115002b32ddb67077a31b31cc1b03c1&key=bc1a933a25b36aeed12a60f149157a3d",
        "group": "MPD"
    },
    {
        "id": "sky-atlantic",
        "title": "Sky Atlantic",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skyserie)/master_2hr-aac.mpd&key_id=1115bf01aeadce32fcec6a220375a3fa&key=9df360a2a22411897cd8b1bc48c0afc0",
        "group": "MPD"
    },
    {
        "id": "sky-sport-24",
        "title": "Sky Sport 24",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skysport24)/master_2hr-aac.mpd&key_id=11151447a65b31d6cb78dd022cb67e8d&key=1d6be453be1e607c133a28826d509a86",
        "group": "MPD"
    },
    {
        "id": "sky-sport-uno",
        "title": "Sky Sport Uno",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skysportuno)/master_2hr-aac.mpd&key_id=1115ca7bae09bbf4364eba27291b88a1&key=a38624a3b373a79e810f3b20cc295096",
        "group": "MPD"
    },
    {
        "id": "sky-sport-calcio",
        "title": "Sky Sport Calcio",
        "url": "https://g003-lin-it-cmaf-prd-cf.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skysportcalcio)/master_2hr-aac.mpd&key_id=11158d8e6031888c16efac25c601f64b&key=0f3bfab5a64037ac8711e58aac24a292",
        "group": "MPD"
    },
    {
        "id": "sky-sport-f1",
        "title": "Sky Sport F1",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skysportf1)/master_2hr-aac.mpd&key_id=11155522b79e825f8cdfd7967a31da4c&key=549190d194a655561f5099427a809812",
        "group": "MPD"
    },
    {
        "id": "sky-sport-motogp",
        "title": "Sky Sport MotoGP",
        "url": "https://g003-lin-it-cmaf-prd-cf.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skysportmotogp)/master_2hr-aac.mpd&key_id=11153aff5496be1a206a178ab3c1c078&key=806eb5923c951bd205257282de834740",
        "group": "MPD"
    },
    {
        "id": "sky-sport-arena",
        "title": "Sky Sport Arena",
        "url": "https://g003-lin-it-cmaf-prd-cf.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skysportarena)/master_2hr-aac.mpd&key_id=1115f90a6831fa7ca058a30383cb0652&key=6c086c2a0a8de8c1f413e4128246abdd",
        "group": "MPD"
    },
    {
        "id": "sky-sport-tennis",
        "title": "Sky Sport Tennis",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skysporttennis)/master_2hr-aac.mpd&key_id=111587fedaf11c03f2140b3e53ff5a5b&key=4192c4108bb887cbd33dc69afabc8096",
        "group": "MPD"
    },
    {
        "id": "sky-sport-nba",
        "title": "Sky Sport NBA",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skysportnba)/master_2hr-aac.mpd&key_id=111509ad5d16918190d8ceb1afa3c2c2&key=5369df3ee38ad965da555846bfa61a37",
        "group": "MPD"
    },
    {
        "id": "sky-sport-max",
        "title": "Sky Sport Max",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skysportmax)/master_2hr-aac.mpd&key_id=11155656191f1c60af13deb6a20f0354&key=95448b624c83d9a9719342cf1ab3e157",
        "group": "MPD"
    },
    {
        "id": "sky-sport-golf",
        "title": "Sky Sport Golf",
        "url": "https://linear309-it-dash1-prd-akp2.cdn13.skycdp.com/016a/32768/FHD/skysportgolf/master.mpd&key_id=00360b7729f74bf56a0a4eb0eda15ec5&key=f8a5f4723c71ac84c2f1ff6f55939a63",
        "group": "MPD"
    },
    {
        "id": "eurosport-1",
        "title": "Eurosport 1",
        "url": "https://g003-lin-it-cmaf-prd-cf.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(eurosport1)/master_2hr-aac.mpd&key_id=11158bc4ef31195cc0e9f93bcb99b8e0&key=1e3169483337e73d3d4646931197b062",
        "group": "MPD"
    },
    {
        "id": "eurosport-2",
        "title": "Eurosport 2",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(eurosport2)/master_2hr-aac.mpd&key_id=1115097a6b5a2cc55c2f6e9c65043ed7&key=2f82bc6a71fad0a0646936c2b0099c73",
        "group": "MPD"
    },
    {
        "id": "sky-sport-251",
        "title": "Sky Sport Calcio 1",
        "url": "https://g003-lin-it-cmaf-prd-cf.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skysport251)/master_2hr-aac.mpd&key_id=11151be3428480868250f38fd1b7f372&key=43c8bf86dc2f6cba8778e7cdff0496cd",
        "group": "MPD"
    },
    {
        "id": "sky-sport-252",
        "title": "Sky Sport Calcio 2",
        "url": "https://g003-lin-it-cmaf-prd-cf.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skysport252)/master_2hr-aac.mpd&key_id=1115ef7a71a700a8a00d028fd70dc4be&key=8742adddc304a5e3aa5376879b02888c",
        "group": "MPD"
    },
    {
        "id": "sky-sport-253",
        "title": "Sky Sport Calcio 3",
        "url": "https://g003-lin-it-cmaf-prd-cf.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skysport253)/master_2hr-aac.mpd&key_id=11151848f262b43a21d7a61bc958c6aa&key=400f5a392c6c5893643b8df74a0e1eec",
        "group": "MPD"
    },
    {
        "id": "sky-sport-254",
        "title": "Sky Sport Calcio 4",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skysport254)/master_2hr-aac.mpd&key_id=11159862c693989cb235f5371dd11fba&key=25e15b3762a2cfc26d471324f197aff6",
        "group": "MPD"
    },
    {
        "id": "sky-sport-255",
        "title": "Sky Sport Calcio 5",
        "url": "https://g003-lin-it-cmaf-prd-cf.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skysport255)/master_2hr-aac.mpd&key_id=111545473a34f1fe05aae0e10700a7e3&key=fdee7c55cb25797ea9918644f3db4ef5",
        "group": "MPD"
    },
    {
        "id": "sky-sport-256",
        "title": "Sky Sport Calcio 6",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skysport256)/master_2hr-aac.mpd&key_id=1115e30272b48b327a666414728f89c0&key=e17fd69cf15cd8e9a57b3b2127f7e0bc",
        "group": "MPD"
    },
    {
        "id": "sky-sport-257",
        "title": "Sky Sport Calcio 7",
        "url": "https://g003-lin-it-cmaf-prd-cf.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skysport257)/master_2hr-aac.mpd&key_id=111550e7ba986b365bcc67dd01cdd27e&key=c292fe7e970841aa795e8832414c5b2e",
        "group": "MPD"
    },
    {
        "id": "sky-sport-258",
        "title": "Sky Sport Calcio 8",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skysport258)/master_2hr-aac.mpd&key_id=1115bb0040c6d04b822da9ae1af8977d&key=c80ba56fdee7782313a33691e9cc2146",
        "group": "MPD"
    },
    {
        "id": "sky-sport-259",
        "title": "Sky Sport Calcio 9",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skysport259)/master_2hr-aac.mpd&key_id=11158627294fcbd5e724e2b521c87aeb&key=c26bc6e33e8f39dc748f66885935a63f",
        "group": "MPD"
    },
    {
        "id": "sky-cinema-uno",
        "title": "Sky Cinema Uno",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skycinemauno)/master_2hr-aac.mpd&key_id=111571675d8183ed169725564cded6d9&key=e077dedf383c8aed73d38567a8e6a046",
        "group": "MPD"
    },
    {
        "id": "sky-cinema-due",
        "title": "Sky Cinema Due",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skycinemadue)/master_2hr-aac.mpd&key_id=11152c4ea1a3bffdd277ce333e54631a&key=17f0c028800dbcb294b9aebbae1f7e0c",
        "group": "MPD"
    },
    {
        "id": "sky-cinema-comedy",
        "title": "Sky Cinema Comedy",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skycinemacomedy)/master_2hr-aac.mpd&key_id=1115676eca79233f2919b53f1a1709b8&key=72298a31b1b015b52adc03ab222494c2",
        "group": "MPD"
    },
    {
        "id": "sky-cinema-action",
        "title": "Sky Cinema Action",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skycinemaaction)/master_2hr-aac.mpd&key_id=11150443883da4df27e25110d10fca31&key=83b6390471a083e00f8f3aff2a271be9",
        "group": "MPD"
    },
    {
        "id": "sky-cinema-family",
        "title": "Sky Cinema Family",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skycinemafamily)/master_2hr-aac.mpd&key_id=1115074065832f74af7e279e1203adce&key=20ece4131fbec82ac7ff056838512143",
        "group": "MPD"
    },
    {
        "id": "sky-cinema-collection",
        "title": "Sky Cinema Collection",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skycinemacollection)/master_2hr-aac.mpd&key_id=11155d8a1fe0b211137c206354e16d2a&key=7f07d0ef693893a84162d51c1c7259f3",
        "group": "MPD"
    },
    {
        "id": "sky-cinema-drama",
        "title": "Sky Cinema Drama",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skycinemadrama)/master_2hr-aac.mpd&key_id=11155ad807b90b9570fb8cce067f6166&key=74c4430ed8142190e52d4b303286696f",
        "group": "MPD"
    },
    {
        "id": "sky-cinema-suspense",
        "title": "Sky Cinema Suspense",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skycinemasuspense)/master_2hr-aac.mpd&key_id=1115d04562a1c328a84b2dab41244cba&key=5cf8c65d4177349308d7043384880659",
        "group": "MPD"
    },
    {
        "id": "sky-cinema-romance",
        "title": "Sky Cinema Romance",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skycinemaromance)/master_2hr-aac.mpd&key_id=1115dbeea57d2fadedc278956bcbfb02&key=3eee23f97ae49a81c03356599a614fca",
        "group": "MPD"
    },
    {
        "id": "sky-serie",
        "title": "Sky Serie",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skyserie)/master_2hr-aac.mpd&key_id=1115bf01aeadce32fcec6a220375a3fa&key=9df360a2a22411897cd8b1bc48c0afc0",
        "group": "MPD"
    },
    {
        "id": "sky-crime",
        "title": "Sky Crime",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skycrime)/master_2hr-aac.mpd&key_id=1115aa47cfa18cf73cb6f936cff1f8ee&key=a27e7383d481596cc34334336d3e7219",
        "group": "MPD"
    },
    {
        "id": "sky-investigation",
        "title": "Sky Investigation",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skyinvestigation)/master_2hr-aac.mpd&key_id=11153dd8de63f9748252104afd6b7405&key=255e0c5bb81bde9602d8746080496e04",
        "group": "MPD"
    },
    {
        "id": "sky-documentaries",
        "title": "Sky Documentaries",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skydocumentaries)/master_2hr-aac.mpd&key_id=111556afa3ac362bbf6d6237a0096793&key=b80627550521e85d0997e3447245f7ff",
        "group": "MPD"
    },
    {
        "id": "sky-nature",
        "title": "Sky Nature",
        "url": "https://g003-lin-it-cmaf-prd-cf.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skynature)/master_2hr-aac.mpd&key_id=111553a2ff74eff230c8bb72efc0504c&key=80ec2c7f64b97098f4f65a15d828ce6a",
        "group": "MPD"
    },
    {
        "id": "history",
        "title": "History Channel",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(historychannel)/master_2hr-aac.mpd&key_id=11158db9a2522642c8da56416d94c6a3&key=edb6a56266dde53f013d170d46b0b265",
        "group": "MPD"
    },
    {
        "id": "sky-arte",
        "title": "Sky Arte",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(skyarte)/master_2hr-aac.mpd&key_id=11158d61157893c665c5ec942528d020&key=2d4b7343dd929afbbd61ef0aa37366d9",
        "group": "MPD"
    },
    {
        "id": "mtv",
        "title": "MTV",
        "url": "https://g003-lin-it-cmaf-prd-ak.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(mtv)/master_2hr-aac.mpd&key_id=111559b5e50a4be12901e456034285a3&key=2fedd4c9c3be1b7f90e86c7bc44131f8",
        "group": "MPD"
    },
    {
        "id": "comedy-central",
        "title": "Comedy Central",
        "url": "https://g003-lin-it-cmaf-prd-cf.pcdn07.cssott02.com/nowitlin1/Content/CMAF_CTR_S1/Live/channel(comedycentral)/master_2hr-aac.mpd&key_id=11155778dc9b7dde1e396a9110f09208&key=c030cf978cbdc4a4c84fc68ab467942b",
        "group": "MPD"
    },
    {
        "id": "dazn-1",
        "title": "DAZN 1",
        "url": "https://abe6fjxaaaaaaaamc4pg55ekcyqz4.otte.live.cf.ww.aiv-cdn.net/dub-nitro/live/clients/dash/enc/lgk8kppclc/out/v1/f51173b6b0624a4386358ab8dfee257f/cenc.mpd&key_id=8272bf6ba46f23f9da5270057b6e028a&key=74ae70dd10b4bb38ed6ffe843f3e2ccd",
        "group": "MPD"
    }
]

# Questo dizionario mappa un nome di canale (che corrisponde a 'id.replace("-", " ")' da STREAM)
# a una lista di chiavi dei provider OMGTV ("daddy", "vavoo", "calcionew", "mpdstatic")
# dove è probabile trovare il canale.
tv_provider_map = {
    "sky uno": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky atlantic": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky sport uno": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky sport calcio": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky sport f1": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky sport 24": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky sport motogp": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky sport arena": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky sport tennis": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky sport nba": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky sport max": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky sport golf": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky sport 251": ["dlhd", "mpdstatic", "calcionew"],
    "sky sport 252": ["dlhd", "mpdstatic", "calcionew"],
    "sky sport 253": ["dlhd", "mpdstatic", "calcionew"],
    "sky sport 254": ["dlhd", "mpdstatic", "calcionew"],
    "sky sport 255": ["dlhd", "mpdstatic", "calcionew"],
    "sky sport 256": ["dlhd", "mpdstatic", "calcionew"],
    "sky sport 257": ["dlhd", "mpdstatic", "calcionew"],
    "sky sport 258": ["dlhd", "mpdstatic", "calcionew"],
    "sky sport 259": ["dlhd", "mpdstatic", "calcionew"],
    "sky cinema uno": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky cinema due": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky cinema comedy": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky cinema drama": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky cinema family": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky cinema romance": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky cinema suspence": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky cinema collection": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky cinema action": ["dlhd", "mpdstatic", "calcionew", "vavoo"], # Basato sulla tua lista per "sky-cinema-action"
    "sky arte": ["calcionew", "vavoo", "mpdstatic"],
    "sky serie": ["dlhd", "mpdstatic", "calcionew", "vavoo"], # Basato sulla tua lista per "sky-serie"
    "sky nature": ["calcionew", "vavoo", "mpdstatic"],
    "sky crime": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky documentaries": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "sky investigation": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "eurosport 1": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "eurosport 2": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "dazn 1": ["dlhd", "mpdstatic", "calcionew", "vavoo"],
    "rai 1": ["dlhd", "vavoo"],
    "rai 2": ["dlhd", "vavoo"],
    "rai 3": ["dlhd", "vavoo"],
    "italia 1": ["dlhd", "vavoo"],
    "rete 4": ["dlhd", "vavoo"],
    "canale 5": ["dlhd", "vavoo"],
    "la7": ["dlhd", "vavoo"],
    "tv8": ["dlhd", "vavoo"],
    "nove": ["dlhd", "vavoo"],
    "dmax": ["dlhd", "vavoo"],
    "realtime": ["dlhd", "vavoo"], # STREAM ID è "realtime", la tua chiave era "real-time"
    "focus": ["dlhd", "vavoo"],
    "cielo": ["dlhd", "vavoo"],
    "comedy central": ["calcionew", "vavoo", "mpdstatic"],
    "history": ["calcionew", "vavoo", "mpdstatic"],
    "sportitalia": ["calcionew", "vavoo", "mpdstatic"], # STREAM ID è "sportitalia", la tua chiave era "sport-italia"
}

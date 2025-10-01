import Src.Utilities.config as config

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
            "name": "Full HD ",
            "genres": ["Rai"],
            "poster": "https://i.imgur.com/bb72vqh.jpeg",
            "url": "https://viamotionhsi.netplus.ch/live/eds/rai1/browser-HLS8/rai1.m3u8"
        },
        {
            "id": "rai-2",
            "title": "Rai 2",
            "name": "Full HD ",
            "genres": ["Rai"],
            "poster": "https://i.imgur.com/jX95Qod.jpeg",
            "url": "https://viamotionhsi.netplus.ch/live/eds/rai2/browser-HLS8/rai2.m3u8"
        },
        {
            "id": "rai-3",
            "title": "Rai 3",
            "name": "Full HD ",
            "genres": ["Rai"],
            "poster": "https://i.imgur.com/fgAh9if.jpeg",
            "url": "https://viamotionhsi.netplus.ch/live/eds/rai3/browser-HLS8/rai3.m3u8"
        },
        {
            "id": "rai-4",
            "title": "Rai 4",
            "name": "Full HD ",
            "genres": ["Rai"],
            "poster": "https://i.imgur.com/NryLzhA.jpeg",
            "url": "https://raiquattro1-dash-live.akamaized.net/dash/live/663977/raiquattro1/manifest.mpd"
        },
        {
            "id": "rai-premium",
            "title": "Rai Premium",
            "name": "Full HD",
            "genres": ["Rai"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/rai-premium_c.png",
            "url": "https://raipremium1-dash-live.akamaized.net/dash/live/663979/raipremium1/manifest.mpd" 
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
            "url": "https://streamcdnb2-8e7439fdb1694c8da3a0fd63e4dda518.msvdn.net/rainews1/hls/playlist_mo.m3u8"
        },
        {
            "id": "rai-movie",
            "title": "Rai Movie",
            "name": "",
            "genres": ["Rai"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/rai-movie_c.png",
            "url": "https://raimovie1-dash-live.akamaized.net/dash/live/663983/raimovie1/manifest.mpd"
        },
        {
            "id": "rai-sport",
            "title": "Rai Sport",
            "name": "",
            "genres": ["Rai"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/rai-sport_c.png",
            "url": "https://viamotionhsi.netplus.ch/live/eds/raisport1/browser-HLS8/raisport1.m3u8"
        },
        {
            "id": "rete-4",
            "title": "Rete 4",
            "name": "Full HD",
            "genres": ["Mediaset"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Rete_4_2018.svg/1024px-Rete_4_2018.svg.png",
            "url": "https://live02-seg.msf.cdn.mediaset.net/live/ch-r4/r4-clr.isml/index.m3u8"
        },
        {
            "id": "euronews",
            "title": "Euronews",
            "name": "720p",
            "genres": ["Euronews"],
            "poster": "https://yt3.googleusercontent.com/t3slq37NYJRuP2UoEZDoPKyMClKyQULG8-j2DEfzL1XXcBvFpR6z6HD7rtc0wDn8Mqt0OtpU=s900-c-k-c0x00ffffff-no-rj",
        },
        {
            "id": "canale-5",
            "title": "Canale 5",
            "name": "Full HD",
            "genres": ["Mediaset"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/canale-5_c.png",
            "url": "https://viamotionhsi.netplus.ch/live/eds/canale5/browser-HLS8/canale5.m3u8"
        },
        {
            "id": "italia-1",
            "title": "Italia 1",
            "name": "Full HD",
            "genres": ["Mediaset"],
            "poster": "https://upload.wikimedia.org/wikipedia/en/thumb/e/e2/Italia_1.svg/1024px-Italia_1.svg.png",
            "url": "https://viamotionhsi.netplus.ch/live/eds/italia1/browser-HLS8/italia1.m3u8"
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
            "id": "dmax",
            "title": "DMAX",
            "name": "",
            "genres": ["Warner Bros"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/d-max_c.png",
            "url": "https://d2j2nqgg7bzth.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-02k1gv1j0ufwn/DMAX_IT.m3u8"
        },
        {
            "id": "foodnetwork",
            "title": "Food Network",
            "name": "",
            "genres": ["Warner Bros"],
            "poster":"https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Food_Network_logo.svg/1024px-Food_Network_logo.svg.png",
            "url": "https://dk3okdd5036kz.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-o4pw0nc02sthz/Foodnetwork_IT.m3u8"
        },
        {
            "id": "frisbee",
            "title": "Frisbee",
            "name": "",
            "genres": ["Warner Bros"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/FRISBEE_LOGO_2015.png/1280px-FRISBEE_LOGO_2015.png",
            "url": "https://d6m7lubks416z.cloudfront.net/v1/manifest/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-zmbstsedxme9s/2fbb852d-6778-4a74-955b-59164269c705/0.m3u8"
        },
        {
            "id": "giallo",
            "title": "Giallo",
            "name": "",
            "genres": ["Warner Bros"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/giallo_c.png",
            "url": "https://d9fqo6nfqlv2h.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-ulukbrgm1n3yb/Giallo_IT.m3u8"
        },
        {
            "id": "hgtv",
            "title": "HGTV",
            "name": "",
            "genres": ["Warner Bros"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/HGTV_2010.svg/1920px-HGTV_2010.svg.png",
            "url": "https://timlivetu0.cb.ticdn.it/Content/DASH/Live/channel(hgtvhd)/manifest.mpd"
        },
        {
            "id": "k2",
            "title": "K2",
            "name": "",
            "genres": ["Warner Bros"],
            "poster": "https://upload.wikimedia.org/wikipedia/it/thumb/7/70/K2_logo_%282013%29.svg/800px-K2_logo_%282013%29.svg.png",
            "url": "https://d1pmpe0hs35ka5.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-39hsskpppgf72/K2_IT.m3u8"
        },
        {
            "id": "nove",
            "title": "Nove",
            "name": "",
            "genres": ["Warner Bros"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/nove_c.png",
            "url": "https://d31mw7o1gs0dap.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-y5pbi2sq9r609/NOVE_IT.m3u8"
        },

        {
            "id": "realtime",
            "title": "Real Time",
            "name": "",
            "genres": ["Warner Bros"],
            "poster": "https://www.sorrisi.com/guidatv/bundles/tvscnewsite/css/images/loghi/real-time_c.png",
            "url": "https://d3562mgijzx0zq.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-kizqtzpvvl3i8/Realtime_IT.m3u8"
        },
        {
            "id": "supertennis",
            "title": "Super Tennis",
            "name": "",
            "genres": ["FIT"],
            "poster": "https://upload.wikimedia.org/wikipedia/commons/0/02/SUPERTENNIS_HD.png",
            "url": "https://live-embed.supertennix.hiway.media/restreamer/supertennix_client/gpu-a-c0-16/restreamer/outgest/aa3673f1-e178-44a9-a947-ef41db73211a/manifest.m3u8"
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
            "url": "https://origin.streamup.eu/sportitaliain/sisolocalcio/playlist.m3u8"
        },
        {
            "id": "rsi-la-2",
            "title": "RSI LA 2",
            "name": "",
            "genres": ["RSI"],
            "poster": "https://livehere.one/img/rsi.png",
            "url": "https://viamotionhsi.netplus.ch/live/eds/rsila2hd/browser-HLS8/rsila2hd.m3u8"    
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
            "id": "bizzarro-movies",
            "title": "Bizzarro Movies",
            "name": "",
            "genres": ["Rakuten"],
            "poster": "https://tvpnlogopeu.samsungcloud.tv/platform/image/sourcelogo/vc/00/02/34/ITBA3300024IU_20240214T034959SQUARE.png_20240214034959.png",
            "url": "https://797fbe152cbe418697be037aef3a708f.mediatailor.us-east-1.amazonaws.com/v1/master/44f73ba4d03e9607dcd9bebdcb8494d86964f1d8/Samsung-it_BizzarroMovies/playlist.m3u8"
        },
        {
            "id": "cinema-italiano",
            "title": "Cinema Italiano",
            "name": "",
            "genres": ["Rakuten"],
            "poster": "https://tvpnlogopeu.samsungcloud.tv/platform/image/sourcelogo/vc/00/02/34/ITBA33000238E_20240313T074122SQUARE.png",
            "url": "http://stitcher-ipv4.pluto.tv/v1/stitch/embed/hls/channel/608aa512d67fd900072323db/master.m3u8?deviceType=samsung-tvplus&deviceMake=samsung&deviceModel=samsung&deviceVersion=unknown&appVersion=unknown&deviceLat=0&deviceLon=0&deviceDNT=%7BTARGETOPT%7D&deviceId=%7BPSID%7D&advertisingId=%7BPSID%7D&us_privacy=1YNY&samsung_app_domain=%7BAPP_DOMAIN%7D&samsung_app_name=%7BAPP_NAME%7D&profileFloor=&profileLimit=&embedPartner=samsung-tvplus"
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

extra_sources = {
    "rai-1": ["https://ilglobotv-live.akamaized.net/channels/RAI1/Live.m3u8"],
    "rai-2": ["https://ilglobotv-live.akamaized.net/channels/RAI2/Live.m3u8"],
    "rai-3": ["https://ilglobotv-live.akamaized.net/channels/RAI2/Live.m3u8","https://dash2.antik.sk/live/test_rai_tre_tizen/playlist.m3u8","https://wzstreaming.rai.it/TVlive/liveStream/playlist.m3u8","https://list.iptvcat.com/my_list/s/1f22856f68f2fba4a993c47f47c78a64.m3u8","https://list.iptvcat.com/my_list/s/a372048a4fb440e752aec141aa02885f.m3u8","https://list.iptvcat.com/my_list/s/c7efe17aa0dc8096561967bfb828d4f3.m3u8","https://list.iptvcat.com/my_list/s/2d1f14bbb3370d263d8d3f0d9f5128e0.m3u8"],
    "rete-4":["https://tvit.leicaflorianrobert.dev/mediaset/rete-4/stream.m3u8","https://timlivetu0.cb.ticdn.it/Content/DASH/Live/channel(rete4)/manifest.mpd"],
    "canale-5":["https://timlivetu0.cb.ticdn.it/Content/DASH/Live/channel(canale5)/manifest.mpd","https://tvit.leicaflorianrobert.dev/mediaset/canale-5/stream.m3u8",'https://timlivetu0.cb.ticdn.it/Content/DASH/Live/channel(canale5)/manifest.mpd','https://live02-seg.msf.cdn.mediaset.net/live/ch-c5/c5-clr.isml/index.m3u8'],
    "italia-1":["https://tvit.leicaflorianrobert.dev/mediaset/italia-1/stream.m3u8","https://live02-seg.msf.cdn.mediaset.net/live/ch-i1/i1-clr.isml/index.m3u8",'https://timlivetu0.cb.ticdn.it/Content/DASH/Live/channel(italia1)/manifest.mpd'],
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

provider_map = {
        'SC': 'STREAMINGCOMMUNITY',
        'SC_MFP': 'SC_MFP',
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
        "ES": "EUROSTREAMING",
        "GO": "GUARDOSERIE",
        "GF": "GUARDAFLIX"
    }
okru = {
    "rai1": "https://ok.ru/videoembed/7703488765552?nochat=1",
    "rai2": "https://ok.ru/videoembed/7805618364016?nochat=1"
}

STREAM = {
    "channels": [
        {
            "id": "la7",
            "title": "LA7",
            "url": "https://d3749synfikwkv.cloudfront.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-74ylxpgd78bpb/Live.m3u8"
        },
        {
            "id": "rai1",
            "title": "Rai 1",
            "url": "https://m3u.iranvids.com/rai01/output.m3u8",
            "behaviorHints": {
                "notWebReady": True,
                "proxyHeaders": {
                    "request": {
                        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
                    }
                }
            }
        },
        {
            "id": "rai2",
            "title": "Rai 2",
            "url": "https://m3u.iranvids.com/rai02/output.m3u8"
        }
    ]
}

# MammaMia

A Stremio Addon for high quality HTTPS Stream in Italian

While hosting, this project, remember that Filmpertutti uses Mixdrop. Mixdrop only allows seeing the videos only from the same IP where they were generated so, if you want to scrape filmpertutti, you have to host this project locally. Else, you can only scrape streamingcommunity.  

  

# Installation

Install required packages

``
pip install -r requirements.txt
``

Then to start the Flask server just execute:
``
python3 run.py
``
# How to add to Stremio
Just paste the URL/manifest.json in your search bar.
# Enviroment Variables

| Enviroment Variable | Value |
|-------------------------|---|
|TMDB_KEY|INSERT YOUR API KEY HERE|
| FT_DOMAIN | INSERT FILMPERTUTTI DOMAIN |
|SC_DOMAIN |  INSERT STREAMINGCOMMUNITY DOMAIN|
|FILMPERTUTTI|Put "1" if you want Filmpertutti to be enabled, "0" if disabled Altought keep in mind that you will only be able to use it if you get the link from the same IP of your streaming server.|
|STREAMINGCOMMUNITY|Put "1" if enabled, "0" if disabled|



Here is [linked](https://developer.themoviedb.org/docs/getting-started) a tutorial about how to get a TMDB KEY
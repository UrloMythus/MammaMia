  

  

# MammaMia

  

  

  

A Stremio Addon for high quality HTTPS Streams in Italian
Movies, Series, Anime and Live TV are supported.

  

  

  

While hosting, this project, remember that Filmpertutti uses Mixdrop. Mixdrop only allows seeing the videos  from the same IP where they were generated so, if you want to scrape filmpertutti, you will have to host this project locally. Else, you can only scrape other providers.

  

  

Hosting your own instance is suggested, but you can use the public instance [linked](https://mammamia-urlo-mammamia.hf.space/) in the About Page of the repo.

  

  

  

# Installation

  

  

## Local

  

  

Install required packages

  

  

``pip install -r requirements.txt ``

  
  

Then to start the Flask server just execute:

  
  

``python3 run.py``

  
Remember to create a .env file with your TMDB Key. 
  

## Hugging Face

  

  

To host this project with Hugging Face, go to the [linked](https://huggingface.co/spaces/MammaMia-Urlo/MammaMia/) page and follow these steps

  

  

  

1. Create an Hugging Face Account

  

  

2. Click on three dots on the top (right) part of the screen

  

  

3. Click Duplicate this Space

  

  

4. Insert TMDB Key

  

  

5. Clone the Project

  

  

6. You are done!

  

  

7. To install it on Stremio altought, you will need the Direct URL. It can be found on three dots --> Embed This Space --> Direct URL

  

  

8. Do not forget to add /manifest.json

  9. The Addon will update everytime you restart the service but you will need to change the config.json manually each time if there are any changes. 
If you just want to syncronize with the public instance then there is a button in the settings to do so.  

  

On Hugging Face you are forced to use the 8080 port because it is the only one allowed to send/get network requests. Moreover, remember that load_env needs to be disabled (it should be by default if you clone the project from HF)

  

  

## Render

  

  

To install this project on [Render](https://render.com/) follow these steps:

  

  

1. Create an Account

  

  

2. Create a Web Service

  

  

3. Fork the repo and then connect it to Render

  

  

4. Among the other environment variables, put PORT = 8080. This is needed because render needs the Port given as an environment variable.

  

  

5. As build command put `` pip install -r requirements `` and as run command put ``python3 run.py ``

  

  

6. Then just finish Render Setup and you are done :)

  

Remember, load_env needs to be disabled in the config.json

  

  

  

  

# How to add to Stremio

  

  

Just paste the URL/manifest.json in your search bar.

  

  

# Enviroment Variables

  

  

  

| Enviroment Variable | Value |
|-------------------------|---|
|TMDB_KEY|INSERT YOUR API KEY HERE|

  

  

Here is [linked](https://developer.themoviedb.org/docs/getting-started) a tutorial about how to get a TMDB KEY

  

  

# Config

  

In the repo there is a config.json that you can modify to change some aspects of the addon like the domains of the sites. Down here all explained:

  

| Config | Value |
|-------------------------|---|
| Domain | The domain of the site, must be a string |
|enabled | If the site is enabled or not. "1" means true. "0" means false. Remember, there is no point in enabling filmpertutti on a remote server since it's IP-LOCKED|
|fast_search|"1" for enabled, "0" for disabled. It enables a faster search for supported Providers but in case there are two movies/series with the exactly same name then they might take the wrong one|
|load_env|Put "1" if enabled, "0" if disabled. It needs to be enabled if you need to load a .env file. On remote hosting services, like Hugging Face or Render, it needs to be disabled. |
|HOST| The host for the Flask APP|
|PORT| The port for the Flask APP. Default: 8080 |

  For now Mysterius must be kept disabled if you do not know what you are doing.
  For now Tantifilm, even if it's player is not IP-Locked, does not work on Hugging Face.

Check those links to get the new Domain for the providers.

[FILMPERTUTTI](https://filmpertuttiiii.nuovo.live/)

[STREAMINGCOMMUNITY](https://t.me/+jlXmmprhtakxYWJh)

[TANTIFILM](https://tantinuovo.com/tantifilm-nuovo-indirizzo/)

[STREAMINGWATCH](https://t.me/streamingwatch)

[LORDCHANNEL](https://t.me/+5MQwrb3eqb81NGI0)

[ANIMEWORLD](https://t.me/AnimeWorldITA2)

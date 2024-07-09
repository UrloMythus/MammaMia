# MammaMia

A Stremio Addon for high quality HTTPS Stream in Italian

While hosting, this project, remember that Filmpertutti uses Mixdrop. Mixdrop only allows seeing the videos only from the same IP where they were generated so, if you want to scrape filmpertutti, you have to host this project locally. Else, you can only scrape streamingcommunity.  
Hosting your own instance is suggested but you can use the public instance [linked](https://mammamia-urlo-mammamia.hf.space/) in the About Page of the repo. 
  

# Installation
## Local
Install required packages

``
pip install -r requirements.txt
``

Then to start the Flask server just execute:
``
python3 run.py
``
## Hugging Face
To host this project with Hugging Face, go to the  [linked](https://huggingface.co/spaces/MammaMia-Urlo/MammaMia/) page and follow these steps

 1. Create an Hugging Face Account
 2. Click on three dots on the top (right) part of the screen
 3. Click Duplicate this Space
 4. Insert TMDB Key
 5. Clone the Project
 6. You are done! 
 7. To install it on Stremio altought, you will need the Direct URL. It can be found on three dots --> Embed This Space --> Direct URL
 8. Do not forget to add /manifest.json
 On Hugging Face you are forced to use the 8080 port because it is the only one allowed to send/get network requests.
## Render
To install this project on [Render](https://render.com/) follow these steps:
 1. Create an Account
 2. Create a Web Service
 3. Clone the repo
 4. Among the other environment variables, put PORT = 8080. This is needed because render needs the Port given as an environment variable. 
 5. As build command put `` pip install -r requirements `` and as run command put ``python3 run.py ``
 6. Then just finish Render Setup and you are done :)

 
 

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




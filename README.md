
  

  

# MammaMia

  

  

  

  

A Stremio Addon for  HTTPS Streams in Italian

Movies, Series, Anime and Live TV are supported.

 
  

  

  

  

# Installation

  

  

  

## Local

  

  

  

1. Install required packages

  

  

  

``pip install -r requirements.txt ``

2. If you want to use Eurostreaming install those packages:
    
- Linux (Debian/Ubuntu):
  ``sudo apt install tesseract-ocr libtesseract-dev ``

- Windows: Install the following library from this [link](https://github.com/UB-Mannheim/tesseract/wiki)

- MacOS: ```brew install tesseract```


Then install the following Python package:

 ``pip install pytesseract ``

  3. Create a .env file and fill it (look at example.env)

4. Modify the config.json as you wish 
    

  

4. Then to start the Fast API app server just execute:

  

  

``python3 run.py``

  



  

## Hugging Face

  

  

  

To host this project with Hugging Face you will need a Github Account, a Hugging Face account and a  [TMDB KEY](https://www.educative.io/courses/movie-database-api-python/set-up-the-credentials).

  

  

  

  

1. Fork this project and give it  a random name. 

[!WARNING] The name must not be related to Mamma Mia or mediaflowproxy. Just use a random name 

2. Go on the Github of the [Repo](https://github.com/UrloMythus/MammaMia/), click on Fork -> Create New Fork -> Create One. 

3. Click on static directory and then click on static.py. Remove the whole content and put:
```
HTML = """
Whatever you want
"""
```
4. Change ```Whatever you want``` with a random phrase (the longer it is, the better it is). If you are too lazy go to this [link](https://www.thewordfinder.com/random-sentence-generator/) and generate it.
 
5. Click Commit Changes
[!WARNING] Since the main page doesn't exist  anymore, you will need to configure MammaMia from /configure endpoint


6. Go to [linked](https://huggingface.co/login?next=%2Fnew-space) page and create a new Public Docker Space.
[!WARNING] The Space must be Public or else you won't be able to access it 


7. Go to Settings and in ```Variables and secrets``` section click New Secret. As ```Name```  put TMDB_KEY and as ```Value`` put your TMDB Key

8. Go to Files  and click Contribute -> Create a new file 
 
9. In ```Name your file``` field put ```Dockerfile``` . Inside the text box put the content of the Dockerfile called ```Dockerfile-auto-update-no-config``` which you will find inside the /Dockerfiles directory of your Github Fork. 

10. Where there is "YourUsername" put your Github username and where there is "YourRepoName" insert the name of the fork. 
[!WARNING] Don't remove the final . or it won't work

11. When you are done click Commit Changes to main

12. Go to the README.md in the Files section of your HuggingFace's space and click on it. After that click on edit. After ```pinned: false``` insert this  ```app_port: 8080```

13. When you are done click Commit Changes to main

14. You are done!


  

15. To install it on Stremio  you will need the Direct URL. It can be found on three dots --> Embed This Space --> Direct URL      
   If you do not find it it means your space is Private. To fix so go to Settings and click Set Visibility to Public. 

 
  

 
16. How to handle updates: First of all you will need to go to your GitHub Repo and click Sync Changes (without discarding commits). Then go into your HuggingFace Space ---> Settings ---> Factory Reset
  

  

  

## Render



  

  

To install this project on [Render](https://render.com/) follow these steps:

[!WARNING] Render might ban your account. Modify the static.py file might help with that


  

  

1. Create an Account

  

  

  

2. Create a Web Service

  

  

  

3. Fork the repo and then connect it to Render

  

  

  

4. Aside from usual enviroment variables you will need to put PORT = 8080. 

  

  

  

5. As build command put `` pip install -r requirements `` and as run command put ``python3 run.py ``

  

  

  

6. Then just finish Render Setup and you are done :)

  

  

Remember, load_env  needs to be disabled in the config.json
  

  

# Vercel
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FUrloMythus%2FMammaMia&env=PORT,TMDB_KEY&envDescription=PORT%20(8080)%20and%20API%20KEY%20of%20TMDB&envLink=https%3A%2F%2Fgithub.com%2FUrloMythus%2FMammaMia%2Fblob%2Fmain%2Fexample.env)



  


  

  

  

# Enviroment Variables

  

  

  

  

| Enviroment Variable | Value |
|-------------------------|---|
|TMDB_KEY|INSERT YOUR API KEY HERE|
|FORWARDPROXY| "YOURFORWARDPROXY/"  |
|PROXY |  ["PROXY1","PROXY2"]|

  

Tutorial to get the TMDB Key: [Tutorial](https://www.themoviedb.org/settings/api)

  

  

  

# Config

  

  

In the repo there is a config.json that you can modify to change some aspects of the addon like the domains of the sites. "1" means True, "0" means False

Down here all explained:

  

  

| Config | Value |
|-------------------------|---|
| Domain | The domain of the site, must be a string |
|enabled | If the site is enabled or not. This will override user-preference in the configuration|
|**_ForwardProxy| Whether or not to use the ForwardProxy for the specific site.|
|**_Proxy| Whether or not to use the Proxies for the specific site.|
|load_env|It needs to be enabled if you need to load a .env file. On remote hosting services, like Hugging Face or Render, it needs to be disabled. |
|HOST| The host for the Fast API APP|
|PORT| The port for the Fast API APP. Default: 8080 
|level| The level for the logging module. Default: info
|Icon| The Icon for the Add-On.|
|Global_Proxy| Whatever to enable a Global Proxy which will be valid for every request in the add-on.
  
  

Check those links to get the new Domain for the providers.

  


  

[STREAMINGCOMMUNITY](https://t.me/+jlXmmprhtakxYWJh)

  


  

[STREAMINGWATCH](https://t.me/streamingwatch)

  


  

[ANIMEWORLD](https://t.me/AnimeWorldITA2)

[CB01](https://cb01.uno/)

[GUARDAFLIX](https://guardoserie.it/)

[GUARDOSERIE](https://guardoserie.it/)

[EUROSTREAMING](https://eurostreaming-nuovo-indirizzo.online/)



## Mediaflow Proxy

This project uses Mediaflow-Proxy to bypass some protections. You can find instructions about how to install it [here](https://github.com/mhdzumair/mediaflow-proxy/).

## Credits

 - Big thanks to [Lovi0](https://github.com/Lovi-0), the creator of StreamingCommunity downloader, for helping me with some aspects of this project.
 - This project uses [MediaFlowProxy](https://github.com/mhdzumair/mediaflow-proxy/) in order to be able to play some Live TV channels and to proxy some streams. Big thanks to his creator, [mhdzumair](https://github.com/mhdzumair)

## Disclaimer

We hereby issue this notice to inform you that this Add-On just function like an ordinary browser (like your browser) that fetch video files from internet, and do not violate the provisions of the Digital Millennium Copyright Act (DMCA). The Content these extensions may access is not hosted  or made avaiable by us or the Stremio application but the websites they are browsing in their autonomous mode. It is sole responsibility of the user and his/her countries' or states' law. If you think they are violating any intellectual property then please contact the actual file hosts not the owners of this repository or the Stremio app.

Thank You.


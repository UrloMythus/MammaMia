
  

  

# MammaMia

  

  

  

  

A Stremio Addon for  HTTPS Streams in Italian

Movies, Series, Anime and Live TV are supported.

 
  

  

  

  

# Installation

  

  

  

## Local

  

  

  

1. Install required packages

  

  

  

``pip install -r requirements.txt ``

  2. Create a .env file and fill it (look at example.env)

    

  

3. Then to start the Fast API app server just execute:

  

  

``python3 run.py``

  



  

## Hugging Face

  

  

  

To host this project with Hugging Face, go to the [linked](https://huggingface.co/spaces/aiMAmmaM/DuplicateTheSpace) page and follow these steps:

  

  

  

  

1. Create an Hugging Face Account [here](https://huggingface.co/join)

  

2. Go to [linked](https://huggingface.co/spaces/aiMAmmaM/DuplicateTheSpace) page and click on three dots on the top (right) part of the screen

3. Click Duplicate this Space

4. Insert TMDB Key and set visibility to Public
 
5. Duplicate the Project

6. Go on the Github of the [Repo](https://github.com/UrloMythus/MammaMia/), and after creating a Github Account click on Fork -> Create New Fork -> Create One. 
7. After that go back to your HuggingFace Space and click on Files --> Click on Dockerfile ---> Click on edit ---> Where there is "YourUsername" put your Github username and where there is "YourRepoName" insert the name of the fork.
8. When you are done click Commit Changes to main
  

7. You are done!


  

  

8. To install it on Stremio altought, you will need the Direct URL. It can be found on three dots --> Embed This Space --> Direct URL      
   If you do not find it it means your space is Private. To fix so go to Settings and click Set Visibility to Public. 

 
  

 
How do I handle Updates ? First of all you will need to go to your GitHub Repo and click Sync Changes. Then go into your HuggingFace Space ---> Settings ---> Factory Reset
  

  

  

## Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/UrloMythus/MammaMia)

  

  

To install this project on [Render](https://render.com/) follow these steps:

  

  

  

1. Create an Account

  

  

  

2. Create a Web Service

  

  

  

3. Fork the repo and then connect it to Render

  

  

  

4. Among the other environment variables, put PORT = 8080. This is needed because Render needs the Port given as an environment variable. Remember to put TMDB_KEY as an enviroment variable.

  

  

  

5. As build command put `` pip install -r requirements `` and as run command put ``python3 run.py ``

  

  

  

6. Then just finish Render Setup and you are done :)

  

  

Remember, load_env and Public Instance needs to be disabled in the config.json and Remote_Instance needs to be set to 1

  

  

# Vercel
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FUrloMythus%2FMammaMia&env=PORT,TMDB_KEY&envDescription=PORT%20(8080)%20and%20API%20KEY%20of%20TMDB&envLink=https%3A%2F%2Fgithub.com%2FUrloMythus%2FMammaMia%2Fblob%2Fmain%2Fexample.env)

  

  

# How to add to Stremio

  

  

  

Open your instance URL and configure MammaMia. Once you are done you can click on INSTALL Button. If it doesn't work click on Generate Manifest and copy it. Then paste it  in Stremio Search Bar. If you are on Mac or on Web go to addons, click Add an Addon, and paste it there.

  

  

  

# Enviroment Variables

  

  

  

  

| Enviroment Variable | Value |
|-------------------------|---|
|TMDB_KEY|INSERT YOUR API KEY HERE|
|FORWARDPROXY| "YOURFORWARDPROXY/"  For sites with Cloudfare Protections|
|PROXY |  ["PROXY1","PROXY2"] For sites with Cloudfare Protections, use as many as you wish|

  

  

Here is [linked](https://www.themoviedb.org/settings/api) a tutorial about how to get a TMDB KEY

  

  

  

# Config

  

  

In the repo there is a config.json that you can modify to change some aspects of the addon like the domains of the sites. "1" means True, "0" means False

Down here all explained:

  

  

| Config | Value |
|-------------------------|---|
| Domain | The domain of the site, must be a string |
|enabled | If the site is enabled or not. This will override user-preference while configuration the add-on|
|**_ForwardProxy|If that site needs to use a ForwardProxy which needs to be given in the enviroment variables
|**_Proxy| If that site needs to use Proxies which need to be given in the enviroment variables
|Cookies| Cookies needed for a specific site to work. To get them you will need to log in the site and obtain cookies using Dev Tools. 
|load_env|It needs to be enabled if you need to load a .env file. On remote hosting services, like Hugging Face or Render, it needs to be disabled. |
|HOST| The host for the Fast API APP|
|PORT| The port for the Fast API APP. Default: 8080 |
|Icon| The Icon for the Add-On.|
|Public_Instance| If it's the main public instance. Most of users shouldn't care about this|
|Remote_Instance| Set to  "1" if the server where the add-on is hosted has not the same IP of the  one where Stremio Server is.|
|Global_Proxy| Whatever to enable a Global Proxy which will be valid for every request in the add-on.
  

For now Mysterius must be kept disabled if you do not know what you are doing.
  

Check those links to get the new Domain for the providers.

  

[FILMPERTUTTI](https://filmpertuttiiii.nuovo.live/)

  

[STREAMINGCOMMUNITY](https://t.me/+jlXmmprhtakxYWJh)

  

[TANTIFILM](https://tantinuovo.com/tantifilm-nuovo-indirizzo/)

  

[STREAMINGWATCH](https://t.me/streamingwatch)

  

[LORDCHANNEL](https://t.me/+5MQwrb3eqb81NGI0)

  

[ANIMEWORLD](https://t.me/AnimeWorldITA2)

[CB01](https://cb01.uno/)

## Mediaflow Proxy

This project uses Mediaflow-Proxy to bypass some protections. You can find instructions about how to install it [here](https://github.com/mhdzumair/mediaflow-proxy/).
Not only some provider won't play without it, as said in the config, but also most of paid channels won't. 

## Credits

 - Big thanks to [Lovi0](https://github.com/Lovi-0), the creator of StreamingCommunity downloader, for helping me with some aspects of this project.
 - This project uses [MediaFlowProxy](https://github.com/mhdzumair/mediaflow-proxy/) in order to be able to play some Live TV channels and to proxy some streams. Big thanks to his creator, [mhdzumair](https://github.com/mhdzumair)

## Disclaimer

We hereby issue this notice to inform you that this Add-On just function like an ordinary browser (like your browser) that fetch video files from internet, and do not violate the provisions of the Digital Millennium Copyright Act (DMCA). The Content these extensions may access is not hosted  or made avaiable by us or the Stremio application but the websites they are browsing in their autonomous mode. It is sole responsibility of the user and his/her countries' or states' law. If you think they are violating any intellectual property then please contact the actual file hosts not the owners of this repository or the Stremio app.

Thank You.



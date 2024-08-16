                #Get showname
                    showname = get_info_imdb(imdb_id,ismovie,type)
                    date = None
                else:
                    #I just set n season to None to avoid bugs, but it is not needed if Fast search is enabled
                    date = None
                    #else just equals them
                    tmdba = imdb_id.replace("tmdb:","")
                    showname = get_info_tmdb(tmdba,ismovie,type)
            elif SC_FAST_SEARCH == "0":
                tmdba = get_TMDb_id_from_IMDb_id(imdb_id)
                showname,date = get_info_tmdb(tmdba,ismovie,type)  
        #HERE THE CASE IF IT IS A MOVIE
        else:
            if "tt" in imdb:
                #Get showname
                date = None
                showname = get_info_imdb(imdb_id,ismovie,type)
            else:
                    #I just set n season to None to avoid bugs, but it is not needed if Fast search is enabled
                    #else just equals them
                    date = None
                    tmdba = imdb_id.replace("tmdb:","")
                    showname = get_info_tmdb(tmdba,ismovie,type) 

        showname = showname.replace(" ", "+").replace("–", "+").replace("—","+")
        query = f'https://streamingcommunity.{SC_DOMAIN}/api/search?q={showname}'
        tid,slug = search(query,date,ismovie)
        version = get_version()
        if ismovie == 1:
            #TID means temporaly ID
            url,url720,quality = get_film(tid,version)
            print(url)
            return url,url720,quality
        if ismovie == 0:
            #Uid = URL ID
            episode_id = get_season_episode_id(tid,slug,season,episode,version)
            url,url720,quality = get_episode_link(episode_id,tid,version)
            print(url)
            return url,url720,quality
    except Exception as e:
        print("Nope It failed")

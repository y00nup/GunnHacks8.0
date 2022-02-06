import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
import sys


spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="", client_secret=""))
# example: 
#results = spotify.search(q='genre:pop', limit=10, type="track", market=["US"])
#print(results)


def getsongs(mood, genre, limit, offset=0):
    print(genre)
    genremusic = spotify.search(q="genre:"+genre, limit=limit, type="track", market="US")
    length = len(genremusic["tracks"]["items"])

    genre_dict = {"songs":[]}
    for i in range(0, length):
        tempdict = {}
        tempdict["name"] = genremusic["tracks"]["items"][i]["name"]
        tempdict["preview"] = genremusic["tracks"]["items"][i]["preview_url"]
        tempdict["artist"] =  genremusic["tracks"]["items"][i]["artists"][0]["name"]
        tempdict["uri"] = genremusic["tracks"]["items"][i]["uri"]
        tempdict["id"] = genremusic["tracks"]["items"][i]["id"]
        genre_dict["songs"].append(tempdict)

    return genre_dict
    


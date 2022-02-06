import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import songsdata
from songsdata import happy_songs, sad_songs, angry_songs, test_dict
from sklearn import tree
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer



## AI Model Training

training_dicts = happy_songs + sad_songs + angry_songs
training_labels = ["happy"] * len(happy_songs) + ["sad"] * len(sad_songs) + ["angry"] * len(angry_songs)
vectorizer = DictVectorizer()
vectorizer.fit(training_dicts)
training_vectors = vectorizer.transform(training_dicts)
testing_vectors = vectorizer.transform(test_dict)
classifier = tree.DecisionTreeClassifier()
classifier.fit(training_vectors, training_labels)
print(classifier.predict(testing_vectors))
tree.export_graphviz(
    classifier,
    out_file='tree.dot',
    feature_names=vectorizer.get_feature_names(),
) 

def manual_classify(song):
    song = song[0]
    if song["tempo"] < 90 and song["speechiness"] < 0.04:
        return "sad"
    if song["tempo"] > 110 or song["speechiness"] > 0.4 :
        return "angry"
    else:
        return "happy"


##


spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="17037de2bf4f479b817cc1d40ef2d4c2", client_secret="1b8adca14e0741dfba733d83754ab015"))

def get_uris(data):
    items = data["tracks"]["items"]
    uris = []
    for item in items:
        uris.append(item["uri"])
    return uris


def get_mood(uri):
    return spotify.audio_features(uri)
    

def infotomood(item):
    energy=item[0]["energy"]
    loudness=item[0]["loudness"]
    speech=item[0]["speechiness"]
    live=item[0]["liveness"]
    tempo=item[0]["tempo"]
    predictions = []
    prediction = manual_classify(item)
    predictions.append(prediction)
    return predictions[0]


def getsongs(mood, genre, limit, offset=0):
    genre_dict = {"songs":[]}
    off = 0
    while len(genre_dict["songs"]) < 21:
        genremusic = spotify.search(q="genre:"+genre, limit=50, offset=50, type="track", market="US")
        length = len(genremusic["tracks"]["items"])
        for i in range(0, length):
            if infotomood(get_mood(genremusic["tracks"]["items"][i]["uri"])) == mood:
                print('match found')
                tempdict = {}
                tempdict["name"] = genremusic["tracks"]["items"][i]["name"]
                tempdict["preview"] = genremusic["tracks"]["items"][i]["preview_url"]
                tempdict["artist"] =  genremusic["tracks"]["items"][i]["artists"][0]["name"]
                tempdict["uri"] = genremusic["tracks"]["items"][i]["uri"]
                tempdict["id"] = genremusic["tracks"]["items"][i]["id"]
                genre_dict["songs"].append(tempdict)
            else:
                print(f"Got " + infotomood(get_mood(genremusic["tracks"]["items"][i]["uri"])) +" expected " + mood)
        off += 50
    

        
    return genre_dict






test = '''

results = spotify.search(q="genre:pop", limit=10, type="track", market=["US"])
data = results["tracks"]["items"]
for item in data:
    item_uri = item["uri"]
    info = get_mood(item_uri)
    mood = infotomood(info)
    
'''
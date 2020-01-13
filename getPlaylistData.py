"""
Takes a library and compiles a csv with useful data:
name
artist
duration
key
mode
beats
acousticness
danceability
energy
instrumentalness
liveness
loudness
speechiness
valence
tempo
popularity

Precondtion: supply program with playlist id and user id by moddifying variables: playlist_id and user_id
"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import SpotifyCred
import pandas as pd

sp = SpotifyCred.spotifyCreds()

playlist_id = '4YbnWNufZdK8Qr00fcWEDz'
user = '12156476892'
#sp.current_user()["id"]

numOfSongs = 0

class variables:
    """
    Stores list of each song and corresponding data
    """
    uri = []
    name = []
    artist = []
    duration = []
    key = []
    mode = []
    beats = []
    acousticness = []
    danceability = []
    energy = []
    instrumentalness = []
    liveness = []
    loudness = []
    speechiness = []
    valence = []
    tempo = []
    popularity = []

def main():
    """
    Loops through entire playlist and calls function fillVariables for each song.
    After it finishes looping, it breaks loop and calls fillCsv to create csv for all the variables
    """
    global numOfSongs
    i=0
    while True:
        if (i%100 == 0):
            result = sp.user_playlist_tracks(user,playlist_id = playlist_id, offset = numOfSongs)
            numOfSongs += len(result["items"])
            i=0
            print(numOfSongs)
        if(i == len(result["items"])):
            break
        song = result["items"][i]["track"]["uri"]
        try:
            features = sp.audio_features(song)
        except:
            i+=1
            continue
        fillVariables(song, result, features, i)
        i+=1
    fillCsv()

Vars = variables()

def fillVariables(song, result, features, i):
    """
    Appends each data element to object Vars of class variable
    """
    Vars.uri.append(song)
    Vars.name.append(result["items"][i]["track"]["name"])
    Vars.artist.append(result["items"][i]["track"]["artists"][0]["name"])
    Vars.duration.append(features[0]["duration_ms"])
    Vars.key.append(features[0]["key"])
    Vars.mode.append(features[0]["mode"])
    Vars.beats.append(features[0]["time_signature"])
    Vars.acousticness.append(features[0]["acousticness"])
    Vars.danceability.append(features[0]["danceability"])
    Vars.energy.append(features[0]["energy"])
    Vars.instrumentalness.append(features[0]["instrumentalness"])
    Vars.liveness.append(features[0]["liveness"])
    Vars.loudness.append(features[0]["loudness"])
    Vars.speechiness.append(features[0]["speechiness"])
    Vars.valence.append(features[0]["valence"])
    Vars.tempo.append(features[0]["tempo"])
    Vars.popularity.append(result["items"][i]["track"]["popularity"])

def fillCsv():
    "Fills out csv of all data"
    data = pd.DataFrame(list(zip(Vars.name, Vars.artist, Vars.duration, Vars.key, Vars.mode,
    Vars.beats, Vars.acousticness, Vars.danceability, Vars.energy, Vars.instrumentalness,
    Vars.liveness, Vars.loudness, Vars.speechiness, Vars.valence, Vars.tempo, Vars.popularity, Vars.uri)),
    columns= ["name", "artist", "duration", "key", "mode", "beats", "acousticness",
    "danceability", "energy", "instrumentalness", "liveness", "loudness", "speechiness",
    "valence", "tempo", "popularity", "URI"])
    data.to_csv("playlistBo.csv")

main()

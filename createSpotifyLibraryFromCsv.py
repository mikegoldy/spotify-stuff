"""
Takes a list of Apple music songs that are pasted onto a csv and adds subsequent songs (or as many as spotify has)
onto Spotify.

Creates a Spotify Playlist with name of user's choice and adds songs unto that library.

Precondition: Copy Apple music libray (A simply control-C will suffice) and paste onto excel or other type of
spreadsheet program. Save as .csv file.
"""

import spotipy
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import SpotifyCred

#playlist_id = '3Wp8MOROoeQ6gBU4QEyMqT'

missingartist = []
missingtrack = []
sp = SpotifyCred.spotifyCreds()

def main():
    """
    Opens web browser, prompting spotiy login.
    Asks name for desired playlist to create,
    prompts for apple music csv file, and calls searchMusic function.
    Lastly calls missingCsv function.
    Precondition: have Apple music .csv.
    """
    print("After logging into spotify, you will be redirected unto a non-existant website. Copy the url and paste here:")
    print("Type the name of the Spotify Playlist to be created:")
    playlistName = input()
    print("UPLOAD CSV FILE")
    root = Tk()
    root.withdraw() # we don't want a full GUI, so keep the root window from appearing
    filepath = askopenfilename()
    root.update() #remove file window
    music = readCsv(filepath)
    user = sp.current_user()["id"]
    playlist = sp.user_playlist_create(user, playlistName)
    searchMusic(music, playlist['id'], user)
    global missingartist
    global missingtrack
    missingCsv(missingtrack, missingartist)

def openFile():
    fname = askopenfilename()
    root.destroy()

def searchMusic(music, playlist, user):
    """
    Searches Spotify for music corresponding to given artist and track name.
    If song cannot be found, calls mussingTrack/missingArtist function to modify the string to
    something spotify can read.
    If song can still not be found, compiles a list of said missing tracks an corresponding artists onto global variables:
    missingartist & missingtrack.
    Lastly, adds song to newly created playlist.
    """
    for index, row in music.iterrows():
        global missingartist
        global missingtrack
        id = []
        artist= row['Artist']
        track = row['Songs']
        fulltrack = track
        fullartist = artist
        result = sp.search(q='artist:' + artist + ' track:' + track, type='track')
        if not result["tracks"]["items"]: # if track not found make some changes to track/artist name
            track = missingTrack(track)
            artist = missingArtist(artist)
            result = sp.search(q='artist:' + artist + ' track:' + track, type='track')
        if not result["tracks"]["items"]: #keep track of all missing tracks on spotify
            print("Track: %s Artist: %s" % (track,artist))
            missingartist.append(fullartist)
            missingtrack.append(fulltrack)
            continue
        trackId = result['tracks']['items'][0]['uri']
        id.append(trackId)
        sp.user_playlist_add_tracks(user,playlist_id=playlist, tracks=id)
        id = []


def missingTrack(track):
    if ("F**k" in track):
        track = track.replace("F**k", "Fuck")
    if("(f" in track):
        track = track[:track.find("(f")]
    if("feat" in track):
        track = track[:track.find("(f")]
    if("(F" in track):
        track = track[:track.find("(F")]
    if("'" in track):
        track = track.replace("'", "")
    if ("ft." in track):
        track = track[:track.find("ft.")]
    if("(Original Mix)" in track):
        track = track[:track.find("(Original Mix)")]
    if("(feat." in track):
        track = track[:track.find("(feat.")]
    if("[feat." in track):
        track = track[:track.find("[feat.")]
    return track

def missingArtist(artist):
    if("'" in artist):
        artist = artist.replace("'", "")
    if("&" in artist):
        artist = artist[:artist.find("&")]
    if("ft." in artist):
        artist = artist[:artist.find("ft.")]
    if("feat" in artist):
        artist = artist[:artist.find("feat")]
    if("Feat" in artist):
        artist = artist[:artist.find("Feat")]
    if("vs" in artist):
        artist = artist[:artist.find("vs")]
    if("/" in artist):
        artist = artist[:artist.find("/")]
    if(" x " in artist):
        artist = artist[:artist.find(" x ")]
    if("," in artist):
        artist = artist[:artist.find(",")]
    if(" and" in artist):
        artist = artist[:artist.find(" and")]
    if(" And" in artist):
        artist = artist[:artist.find(" And")]
    if("Ft" in artist):
        artist = artist[:artist.find("Ft")]
    return artist

def missingCsv(missingtrack, missingartist):
    "Creates csv of missing songs."
    missing = pd.DataFrame(list(zip(missingtrack, missingartist)), columns=["Track", "Artist"])
    missing.to_csv("missingSongs.csv")

def readCsv(filepath):
    "Reads Apple music csv"
    songs = pd.read_csv(filepath, names = ["Songs", "unknown", "Length", "Artist", "Albums", "genre", "whatever", "whateverq"] )
    return songs.iloc[:, [0, 3]]

main()

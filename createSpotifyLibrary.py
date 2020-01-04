import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import SpotifyCred

################################# USER INPUT #################################

print("Please enter playlist id below")
playlist_id = input()
#playlist_id = '3Wp8MOROoeQ6gBU4QEyMqT'
################################# SPOTIFY LOGIN ###################################

sp = SpotifyCred.spotifyCreds()

################################# CSV CONSTUCTION #################################
print("UPLOAD CSV FILE")
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filepath = askopenfilename()
songs = pd.read_csv(filepath, names = ["Songs", "unknown", "Length", "Artist", "Albums", "genre", "whatever", "whateverq"] )
music = songs.iloc[:, [0, 3]]

missingartist = []
missingtrack = []
##################### SEARCH SONGS AND ADD TO PLAYLIST #########################

for index, row in music.iterrows():
    id = []
    artist= row['Artist']
    track= row['Songs']
    result = sp.search(q='artist:' + artist + ' track:' + track, type='track')
    if not result["tracks"]["items"]: # if track not found make some changes to track/artist name
        fullartist = artist
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
        if("(Original Mix)" in track):
            track = track[:track.find("(Original Mix)")]
        result = sp.search(q='artist:' + artist + ' track:' + track, type='track')
    if not result["tracks"]["items"]: #keep track of all missing tracks on spotify
        print("Track: %s Artist: %s" % (track,fullartist))
        missingartist.append(fullartist)
        missingtrack.append(track)
        continue
    trackId = result['tracks']['items'][0]['uri']
    id.append(trackId)
    sp.user_playlist_add_tracks(user,playlist_id=playlist_id, tracks=id)

##################### ADDING MISSING TRACKS TO A CSV FILE #####################

missing = pd.DataFrame(list(zip(missingtrack, missingartist)), columns=["Track", "Artist"])
filesave = filepath[:filepath.rfind("/")]
filesave = filesave + "/"
missing.to_csv(filesave)

"""
artist= "Travis Scott "
track= "pick up the phone"
result = sp.search(q=' track:' + track, type='track')
print(result)
#trackId = result['tracks']['items'][0]['uri']
#sp.user_playlist_add_tracks(user,playlist_id='3Wp8MOROoeQ6gBU4QEyMqT', tracks=trackId)
"""

#4Kqp4AtoCDoCotN7KjrLKL

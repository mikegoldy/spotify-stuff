# spotify-stuff

This project first started after I saw Spotify's "Wrapped" 2019 feature. I've always been an Apple Music user but that feature was finally enough to push me to change sides. (Whoever thought of the idea is a genius) But one difficult barrier remained: the tedious hassle of moving my apple music library to Spotify. That is until I discovered I could use Spotify's api for free.

Hence, I created an app that takes my apple music from a csv file and adds all of my music (1522 songs/ 1600 songs) onto Spotify. But once, I did that I got curius...

I realized that I could do so much more with Spotify's api. See, Spotify provides a set of metrics for each song: danceability, energy, acousticness, loudness, mode, key, instrumentalness, valence, etc. (Refer here for the full list: https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/) As a statistics student, this is when my mind started thinking. I could analyze music, find patterns, and make statistical claims, albeit not very solid ones.

WHAT I HAVE DONE SO FAR:

1. Created an app that can move one's apple music library unto spotify using python and the library spotipy. And, made a set of instructions to use the app. -See: createSpotifyLibraryFromCsv.py
2. Created a script that takes the music of a playlist and compiles a list of songs with its' audio features onto a csv. -See: getPlaylistData.py
3. Analyzed my music library, found some interesting insights about my music and some friends (Bo, and hopefully more soon)   -See: SpotifyLibraryDataAnalysis.ipynb and BoLibraryDataAnalysis.ipynb
4. Make different playlists. For example high energy songs can be a workout playlist etc. -See: playlistCreation.ipynb

WHAT I AM WORKING ON NOW:

1. What causes a song to be associated as positive? (For example: Are songs with higher energy more positive? Are songs that are louder more positive?)
2. What causes a song to be popular? This one is far more difficult to pinpoint.

WHAT I'D LIKE TO DO IN THE FUTURE:

1. Encrypt my Spotify api login
2. Compare the top charts between countries
3. Compare different genres
4. Create data clusters of a library and, if possible, optimize the shuffle feature in that library to play a cluster of music that matches the user's mood at that given moment. (This is more conceptual I don't I can control spotify's shuffle)


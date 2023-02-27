import spotipy
import SpotifyCred

sp = SpotifyCred.spotifyCreds()

result = sp.current_playback()
print(result)

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

def spotifyCreds():
    cid = '1f439f0097ad4588acda4fb387ec714d'
    secret = 'fac8c33b1a854fa19be936ee96c52c11'
    #client_credentials_manager = SpotifyClientCredentials(client_id = cid, client_secret = secret)
    #token = client_credentials_manager.get_access_token()
    scope = 'playlist-modify-public'
    redirect_uri='http://localhost:8888/callback'
    user = '12120259561'
    token = util.prompt_for_user_token(
            username=user,
            scope=scope,
            client_id=cid,
            client_secret=secret,
            redirect_uri=redirect_uri)
    sp = spotipy.Spotify(auth=token)
    return sp

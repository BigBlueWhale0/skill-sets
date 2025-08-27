from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

load_dotenv()

SPOTIPY_CLIENT_ID = os.environ.get("ENV_SPOTIFY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("ENV_SPOTIFY_CLIENT_SECRET")
REDIRECT_URL = "http://spotify.com"

class Spotify:
    def __init__(self):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri="https://example.com",
                client_id=SPOTIPY_CLIENT_ID,
                client_secret=SPOTIPY_CLIENT_SECRET,
                show_dialog=True,
                cache_path="token.txt"
            )
        )
        self.user_id = self.sp.current_user()["id"]

    def create_playlist(self,timestamp):
        self.timestamp = timestamp
        result = self.sp.user_playlist_create(self.user_id, f"{self.timestamp} Billboard 100", public=False, collaborative=False, description='Top 100 songs retrieved from billboard.com')
        self.playlist_id = result["id"]

    def add_song_to_playlist(self,song_list):
        year = self.timestamp.split("-")[0]
        song_urls = []
        for song_name in song_list:
            result = self.sp.search(q=f"track:{song_name} year:{year}", type="track")
            try:
                song_urls.append(result["tracks"]["items"][0]["uri"])
            except IndexError:
                print(f"The song {song_name} was not found in Spotify")
        self.sp.playlist_add_items(self.playlist_id, items=song_urls)



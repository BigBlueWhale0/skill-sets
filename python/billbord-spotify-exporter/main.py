from billboard import Billboard
from spotify import Spotify
import urllib3
from dotenv import load_dotenv

load_dotenv()

urllib3.disable_warnings()

timestamp = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

billboard = Billboard()
song_list = billboard.search_top_list(timestamp)

spotify = Spotify()
spotify.create_playlist(timestamp)
spotify.add_song_to_playlist(song_list)
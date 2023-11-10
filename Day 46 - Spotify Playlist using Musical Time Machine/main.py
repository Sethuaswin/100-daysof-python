# importing Beutiful soup and requests module
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

DATE = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{DATE}/"

# Getting the response for the top 100 song list
response = requests.get(URL)
billboard_songs_page = response.text

# Intializing BeautifuleSoup with the billboard_songs_page html text
soup = BeautifulSoup(billboard_songs_page, "html.parser")

# Getting the top 100 songs

first_song = soup.find(name="a", class_="c-title__link lrv-a-unstyle-link").getText().strip()  # type: ignore
songs_99 = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

song_list = [song.getText().strip() for song in songs_99]
song_list.insert(0, first_song)

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="YOUR CLIENT ID",
        client_secret="YOUR CLIENT SECRET",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]  #type: ignore
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = DATE.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]  #type: ignore
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{DATE} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)  #type: ignore


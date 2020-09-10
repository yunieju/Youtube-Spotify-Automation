import os
import json

from spotify_client import SpotifyClient
from youtube_client import YouTubeClient

def run():
    with open('creds/spotify_auth.json') as sp:
        data = sp.read()
    spotify_cred = json.loads(data)
    youtube_client = YouTubeClient()

    spotify_client = SpotifyClient(spotify_cred["spotify_token"])
    playlists = youtube_client.get_playlists()

    for index, playlist in enumerate(playlists):
        print(f"{index}: {playlist.title}")
    choice = int(input("Enter you choice: "))
    chosen_playlist = playlists[choice]
    print(f"You selected: {chosen_playlist.title}")

    playlist_name = input("Enter a name for your new playlist: ")
    playlist_id = spotify_client.create_new_playlist(playlist_name)
    print(playlist_id)

    songs = youtube_client.get_songs_from_playlist(chosen_playlist.id)
    print(songs)
    print(f"Attept to add {len(songs)} songs")

    uris = []
    for song in songs:
        spotify_song_uri = spotify_client.search_song(song.artist, song.track)
        uris.append(spotify_song_uri)
        print(uris)
        count = len(uris)
    added_song = spotify_client.add_song_to_spotify(uris, playlist_id)
    print(f"added {count} songs in your {playlist_name} playlist")


if __name__ == '__main__':
    run()

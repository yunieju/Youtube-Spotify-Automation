import requests
import urllib.parse

class SpotifyClient(object):
    def __init__(self, api_token):
        self.api_token = api_token

    def search_song(self, artist, track):
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            track,
            artist
        )
        print(track, artist)
        # query = urllib.parse.quote(f'{artist} {track}')
        # url = f"https://api.spotify.com/v1/search?q={query}$type=track"
        response = requests.get(
            query,
            headers= {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        response_json = response.json()

        results = response_json['track']['items']
        if results:
            return results[0]['id']
        else:
            raise Exception(f"No song found for {track} by {artist}")

    def create_new_playlist(self, playlist_name):
        url = "https://api.spotify.com/v1/me/playlists"
        response = requests.post(
            url,
            json = {
                    "name": playlist_name,
                    "public": False
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        response_json = response.json()
        print("Print Response object", response)
        print("Print Response json", response_json)
        return response_json["id"]

    def add_song_to_spotify(self, song_id, playlist_id):
        url = f"https://api.spotify.com/v1/me/{playlist_id}/tracks"
        response = requests.put(
            url,
            json={
                "ids": [song_id]
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )

        return response.ok
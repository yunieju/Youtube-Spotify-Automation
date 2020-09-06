import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import youtube_dl


class Playlist(object):
    def __init__(self, id, title):
        self.id = id
        self.title = title


class Song(object):
    def __init__(self, artist, track):
        self.artist = artist
        self.track = track


class YouTubeClient(object):
    def __init__(self):
        # youtube_dl default User-Agent can cause some json values to return as None, using Facebook's web crawler solves this.
        # print(youtube_dl.utils.std_headers['User-Agent'])
        youtube_dl.utils.std_headers['User-Agent'] = "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"
        # print(youtube_dl.utils.std_headers['User-Agent'])
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        credentials_location = "creds/auth.json"
        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            credentials_location, scopes)
        credentials = flow.run_console()
        youtube_client = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        self.youtube_client = youtube_client

    def get_playlists(self):
        request = self.youtube_client.playlists().list(
            part="id, snippet",
            maxResults=50,
            mine=True
        )
        response = request.execute()
        print(response['items'])

        playlists = [Playlist(item['id'], item['snippet']['title']) for item in response['items']]

        return playlists

    def get_songs_from_playlist(self, playlist_id):
        songs = []
        request = self.youtube_client.playlistItems().list(
            playlistId=playlist_id,
            part="id, snippet",
            maxResults=25
        )
        response = request.execute()

        for item in response['items']:
            video_id = item['snippet']['resourceId']['videoId']
            youtube_url = f"https://www.youtube.com/watch?v={video_id}"
            video = youtube_dl.YoutubeDL({'quiet': True}).extract_info(youtube_url, download=False)

            title = video['title']

            track = video['track']
            artist = video['artist']
            print(video)
            print(track, artist)

            if artist and track:
                songs.append(Song(artist, track))

        return songs

# Youtube-Spotify-Automation
automatically generate Spotify playlist from your Youtube playlist 

## Technologies
- Spotify API
- YoutubeDL library
- Youtube Data API
- Requests library

## Setup
- install all dependencies
```
pip3 install -r requirements.txt
```
- Run the app
```
python run.py
```

## Spotify API Token
- get your Spotify ID and OAuth Token and add id to spotify_auth.json in creds folder
- you can get your User ID from [Account Overview](https://www.spotify.com/us/account/overview/) in username
- You can get API Token in [Spotify Web API website](https://developer.spotify.com/console/post-playlists/)

## Youtube Auth
- You can download Google credential json file by making API key and OAuth 2.0 [here](https://console.developers.google.com/apis/credentials)

## Note
- If the video uploader didn't specify song information(artist, track), song and artist field may return None in response.
- To resolve this issue, added extraction from video title part, but it only supports "artist - track" naming conventions

### Thanks to
Thanks for the great inspiration! @TheComeUpCode & @imdadahad 

import requests
import os
from dotenv import load_dotenv


# Spotify API endpoints
AUTH_URL = "https://accounts.spotify.com/api/token"
BASE_URL = "https://api.spotify.com/v1/"


# Internal function to be used to get
# The ID of an artist
def get_artist_id(headers,artist):

    response = requests.get(BASE_URL + f'search?q=artist:{str.lower(artist)}&type=artist', headers=headers)

    response_data = response.json()

    
    # Get the artist's Spotify ID
    artist_id = response_data['artists']['items'][0]['id']

    return artist_id

def get_track_id(headers, song):

    response = requests.get(BASE_URL + f'search?q=track:{str.lower(song)}&type=track',headers=headers)
    response_data = response.json()
    # print(response_data['tracks']['items'])
    # Get the song's Spotify ID
    if response_data['tracks']['items'] == []:
        return "No such track ID found"
    elif song == "":
        # print("Please enter the name of a song.")
        return "Please enter the name of a song."
    else: song_id = response_data['tracks']['items'][0]['id']
    return song_id

def authenticate():

    load_dotenv()

    # Spotify app's client ID and client secret
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET =  os.getenv("CLIENT_SECRET")


    # Request an access token
    auth_response = requests.post(AUTH_URL, data={
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    # Convert the response to JSON
    auth_response_data = auth_response.json()

    print(auth_response_data)
    #Save the access token
    access_token = auth_response_data['access_token']

    return access_token



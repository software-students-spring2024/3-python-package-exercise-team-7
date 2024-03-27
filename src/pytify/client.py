import requests
import os
from dotenv import load_dotenv
import base64
from requests import post
import json

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
    token = auth_response_data['access_token']

    return token


token = authenticate()


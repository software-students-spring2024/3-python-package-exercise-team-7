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

load_dotenv()


    # Spotify app's client ID and client secret
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET =  os.getenv("CLIENT_SECRET")
    
def authenticate():
    auth_string = CLIENT_ID + ":" + CLIENT_SECRET
    auth_bytes = auth_string.encode ("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    
    url = "https://accounts.spotify.com/api/token"
    headers={
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
         }
    
    data = {"grant_type":"client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

token = authenticate()


    
            




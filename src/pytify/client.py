import requests
import os
from dotenv import load_dotenv
import base64
from requests import post
import json

# Spotify API endpoints
AUTH_URL = "https://accounts.spotify.com/api/token"
BASE_URL = "https://api.spotify.com/v1/"


class Client:
    def __init__(self, CLIENT_ID, CLIENT_SECRET):
        
        self.CLIENT_ID = os.getenv("CLIENT_ID")
        self.CLIENT_SECRET = os.getenv("CLIENT_SECRET")
        self.token = self.authenticate()

    def authenticate(self):
        auth_string = self.CLIENT_ID + ":" + self.CLIENT_SECRET
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    
        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-Type": "application/x-www-form-urlencoded"
        }
    
        data = {"grant_type": "client_credentials"}
        result = post(url, headers=headers, data=data)
        json_result = json.loads(result.content)
        token = json_result["access_token"]
        return token

    def get_artist_id(self, artist):
        headers = {
            'Authorization': 'Bearer {token}'.format(token=self.token)
        }

        response = requests.get(BASE_URL + f'search?q=artist:{str.lower(artist)}&type=artist', headers=headers)

        response_data = response.json()
        
        # Get the artist's Spotify ID
        artist_id = response_data['artists']['items'][0]['id']

        return artist_id

    def search_for_artist(self, artist_name):
        """
        Search for an artist by name.

        Args:
            - artist_name (str): the name of the artist to search for.

        Returns:
            - dict: About the artist.
        """  
        access_token = self.authenticate()

        headers = {
            'Authorization': 'Bearer {token}'.format(token=access_token)
        }

        response = requests.get(BASE_URL + 'search?q=' + artist_name + '&type=artist', headers=headers)

        if response.status_code == 200:
            artist_data = response.json()['artists']['items'][0]
            return artist_data
        else:
            print(f"Failed to get artist's information: {response.status_code}")
            return None

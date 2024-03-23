import requests
import os
from dotenv import load_dotenv
from client import get_artist_id, authenticate

load_dotenv()

# Spotify app's client ID and client secret
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET =  os.getenv("CLIENT_SECRET")

# Spotify API endpoints
AUTH_URL = "https://accounts.spotify.com/api/token"
BASE_URL = "https://api.spotify.com/v1/"

def main():
   get_top_ten("J Cole")

def get_top_ten(artist):
    access_token = authenticate()

    headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    artist_id = get_artist_id(headers, artist)

    # Use the artist's Spotify ID to get their top tracks
    response = requests.get(BASE_URL + 'artists/' + artist_id + '/top-tracks?country=US', headers=headers)

    # Convert the response to JSON
    response_data = response.json()

    # Print the names of the artist's top 10 tracks
    for i, track in enumerate(response_data['tracks'][:10]):
        print(f"{i+1}. {track['name']}")

if __name__ == "__main__":
    main()
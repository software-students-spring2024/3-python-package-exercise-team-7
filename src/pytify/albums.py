import requests
import os
from dotenv import load_dotenv
from src.Pytify.client import get_artist_id, authenticate

load_dotenv()

# Spotify app's client ID and client secret
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET =  os.getenv("CLIENT_SECRET")

# Spotify API endpoints
AUTH_URL = "https://accounts.spotify.com/api/token"
BASE_URL = "https://api.spotify.com/v1/"

def main():
     get_artist_albums("wallows")


def get_artist_albums(artist):
    access_token = authenticate()
    headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}
    artist_id = get_artist_id(headers, artist)
    if artist_id:
        response = requests.get(BASE_URL + 'artists/' + artist_id + '/albums', headers=headers)
        if response.status_code == 200:
            response_data = response.json()
            
            if 'items' in response_data:
                albums = [album for album in response_data['items'] if album.get('album_type') == 'album']
                album_names = [album["name"] for album in albums]
                print(album_names)
                return album_names
                
            else:
                print("No albums found for the artist.")
                return []
        else:
            print(f"Failed to fetch albums for artist {artist_id}. Status code: {response.status_code}")
            return []
    else:
        print(f"No artist found with name '{artist}'")
        return []



if __name__ == "__main__":
    main()
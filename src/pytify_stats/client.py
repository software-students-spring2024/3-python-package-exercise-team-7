import requests

class Client:
    # Spotify API endpoints
    AUTH_URL = "https://accounts.spotify.com/api/token"
    BASE_URL = "https://api.spotify.com/v1/"

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def authenticate(self):
        # Request an access token
        auth_response = requests.post(self.AUTH_URL, data={
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        })

        # Convert the response to JSON
        auth_response_data = auth_response.json()

        print(auth_response_data)
        #Save the access token
        access_token = auth_response_data['access_token']

        return access_token
            
    def search(self, headers,name,keyword):

        response = requests.get(self.BASE_URL + f'search?q={keyword}:{str.lower(name)}&type={keyword}', headers=headers)

        # Convert the response to JSON
        response_data = response.json()

        # Get the album's Spotify ID
        album_id = response_data[keyword+"s"]['items'][0]['id']

        return album_id
    
    

    def get_top_ten(self, artist):
        retArray = []

        access_token = self.authenticate()

        headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
        }

        artist_id = self.search(headers, artist, "artist")

        # Use the artist's Spotify ID to get their top tracks
        response = requests.get(self.BASE_URL + 'artists/' + artist_id + '/top-tracks?country=US', headers=headers)

        # Error handling
        if response.status_code != 200:
            print(f"The artist request was invalid, error:{response.status_code}")
            return
        

        # Convert the response to JSON
        response_data = response.json()

        # Print the names of the artist's top 10 tracks
        for i, track in enumerate(response_data['tracks'][:10]):
            retArray.append(track['name'])
            #print(f"{i+1}. {track['name']}")

        return retArray

    def get_album(self, album):
        retArray = []

        access_token = self.authenticate()

        headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
        }

        album_id = self.search(headers, album, "album")

        # Use the album's Spotify ID to get more information
        response = requests.get(self.BASE_URL + 'albums/' + album_id, headers=headers)

        # Error handling
        if response.status_code != 200:
            print(f"The album request was invalid, error:{response.status_code}")
            return

        # Convert the response to JSON
        response_data = response.json()

        # Print the names of the artist's top 10 tracks
        for track in response_data['tracks']['items']:
            retArray.append({'name' : track['name'], "milliseconds": track['duration_ms'], "id": track['duration_ms']})
            #print(f"{i+1}. {track['name']}")

        return retArray

    def get_song(self, song):

        access_token = self.authenticate()

        headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
        }

        song_id = self.search(headers, song, "track")

        # Use the song's Spotify ID to get more information
        response = requests.get(self.BASE_URL + 'tracks/' + song_id, headers=headers)

        # Error handling
        if response.status_code != 200:
            print(f"The song request was invalid, error:{response.status_code}")
            return

        # Convert the response to JSON
        response_data = response.json()    

        return [response_data['name'],response_data['duration_ms']]



        



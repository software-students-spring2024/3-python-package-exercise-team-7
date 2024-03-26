def analyze(song):
    access_token = authenticate()

    headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    if get_track_id(headers, song) == "No such track ID found":
        print("Invalid track ID")
        return "Invalid track ID"
    elif song == "":
        print("Please enter the name of a song.")
        return "Please enter the name of a song."
    else:
        song_id = get_track_id(headers, song)
        #print(song_id)
        response = requests.get(BASE_URL + 'tracks/' + song_id, headers=headers)
        response_data = response.json()
        # print(response_data["artists"])
        print(f"{response_data['name']} by {response_data['artists'][0]['name']}:")

        #Use the song's Spotify ID to get their audio features
        features_response = requests.get(BASE_URL + 'audio-features/' + song_id, headers=headers)
        features_response_data = features_response.json()
        # print(features_response_data)

        feature_list = ''
        for feature in features_response_data:
            # print(f"{feature}: {features_response_data[feature]}")
            feature_list = feature_list + f"{feature}: {features_response_data[feature]}\n"
        print(feature_list)
        return feature_list

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
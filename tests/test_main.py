import pytest
import os
from dotenv import load_dotenv
from pytify import get_artist_id, authenticate



class Tests:

    def test_sanity_check(self):
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"
    
    def test_get_env(self):
        load_dotenv()
        CLIENT_ID = os.getenv("CLIENT_ID")
        CLIENT_SECRET =  os.getenv("CLIENT_SECRET")
        assert isinstance(CLIENT_ID, str)
        assert len(CLIENT_ID) > 0
        assert isinstance(CLIENT_SECRET, str)
        assert len(CLIENT_SECRET) > 0
        


    def test_get_spofify_auth(self):
        access_token = authenticate()
        assert isinstance(access_token, str)

    
    def test_get_artist_id(self):
        access_token = authenticate()

        headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
        }

        artist_id = get_artist_id(headers, "J Cole")

        assert isinstance(artist_id, str)

        
    

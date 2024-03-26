import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from dotenv import load_dotenv
from pytify_stats.client import Client

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
        load_dotenv()
        CLIENT_ID = os.getenv("CLIENT_ID")
        CLIENT_SECRET =  os.getenv("CLIENT_SECRET")
        spy = Client(CLIENT_ID,CLIENT_SECRET)
        access_token = spy.authenticate()
        assert isinstance(access_token, str)
        assert len(access_token) > 0

    
    def test_get_artist_id(self):
        load_dotenv()
        CLIENT_ID = os.getenv("CLIENT_ID")
        CLIENT_SECRET =  os.getenv("CLIENT_SECRET")
        spy = Client(CLIENT_ID,CLIENT_SECRET)
        access_token = spy.authenticate()
        headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
        }
        artist_id = spy.search(headers, "J Cole", "artist")
        assert isinstance(artist_id, str)

        
    

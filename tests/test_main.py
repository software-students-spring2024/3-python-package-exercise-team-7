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

        
    def test_get_track_id(self):
        access_token = authenticate()

        headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
        }

        track_id = get_track_id(headers, "Hello")

        assert isinstance(track_id, str)

    def test_get_track_id_dne(self):
        access_token = authenticate()

        headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
        }

        track_id = get_track_id(headers, "nkewfnnanfsdikesd")

        assert track_id == "No such track ID found"

    def test_get_track_id_no_search(self):
        access_token = authenticate()

        headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
        }
        track_id = get_track_id(headers, "")
        assert track_id == "Please enter the name of a song."

    def test_analyze(self):
        access_token = authenticate()

        headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
        }

        analysis = analyze("Hello")
        assert isinstance(analysis, str)

    def test_analyze_dne(self):
        access_token = authenticate()

        headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
        }
        analysis = analyze("dcinneoenndsiweinwo")
        assert analysis == "Invalid track ID"

    def test_analyze_no_search(self):
        access_token = authenticate()

        headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
        }
        analysis = analyze("")
        assert analysis == "Please enter the name of a song."


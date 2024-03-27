import pytest
import os
from dotenv import load_dotenv 
from src.Pytify.albums import get_artist_albums
from src.Pytify.client import get_artist_id, authenticate




class Tests:
    def test_get_artist_albums(self):
        artist = "wallows" 
        albums = get_artist_albums(artist)

        # Check if the function returns a list
        assert isinstance(albums, list)

        if not albums:
            # if no albums, return empty list
            assert albums == []
            print("No albums found for the artist.")
        else:
            # else check the format of albums
            for album in albums:
                assert isinstance(album, str)
                assert len(album) > 0

   
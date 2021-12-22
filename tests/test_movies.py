import os
import json
import base64
import unittest


app = create_app()


class TestMovies(unittest.TestCase):

    test_data = {
        "director": "Victor Fleming",
        "genre": [
            "Adventure",
            " Family",
            " Fantasy"
        ],
        "99popularity": 87,
        "imdb_score": 8.3,
        "name": "test_input1"
    }

    @classmethod
    def setUpClass(cls):
        load_db()

    def setUp(self):
        self.auth = base64.b64encode(b'admin:admin').decode()
        self.headers = {"Authorization": f"Basic {self.auth}"}
        self.API_URI = "v1/movies"


    @staticmethod
    def parse_json(movie_json):
        popularity = float(movie_json.get('99popularity', 0))
        director = movie_json.get('director', '').strip()
        genre_list = movie_json.get('genre', [])
        imdb_score = float(movie_json.get('imdb_score', 0))
        name = movie_json.get('name', '').strip()
    

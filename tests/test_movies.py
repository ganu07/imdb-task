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
    
            # Check response 200 with output Success case
            response = client.post(self.API_URI, data=json.dumps(data), headers=self.headers)
            self.assertEqual(ResponseMaker.RESPONSE_200, response.status_code)

            # Check response 400 with entry exists
            response = client.post(self.API_URI, data=json.dumps(data), headers=self.headers)
            self.assertEqual(ResponseMaker.RESPONSE_400, response.status_code)
            self.assertEqual(ResponseMaker.RESPONSE_400_ERROR_ENTRY_PRESENT,
                             json.loads(response.get_data(as_text=True)).get('err_code'))

	# Check 99popularity and imdb score out of bounds
            data['99popularity'] = -1
            response = client.post(self.API_URI, data=json.dumps(data), headers=self.headers)
            self.assertEqual(ResponseMaker.RESPONSE_400, response.status_code)
            self.assertEqual(ResponseMaker.RESPONSE_400_ERROR_OUT_OF_BOUNDS,
                             json.loads(response.get_data(as_text=True)).get('err_code'))

            data['99popularity'] = 101
            response = client.post(self.API_URI, data=json.dumps(data), headers=self.headers)
            self.assertEqual(ResponseMaker.RESPONSE_400, response.status_code)
            self.assertEqual(ResponseMaker.RESPONSE_400_ERROR_OUT_OF_BOUNDS,
                             json.loads(response.get_data(as_text=True)).get('err_code'))


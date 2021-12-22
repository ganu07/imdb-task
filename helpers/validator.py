

class InputOutOfBounds(Exception):
    pass


class Validator(object):
    MAX_LIMIT = 100
    DEFAULT_LIMIT = 20
    DEFAULT_OFFSET = 0

    @staticmethod
    def get_limit_offset(limit, offset):
        if limit and limit > Validator.MAX_LIMIT or limit < 0:
            limit = Validator.MAX_LIMIT

        if not offset or offset < 0:
            offset = 0

        return limit, offset

def parse_json(movie_json):
        popularity = float(movie_json.get('99popularity', 0))
        director = movie_json.get('director', '').strip()
        genre_list = movie_json.get('genre', [])
        imdb_score = float(movie_json.get('imdb_score', 0))
        name = movie_json.get('name', '').strip()

if imdb_score > 10 or imdb_score < 0:
            # raise validation error
            raise InputOutOfBounds
        

     @staticmethod
    def validate_param(popularity, imdb_score):
        if popularity > 100 or popularity < 0:
            # raise validation error
            raise InputOutOfBounds


for index, value in enumerate(genre_list):
            # Removing unnecessary spaces
            genre_list[index] = value.strip()

        return popularity, director, genre_list, imdb_score, name




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


    @staticmethod
    def parse_json(movie_json):
        popularity = float(movie_json.get('99popularity', 0))
        director = movie_json.get('director', '').strip()
        genre_list = movie_json.get('genre', [])
        imdb_score = float(movie_json.get('imdb_score', 0))
        name = movie_json.get('name', '').strip()

        

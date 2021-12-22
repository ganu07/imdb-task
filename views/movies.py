"""
This file contains API endpoints which would be exposed to the outer world
"""

import json

from flask import Blueprint, request

from data_api.movies_dao import MoviesDao
from helpers.auth import basic_auth
from helpers.db import terminating_sn
from helpers.logger import LOG
from helpers.response_maker import ResponseMaker
from helpers.validator import Validator, InputOutOfBounds

blueprint = Blueprint('movies', __name__)


class MissingFields(Exception):
    pass


@blueprint.route('/')
def homepage():
    """
    A test API to check if flask is properly configured
    :return:
    """
    return "Welcome to IMDB API"


@blueprint.route('/v1/movies', methods=['GET'])
def get_movies():
    """
    A GET API to get movies stored in the db
    Request:
    v1/movies?name=test&genre=Adventure&director=Vic&limit=100&offset=0
    :param name: optional
    :param genre: optional
    :param director: optional
    :param limit: optional
    :param offset: optional

    Response:
    :return: 200, SUCCESS for a successful entry
    200 response
    {
    "total": 2,
    "data": [
        {
            "id": 17,
            "99popularity": 82.0,
            "director": "Victor Fleming",
            "genre": [
                "Drama",
                "Romance",
                "War"
            ],
            "imdb_score": 8.2,
            "name": "Gone with the Wind"
        },
        {
            "id": 248,
            "99popularity": 99.0,
            "director": "Victo Fleming",
            "genre": [
                "Adventure",
                "Family",
                "Fantasy"
            ],
            "imdb_score": 8.3,
            "name": "test_input1"
        }
    ]
    }
    :return: 500, INTERNAL SERVER ERROR for issue on server side
    """
    name = request.args.get('name')
    director = request.args.get('director')
    genre = request.args.get('genre')
    limit = int(request.args.get('limit', Validator.DEFAULT_LIMIT))
    offset = int(request.args.get('offset', Validator.DEFAULT_OFFSET))

    limit, offset = Validator.get_limit_offset(limit, offset)

   


@blueprint.route('/v1/movies', methods=['POST'])
@basic_auth
def add_movies():
    """
    An API for adding new movies accepts json input. ALL Fields Mandatory
    Request Body:
    {
    "99popularity": 83.0,
    "director": "Victor Fleming",
    "genre": [
      "Adventure",
      " Family",
      " Fantasy",
      " Musical"
    ],
    "imdb_score": 8.3,
    "name": "The Wizard of Oz"
    }
    Response:
    :return: 200, SUCCESS for a successful entry
    :return: 400, BAD REQUEST for issue in client request side
    :return: 401, UNAUTHORIZED for wrong user access
    :return: 500, INTERNAL SERVER ERROR for issue on server side
    """
    try:
        data = json.loads(request.data)

        if not data:
            raise MissingFields

        popularity, director, genre_list, imdb_score, name = Validator.parse_json(data)
        except (json.decoder.JSONDecodeError, MissingFields):
        return ResponseMaker(ResponseMaker.RESPONSE_400, ResponseMaker.RESPONSE_400_MESSAGE,
                             ResponseMaker.RESPONSE_400_ERROR_MISSING_FIELDS).return_response()
    except InputOutOfBounds:
        return ResponseMaker(ResponseMaker.RESPONSE_400, ResponseMaker.RESPONSE_400_MESSAGE,
                             ResponseMaker.RESPONSE_400_ERROR_OUT_OF_BOUNDS).return_response()
    except Exception:
        session.rollback()
        LOG.exception("Exception occurred while writting movie {} to db".format(name))
        return ResponseMaker(ResponseMaker.RESPONSE_500).return_response(
            ResponseMaker.RESPONSE_500_MESSAGE)

        # Add a validation for popularity and imdb_score

try:
        data = json.loads(request.data)

        if not data:
            raise MissingFields

        popularity, director, genre_list, imdb_score, name = Validator.parse_json(data)

        # Add a validation for popularity and imdb_score
        Validator.validate_param(popularity, imdb_score)

        if not movie_id or not any([popularity, director, genre_list, imdb_score, name]):
            raise MissingFields

        
with terminating_sn() as session:
            if not MoviesDao.movie_id_exists(session, movie_id):
                return ResponseMaker(ResponseMaker.RESPONSE_400,
                                     ResponseMaker.RESPONSE_400_MESSAGE,
                                     ResponseMaker.RESPONSE_400_ERROR_ENTRY_MISSING
                                     ).return_response()

            MoviesDao.edit_movie(session, movie_id, popularity, director, genre_list, imdb_score,
                                 name)
            return ResponseMaker(ResponseMaker.RESPONSE_200).return_response(
                ResponseMaker.RESPONSE_200_MESSAGE)


@blueprint.route('/v1/movies', methods=['PUT'])
@basic_auth
def edit_movies():
    pass
@basic_auth
def delete_movies():
    pass

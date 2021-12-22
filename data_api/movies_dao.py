"""
A data access object file to provide an interface between DB and
it's calling function for the genre and Movies table
"""
from data_api.models import Movies, Cast, MovieGenre, Genres
from data_api.cast_dao import CastDao
from data_api.genre_dao import GenreDao
from helpers.db import enable_foreign_keys


class MoviesDao(object):
    """
    A static Movies dao class to isolate Movies related functionality
    """

    GENRE_MARKER = '$'

    @staticmethod
    def get_genre_blob(genre_list):
        return MoviesDao.GENRE_MARKER.join(genre for genre in genre_list)

    @staticmethod
    def get_genre_list(genre_blob):
        return genre_blob.split(MoviesDao.GENRE_MARKER)

    if imdb_score and imdb_score != movie.imdb_score:
            movie.imdb_score = imdb_score

        if director:
            director_obj = CastDao.check_or_add_cast(session, director)
            movie.director_id = director_obj.id


    @staticmethod
    def add_movie(session, popularity, director, genre_list, imdb_score, name):
        director_obj = CastDao.check_or_add_cast(session, director)

        genre_blob = MoviesDao.get_genre_blob(genre_list)
        movie_obj = MoviesDao.add_movie_to_db(
            session, popularity, director_obj.id, imdb_score, name, genre_blob)
        session.flush()



    @staticmethod
    def edit_movie(session, movie_id, popularity, director, genre_list, imdb_score, name):
        movie = session.query(Movies).filter(Movies.id == movie_id).first()

        if name and name != movie.name:
            movie.name = name
	


    @staticmethod
    def get_movie(session, name, director, genre, limit, offset):
        query = session.query(
            Movies.id, Movies.popularity, Cast.name, Movies.genre_blob, Movies.imdb_score, Movies.name)\
            .join(Cast, Movies.director_id == Cast.id)
           

        return total, resp

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

    @staticmethod
    def movie_id_exists(session, movie_id):
        return bool(session.query(Movies.id).filter(Movies.id == movie_id).first())

    @staticmethod
    def movie_exists(session, name):
        return bool(session.query(Movies.id).filter(Movies.name == name).first())

    @staticmethod
    def add_movie_to_db(session, popularity, director_id, imdb_score, name, genre_blob):
        movie = Movies(popularity, director_id, imdb_score, name, genre_blob)
        session.add(movie)
        return movie

    @staticmethod
    def add_movie(session, popularity, director, genre_list, imdb_score, name):
        director_obj = CastDao.check_or_add_cast(session, director)

        genre_blob = MoviesDao.get_genre_blob(genre_list)
        movie_obj = MoviesDao.add_movie_to_db(
            session, popularity, director_obj.id, imdb_score, name, genre_blob)
        session.flush()

        for genre in genre_list:
            GenreDao.attach_movie_to_genre(session, movie_obj.id, genre)

        session.commit()

    @staticmethod
    def delete_movie_from_db(session, movie_id):
        enable_foreign_keys(session)
        session.query(Movies).filter(Movies.id == movie_id).delete()
        session.commit()

    @staticmethod
    def edit_movie(session, movie_id, popularity, director, genre_list, imdb_score, name):
        movie = session.query(Movies).filter(Movies.id == movie_id).first()

        if name and name != movie.name:
            movie.name = name

        if popularity and popularity != movie.popularity:
            movie.popularity = popularity

        if imdb_score and imdb_score != movie.imdb_score:
            movie.imdb_score = imdb_score

        if director:
            director_obj = CastDao.check_or_add_cast(session, director)
            movie.director_id = director_obj.id

        if genre_list:
            movie.genre_blob = MoviesDao.get_genre_blob(genre_list)
            GenreDao.clear_movie_genre_map(session, movie_id)
            for genre in genre_list:
                GenreDao.attach_movie_to_genre(session, movie_id, genre)

        session.merge(movie)
        session.commit()

    @staticmethod
    def get_movie(session, name, director, genre, limit, offset):
        query = session.query(
            Movies.id, Movies.popularity, Cast.name, Movies.genre_blob, Movies.imdb_score, Movies.name)\
            .join(Cast, Movies.director_id == Cast.id)

        if genre:
            genre_filter = session.query(MovieGenre.movie_id).join(
                Genres, MovieGenre.genre_id == Genres.id).filter(Genres.name == genre)
            query = query.filter(Movies.id.in_(genre_filter))

        if name:
            query = query.filter(Movies.name.ilike("%{}%".format(name)))

        if director:
            query = query.filter(Cast.name.ilike("%{}%".format(director)))

        total = query.with_entities(Movies.id).count()
        resp = query.group_by(Movies.id).offset(offset).limit(limit).all()

        return total, resp
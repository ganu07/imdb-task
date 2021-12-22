"""
A data access object file to provide an interface between DB and
it's calling function for the genre and movie_genre table
"""

from data_api.models import Genres, MovieGenre


class GenreDao(object):
    """
    A static Genre dao class to isolate Genre related functionality
    """
    @staticmethod
    def get_genre(session, name):
        """
        :param session: DB session to passed from caller
        :param name: Genre name to be queried from db
        :return: SQLAlchemy Genre object returned from DB
        """
        return session.query(Genres).filter(Genres.name == name).first()

    @staticmethod
    def add_genre(session, name):
        """
        :param session: DB session to passed from caller
        :param name: Genre name to be added in DB
        :return: Genre object returned from python class
        """
        genre = Genres(name)
        session.add(genre)
        return genre

    @staticmethod
    def attach_movie_to_genre_db(session, movie_id, genre_id):
        """
        :param session: DB session to passed from caller
        :param movie_id: id of the movie to which genre is attached
        :param genre_id: id of genre to which movie is going to be attached
        :return: MovieGenre object return from python class
        """
        movie_genre = MovieGenre(movie_id, genre_id)
        session.add(movie_genre)
        return movie_genre

    @staticmethod
    def attach_movie_to_genre(session, movie_id, genre_name):
        """
        :param session: DB session to passed from caller
        :param movie_id: id of the movie to which genre is going to be attached
        :param genre_name: name of the genre to which movie is going to be attached
        :return: None
        """
        genre_obj = GenreDao.get_genre(session, genre_name)
        if not genre_obj:
            # genre not found, create it.
            genre_obj = GenreDao.add_genre(session, genre_name)
            session.flush()

        GenreDao.attach_movie_to_genre_db(session, movie_id, genre_obj.id)

    @staticmethod
    def clear_movie_genre_map(session, movie_id):
        """
        clear all the genre attached to that movie_id
        :param session: DB session to passed from caller
        :param movie_id: id from which genre is supposed to be cleared
        :return: None
        """
        session.query(MovieGenre).filter(MovieGenre.movie_id == movie_id).delete()

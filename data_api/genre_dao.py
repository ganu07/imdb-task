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

    


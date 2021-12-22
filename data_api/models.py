"""
A file to store all the DB Models
"""

from sqlalchemy import Column, Index, ForeignKeyConstraint
from sqlalchemy.dialects.sqlite import CHAR, REAL, INTEGER, TEXT

from data_api.base import Base


class Movies(Base):
    __tablename__ = 'movies'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    popularity = Column(REAL)
    director_id = Column(INTEGER)
    imdb_score = Column(REAL)
    name = Column(CHAR(100), unique=True)
    genre_blob = Column(TEXT)

    

    def __init__(self, popularity, director_id, imdb_score, name, genre_blob):
        self.popularity = popularity
        self.director_id = director_id
        self.imdb_score = imdb_score
        self.name = name
        self.genre_blob = genre_blob

    def __repr__(self):
        return "Movies table Id={} Popularity={} Director ID={} Imdb Score={} Name={} " \
               "Genre Blob={}".format(self.id, self.popularity, self.director_id,
                                      self.imdb_score, self.name, self.genre_blob)

class Cast(Base):
    __tablename__ = 'cast'
    

    __table_args__ = (
        Index('cast_id_index', 'id'),
        Index('cast_name_index', 'name')
    )



class Genres(Base):
    __tablename__ = 'genres'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(CHAR(20), unique=True)

    
class MovieGenre(Base):
    __tablename__ = 'movie_genre'

    

	def __init__(self, movie_id, genre_id):
        self.movie_id = movie_id
        self.genre_id = genre_id

	def __repr__(self):
        return "Movie Genre Table Id={} Movie ID={}, Genre ID={}".format(
            self.id, self.movie_id, self.genre_id)
   
class Genres(Base):
    __tablename__ = 'genres'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(CHAR(20), unique=True)

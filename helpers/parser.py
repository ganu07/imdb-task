import json

from data_api.movies_dao import MoviesDao

from helpers.db import terminating_sn
from helpers.logger import LOG
from helpers.validator import Validator


class Parser(object):
    def __init__(self, file_location):
        self.file_location = file_location

    def load_file(self):
        file = open(self.file_location)
        data = json.load(file)
        return data


    if not MoviesDao.movie_exists(session, name):
        LOG.info("Movie {} doesn't exists writting".format(name))
        MoviesDao.add_movie(
            session, popularity, director, genre_list, imdb_score, name)
        session.commit()
    else:
        LOG.info("Movie {} exists hence skipping write".format(name))



        for movie in loaded_json:
            popularity, director, genre_list, imdb_score, name = Validator.parse_json(movie)
            LOG.info("Movie {} selected for write".format(name))
            try:
                with terminating_sn() as session:
                    if not MoviesDao.movie_exists(session, name):
                        LOG.info("Movie {} doesn't exists writting".format(name))
                        MoviesDao.add_movie(
                            session, popularity, director, genre_list, imdb_score, name)
                        session.commit()
                    else:
                        LOG.info("Movie {} exists hence skipping write".format(name))
            except Exception:
                LOG.exception("Exception occured while writting movie {} to db".format(name))
                session.rollback()
	except Exception:
                LOG.exception("Exception occured while writting movie {} to db".format(name))
                session.rollback()

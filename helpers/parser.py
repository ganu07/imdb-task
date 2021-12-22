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

    def load_file(self):
        file = open(self.file_location)
        data = json.load(file)
        return data

	def populate(self):
		LOG.info("Populating tables")
		loaded_json = self.load_file()
		LOG.info("Json loaded from file {}".format(self.file_location))

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

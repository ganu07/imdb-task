"""
A data access object file to provide an interface between DB and
it's calling function for the cast table
"""

from data_api.models import Cast


class CastDao(object):
    """
    A static Cast dao class to isolate cast related functionality
    """
    @staticmethod
    def get_cast(session, name):
        """
        :param session: DB session to passed from caller
        :param name: Cast name to be queried from db
        :return: SQLAlchemy Cast object returned from DB
        """
        return session.query(Cast).filter(Cast.name == name).first()

    @staticmethod
    def add_cast(session, name):
        """
        :param session: DB session to passed from caller
        :param name: Cast name to be added in db
        :return: Cast object of python class
        """
        cast_obj = Cast(name)
        session.add(cast_obj)
        return cast_obj

    @staticmethod
    def check_or_add_cast(session, cast_name):
        """
        :param session: DB session to passed from caller
        :param cast_name: Cast name to be queried or added in db
        :return: Cast object queried from db or created with id after session flush
        """
        cast_obj = CastDao.get_cast(session, cast_name)

        if not cast_obj:
            cast_obj = CastDao.add_cast(session, cast_name)
            session.flush()
        return cast_obj


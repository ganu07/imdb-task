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

    


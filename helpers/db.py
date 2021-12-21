from contextlib import contextmanager

from sqlalchemy import create_engine
from data_api.base import Base
from conf.settings import Config
from sqlalchemy.orm import Session


def get_engine():
    return create_engine(Config.SQLITE_PREFIX + Config.SQLITEDB, echo=True)


@contextmanager
def terminating_sn():
    # A context manager which closes session and db connections after use
    sn = session()
    try:
        yield sn
    finally:
        sn.close()
        sn.bind.dispose()


def enable_foreign_keys(sn):
    sn.execute('PRAGMA foreign_keys = ON')

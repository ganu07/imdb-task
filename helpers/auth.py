import functools

from flask import request
from conf.settings import Config
from helpers.response_maker import ResponseMaker


def enforce_auth(username, password):
    return username in Config.EDIT_USER_MAP and Config.EDIT_USER_MAP.get(username) == password


def basic_auth(func):

    pass

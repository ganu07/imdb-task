import functools

from flask import request
from conf.settings import Config
from helpers.response_maker import ResponseMaker


def enforce_auth(username, password):
    return username in Config.EDIT_USER_MAP and Config.EDIT_USER_MAP.get(username) == password


def basic_auth(func):

    @functools.wraps(func)
    def inner(*args, **kwargs):
        auth = request.authorization

        if not auth or not enforce_auth(auth.username, auth.password):
            return ResponseMaker(ResponseMaker.RESPONSE_401).return_response(
                ResponseMaker.RESPONSE_401_MESSAGE)

        return func(*args, **kwargs)
    return inner

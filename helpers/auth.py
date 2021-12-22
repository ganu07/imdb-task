import functools

from flask import request
from conf.settings import Config
from helpers.response_maker import ResponseMaker


def basic_auth(func):

    @functools.wraps(func)
    def inner(*args, **kwargs):
        auth = request.authorization
	if not auth or not enforce_auth(auth.username, auth.password):
            pass

    return inner

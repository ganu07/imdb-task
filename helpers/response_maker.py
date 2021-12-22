import json
from flask import Response


class ResponseMaker(object):
    RESPONSE_200 = 200
    RESPONSE_401 = 401
    RESPONSE_400 = 400
    RESPONSE_500 = 500

	
    RESPONSE_200_MESSAGE = 'SUCCESS'
    RESPONSE_401_MESSAGE = 'UNAUTHORIZED'
    RESPONSE_400_MESSAGE = 'BAD REQUEST'
    RESPONSE_500_MESSAGE = 'INTERNAL SERVER ERROR'



    def __init__(self, status_code, message=None, error_code=None):
        self.status_code = status_code
        self.message = message
        self.error_code = error_code

  def return_response(self, content=None):
        resp = {'message': self.message, 'err_code': self.error_code if self.error_code else ''}
        if content:
            resp = content
        resp = Response(json.dumps(resp), self.status_code)
        resp.headers['Content-Type'] = 'application/json'
        return resp


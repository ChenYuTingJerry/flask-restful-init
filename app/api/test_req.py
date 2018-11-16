from flask import Blueprint
from flask_restful import Resource, Api
from requests import RequestException

from app.exceptions import RequestError
from utils import httprequest as req
from flask import current_app as app
from entities.response import SuccessResponse

bp = Blueprint(name='test', import_name=__name__)
api = Api(bp)


class TestRequest(Resource):
    def get(self):
        try:
            entity = req.get('http://127.0.0.2:5001')
            return SuccessResponse(entity).to_dict(), 200
        except RequestException as e:
            app.logger.error(e)
            raise RequestError(description=str(e))


api.add_resource(TestRequest, '')

from flask import Blueprint
from flask_restful import Resource, Api
from lib import httprequest as req
from entities.response import SuccessResponse

bp = Blueprint(name='test', import_name=__name__)
api = Api(bp)


class TestRequest(Resource):
    def get(self):
        entity = req.get('http://127.0.0.2:5001')
        return SuccessResponse(entity).to_json()


api.add_resource(TestRequest, '')

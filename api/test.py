from flask import Blueprint
from flask_restful import Resource, Api
from lib import httprequest as req
from entities.response import SuccessResponse

bp = Blueprint(name='test', import_name=__name__)
api = Api(bp)


class Test(Resource):
    def get(self):
        x = req.get('http://127.0.0.2:5001')
        return SuccessResponse(x).to_json()


api.add_resource(Test, '/health')

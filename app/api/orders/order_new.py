from flask_restful import Resource, Api
from . import bp

api = Api(bp)


class OrderNew(Resource):
    def get(self):
        return None, 204

api.add_resource(OrderNew, '/new')

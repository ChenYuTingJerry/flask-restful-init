from flask_restful import Resource, Api, reqparse

from app.entities.response import SuccessResponse
from app.api.messages import bp
from ....msg_queue import producer

api = Api(bp)

parser = reqparse.RequestParser()
parser.add_argument('task')


class Message(Resource):
    def post(self):
        args = parser.parse_args()
        producer.publish(body=args['task'], exchange='topic_logs', routing_key='test')
        return SuccessResponse(), 200


api.add_resource(Message, '')

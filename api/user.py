from flask import Blueprint
from flask_restful import Resource, Api, reqparse, abort

from decorator import valid_request
from exceptions import InvalidUsage
from entities.user import UserEntity
from entities.response import SuccessResponse

bp = Blueprint(name='user', import_name=__name__)
api = Api(bp)

# Define request body
user_post_parser = reqparse.RequestParser()
user_post_parser.add_argument(
    'username',
    type=str,
    location='json',
    required=True,
    help='The user\'s username',
)

user_post_parser.add_argument(
    'password',
    type=str,
    location='json',
    required=True,
)


class User(Resource):

    def get(self):
        return SuccessResponse(UserEntity()).to_dict()

    def put(self):
        raise InvalidUsage('Not support post')

    @valid_request
    def post(self):
        args = user_post_parser.parse_args()
        return SuccessResponse({
            "username": args.get('username'),
            "password": args.get('password')
        }).to_dict()





api.add_resource(User, '/health')

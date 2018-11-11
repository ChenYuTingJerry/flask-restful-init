from flask import Blueprint
from flask_restful import Resource, Api, reqparse

from decorators import valid_request
from app.exceptions import InvalidUsage
from ..model.user import UserModel
from ..model.log import LogModel
from entities.response import SuccessResponse
from ..service import user_service as service

bp = Blueprint(name='users', import_name=__name__)
api = Api(bp)

# Define request body
user_post_parser = reqparse.RequestParser()
user_post_parser.add_argument(
    'user_name',
    type=str,
    location='json',
    required=True,
    help='The user\'s username',
)

user_post_parser.add_argument(
    'age',
    type=int,
    location='json',
    required=True,
    help='The user\'s age',
)


class User(Resource):

    def get(self, user_id):
        log_model = LogModel(content='What is mongoDB?', category='TEST')
        log_model.save()
        user = UserModel.find_by_id(user_id)
        if user:
            return SuccessResponse(user.to_entity()).to_dict()
        else:
            return SuccessResponse().to_dict()

    def put(self):
        raise InvalidUsage('Not support post')

    @valid_request
    def post(self):
        args = user_post_parser.parse_args()
        new_id = service.create_user(name=args['user_name'], age=args['age'])
        return SuccessResponse({'id': new_id}).to_dict(), 201


api.add_resource(User, '', '/', '/<int:user_id>')

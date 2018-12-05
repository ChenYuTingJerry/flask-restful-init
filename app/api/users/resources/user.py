from flask_restful import reqparse, Resource, Api

from app.entities.response import SuccessResponse
from app.api.users import bp
from app.entities.exceptions import InvalidUsage
from app.decorators import valid_request
from app.api.users.services import user_service
from flasgger import swag_from

from utils.entity import Entity

api = Api(bp)

# Define request query
user_get_parser = reqparse.RequestParser()
user_get_parser.add_argument('user_id', type=int, location='args', required=True, help='The id of user')

# Define request body
user_post_parser = reqparse.RequestParser()
user_post_parser.add_argument('user_name', type=str, location='json', required=True, help='The user\'s username')

user_post_parser.add_argument('age', type=int, location='json', required=True, help='The user\'s age')


class User(Resource):
    @valid_request
    @swag_from('../../../../swagger/get_user.yml')
    def get(self):
        args = user_get_parser.parse_args()
        user = user_service.get_user(args['user_id'])
        return SuccessResponse(data=user), 200

    def put(self):
        raise InvalidUsage('Not allow to update user')

    @valid_request
    @swag_from('../../../../swagger/post_user.yml')
    def post(self):
        args = user_post_parser.parse_args()
        new_id = user_service.create_user(name=args['user_name'], age=args['age'])
        return SuccessResponse(data=Entity.from_object({'id': new_id})), 201


api.add_resource(User, '')

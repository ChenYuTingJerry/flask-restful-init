from flask_restful import reqparse, Resource, Api

from app.entities.response import SuccessResponse
from app.api.users import bp
from app.exceptions import InvalidUsage
from app.decorators import valid_request
from app.api.users.services import user_service

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

class BaseResource(Resource):
    def get(self):
        raise InvalidUsage('Not supported')

class User(BaseResource):

    def get(self, user_id=None):
        user = user_service.get_user(user_id)
        if user:
            return SuccessResponse(user).to_dict(), 200
        else:
            return None, 204

    def put(self, user_id):
        raise InvalidUsage('Not allow to update user')

    @valid_request
    def post(self):
        args = user_post_parser.parse_args()
        new_id = user_service.create_user(name=args['user_name'], age=args['age'])
        return SuccessResponse({'id': new_id}).to_dict(), 201


api.add_resource(User, '', '/', '/<int:user_id>')

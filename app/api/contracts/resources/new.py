from flask_restful import Api, Resource, reqparse

from app.api.contracts import bp
from app.api.contracts.services import contract_service
from app.entities.response import SuccessResponse

api = Api(bp)

contract_get_parser = reqparse.RequestParser()
contract_get_parser.add_argument('contract_id', type=str, location='args', required=True, help='The id of contract')


class NewContract(Resource):
    def post(self):
        contract_id = contract_service.create_contract()
        return SuccessResponse({'contract_id': contract_id}), 200

    def get(self):
        args = contract_get_parser.parse_args()
        contract_id = args['contract_id']
        return SuccessResponse(contract_service.get_contract(contract_id))


api.add_resource(NewContract, '/new')

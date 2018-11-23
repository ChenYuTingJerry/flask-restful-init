from app.entities.response import ErrorResponse, SuccessResponse
from utils.entity import Entity


class TestResponse:
    def test_no_payload_in_error_response(self):
        response = ErrorResponse()
        assert len(response['error'].keys()) == 0

    def test_no_payload_in_success_response(self):
        response = SuccessResponse()
        assert len(response['data'].keys()) == 0

    def test_payload_is_entity_in_success_response(self):
        entity = Entity.from_object({'key': 'test'})
        response = SuccessResponse(data=entity)
        assert len(response['data'].keys()) is not 0

    def test_payload_is_dict_in_success_response(self):
        response = SuccessResponse(data={'key': 'test'})
        assert len(response['data'].keys()) is not 0

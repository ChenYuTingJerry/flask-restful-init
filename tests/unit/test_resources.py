import json

from app.api.users.services import user_service
from utils.entity import Entity


class TestUserResource:
    def test_get_user(self, client, monkeypatch):
        def mockreturn(_id):
            return Entity.from_object({'id': _id, 'user_name': 'Test', 'age': 15})

        monkeypatch.setattr(user_service, 'get_user', mockreturn)
        response = client.get('/users/1')

        assert response.status_code == 200
        assert response.data

        body = json.loads(response.data)
        assert body.get('status') == 0
        assert body.get('data').get('user_name') == 'Test'
        assert body.get('data').get('age') == 15

    def test_get_no_user(self, client, monkeypatch):
        def mockreturn(_id):
            return None

        monkeypatch.setattr(user_service, 'get_user', mockreturn)
        response = client.get('/users/1')

        assert response.status_code == 204

    def test_put_user(self, client):
        response = client.put('/users/1')
        assert response.status_code == 400

        assert response.data

        body = json.loads(response.data)
        assert body.get('status') == 1
        assert body.get('error').get('type') == 'InvalidUsage'

    # def test_post_user(self):

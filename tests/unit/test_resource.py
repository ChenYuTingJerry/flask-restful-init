import json

from app.api.users.services import user_service
from utils.entity import Entity


class TestUserResource:
    def test_get_user(self, client, monkeypatch):
        def mockreturn(_id):
            return Entity.from_object({'id': _id, 'user_name': 'Test', 'age': 15})

        monkeypatch.setattr(user_service, 'get_user', mockreturn)
        response = client.get('/users?user_id={}'.format(1))

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
        response = client.get('/users?user_id={}'.format(1))

        assert response.status_code == 200
        assert response.data

        body = json.loads(response.data)
        assert body.get('status') == 0
        assert not body.get('data')

    def test_put_user(self, client):
        response = client.put('/users')
        assert response.status_code == 400

        assert response.data

        body = json.loads(response.data)
        assert body.get('status') == 1
        assert body.get('error').get('type') == 'InvalidUsage'

    def test_post_user(self, client, monkeypatch):
        def mockreturn(name, age):
            return 18

        monkeypatch.setattr(user_service, 'create_user', mockreturn)

        response = client.post('/users', json={'user_name': 'Test', 'age': 20})
        assert response.status_code == 201
        assert response.data

        body = json.loads(response.data)
        assert body.get('status') == 0
        assert body.get('data').get('id') == 18

    def test_post_user_with_wrong_format(self, client):
        response = client.post('/users', json={'wrong_name': 'Test', 'age': 20})
        assert response.status_code == 400
        assert response.data

        body = json.loads(response.data)
        assert body.get('status') == 1
        assert body.get('error').get('type') == 'InvalidRequest'


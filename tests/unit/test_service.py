from unittest import mock

from app.api.users.models.user import UserModel
from app.api.users.services import user_service
from utils import httprequest


def test_user_service(monkeypatch):
    def mockreturn(_id):
        return UserModel(id=1, username='Test', age=15)

    monkeypatch.setattr(UserModel, 'find_by_id', mockreturn)
    x = user_service.get_user(1)
    assert x.user_name == 'Test'
    assert x.age == 15

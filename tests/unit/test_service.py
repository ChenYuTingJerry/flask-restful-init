from app.api.users.models.user import UserModel
from app.api.users.services import user_service


class TestUserService:

    def test_get_user(self, monkeypatch):
        def mockreturn(_id):
            return UserModel(id=_id, username='Test', age=15)

        monkeypatch.setattr(UserModel, 'find_by_id', mockreturn)
        x = user_service.get_user(1)
        assert x.user_name == 'Test'
        assert x.age == 15

    def test_get_no_user(self, monkeypatch):
        def mockreturn(_id):
            return None

        monkeypatch.setattr(UserModel, 'find_by_id', mockreturn)
        user = user_service.get_user(1)
        assert not user

    def test_create_user(self, app):
        with app.app_context():
            user_id = user_service.create_user('Test', 15)
            assert type(user_id) == int

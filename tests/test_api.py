from app.api.users.models.user import UserModel


def test_get_no_user(client):
    response = client.get('/users/0')
    assert response.status_code == 204


def test_create_user(app, client, mysql):
    with app.app_context():
        data = {
            'user_name': 'Test King',
            'age': 15
        }

        response = client.post('/users', json=data)

        assert response.status_code == 201

        user = UserModel.query.filter_by(username=data['user_name']).first()
        assert user.age == data['age']


def test_update_user(client):
    response = client.put('/users')
    assert response.status_code == 400

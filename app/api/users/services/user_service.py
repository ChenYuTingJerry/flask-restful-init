from app.api.users.models.user import UserModel


def create_user(name, age):
    user = UserModel(name, age)
    user.save()
    return user.id


def get_user(user_id):
    user = UserModel.find_by_id(user_id)
    if user:
        entity = user.to_entity()
        return entity
    else:
        return None

from app.api.users.model.user import UserModel


def create_user(name, age):
    user = UserModel(name, age)
    user.save()
    return user.id


def get_user(user_id):
    user = UserModel.find_by_id(user_id)
    if user:
        return user.to_entity()
    else:
        return None

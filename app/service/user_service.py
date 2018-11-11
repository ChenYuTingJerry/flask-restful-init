from app.model.user import UserModel


def create_user(name, age):
    user = UserModel(name, age)
    user.save()
    return user.id

from app.model.user import UserModel
from flask import current_app as app


def create_user(name, age):
    user = UserModel(name, age)
    user.save()
    return user.id


def get_user(user_id):
    user = UserModel.find_by_id(user_id)
    app.logger.debug('{}'.format(user))
    if user:
        return user.to_entity()
    else:
        return None

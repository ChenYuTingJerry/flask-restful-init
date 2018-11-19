from flask import current_app as app
from blinker import Namespace

user_signals = Namespace()
user_created = user_signals.signal('user-created')


def user_created_notify(user):
    app.logger.debug('Create {user}'.format(user=user.username))


def connect_handlers():
    user_created.connect(user_created_notify)

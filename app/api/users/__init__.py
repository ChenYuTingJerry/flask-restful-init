from flask import Blueprint

bp = Blueprint(name='users', import_name=__name__)

from app.api.users.resources import user

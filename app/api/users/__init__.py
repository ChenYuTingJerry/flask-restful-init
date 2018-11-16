from flask import Blueprint

bp = Blueprint(name='users', import_name=__name__)

from . import user

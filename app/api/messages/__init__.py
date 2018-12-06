from flask import Blueprint

bp = Blueprint(name='messages', import_name=__name__)

from app.api.messages.resources import message
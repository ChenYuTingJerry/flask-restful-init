from flask import Blueprint

bp = Blueprint(name='contracts', import_name=__name__)

from app.api.contracts.resources import new
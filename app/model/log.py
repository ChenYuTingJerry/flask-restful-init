from datetime import datetime

from lib.constant import db_types
from ..db import get_db
from lib import entity
from . import AbstractModel

db = get_db(db_types.NO_SQL)()


class LogModel(db.Document, AbstractModel):
    issue_time = db.DateTimeField(default=datetime.utcnow)
    category = db.StringField(max_length=50)
    content = db.StringField(max_length=50)
    meta = {'collection': 'log'}

    def to_entity(self):
        return entity.mapper({
            'issue_time': self.issue_time,
            'category': self.category,
            'content': self.content
        })

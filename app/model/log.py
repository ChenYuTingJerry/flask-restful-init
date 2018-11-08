from datetime import datetime
from ..db import mongodb
from lib import entity
from . import AbstractModel

db = mongodb.instance()


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

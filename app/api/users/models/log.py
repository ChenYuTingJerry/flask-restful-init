from datetime import datetime
from app.db import mongodb
from utils import entity

db = mongodb.engine


class LogModel(db.Document):
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

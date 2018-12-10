from app.signal_handlers import user_created
from utils.entity import Entity
from app.db import mysql

db = mysql.engine


class UserModel(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    age = db.Column(db.Integer)

    def __init__(self, username, age, user_id=None):
        self.username = username
        self.age = age
        if user_id:
            self.user_id = user_id

    def save(self):
        db.session.add(self)
        db.session.flush()
        user_created.send(self)

    def delete(self):
        db.session.delete(self)
        db.session.flush()

    def to_entity(self):
        return Entity.from_object({
            'user_id': self.user_id,
            'user_name': self.username,
            'age': self.age
        })

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

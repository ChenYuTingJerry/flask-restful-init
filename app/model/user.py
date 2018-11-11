from ..db import mysql
from utils import entity
from . import AbstractModel

db = mysql.engine


class UserModel(db.Model, AbstractModel):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    age = db.Column(db.Integer)

    def __init__(self, username, age):
        self.username = username
        self.age = age

    def save(self):
        db.session.add(self)
        db.session.flush()

    def delete(self):
        db.session.delete(self)
        db.session.flush()

    def to_entity(self):
        return entity.mapper({
            'id': self.id,
            'user_name': self.username,
            'age': self.age
        })

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

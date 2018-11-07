from lib.constant import db_types
from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine


class SQLInstance:
    def __init__(self):
        self.db = SQLAlchemy()

    def init_db(self, app):
        self.db.init_app(app)
        self.db.create_all()

    def __call__(self):
        return self.db


class NoSQLInstance:
    def __init__(self):
        self.db = MongoEngine()

    def init_db(self, app):
        self.db.init_app(app)

    def __call__(self):
        return self.db


db_pool = {
    db_types.NO_SQL: None,
    db_types.SQL: None
}

_engines = {
    db_types.NO_SQL: NoSQLInstance,
    db_types.SQL: SQLInstance
}


def get_db(db_name):
    db = db_pool.get(db_name, None)
    if not db:
        db = _engines[db_name]()
        db_pool[db_name] = db
    return db

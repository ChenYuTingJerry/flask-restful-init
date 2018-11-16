from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine


class DatabaseProxy:
    def init_db(self, app):
        raise NotImplemented('init_db() needs to be implemented')

    @property
    def engine(self):
        raise NotImplemented('engine() needs to be implemented')

    def commit(self):
        raise NotImplemented('commit() needs to be implemented')

    def rollback(self):
        raise NotImplemented('rollback() needs to be implemented')


_engines = {
    'mongo': MongoEngine(),
    'sql_alchemy': SQLAlchemy()
}


class Mysql(DatabaseProxy):
    def __init__(self):
        self.db = _engines.get('sql_alchemy')

    def init_db(self, app):
        self.db.init_app(app)
        self.db.create_all()

    @property
    def engine(self):
        return self.db

    def commit(self):
        self.db.session.commit()

    def rollback(self):
        self.db.session.rollback()


class Mongodb(DatabaseProxy):
    def __init__(self):
        self.db = _engines.get('mongo')

    def init_db(self, app):
        self.db.init_app(app)

    @property
    def engine(self):
        return self.db


mysql = Mysql()
mongodb = Mongodb()

from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine


class _SQLAlchemySingleton:
    _instance = None

    @staticmethod
    def get_instance():
        if not _SQLAlchemySingleton._instance:
            _SQLAlchemySingleton._instance = SQLAlchemy()
        return _SQLAlchemySingleton._instance


class _MongoEngineSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        if not _MongoEngineSingleton._instance:
            _MongoEngineSingleton._instance = MongoEngine()
        return _MongoEngineSingleton._instance


class Instance:
    def init_db(self, app):
        raise NotImplemented('init_db() needs to be implemented')

    def instance(self):
        raise NotImplemented('get_db_instance() needs to be implemented')


class MysqlInstance(Instance):
    def __init__(self):
        self.db = _SQLAlchemySingleton.get_instance()

    def init_db(self, app):
        self.db.init_app(app)
        self.db.create_all()

    def instance(self):
        return self.db


class MongoInstance(Instance):
    def __init__(self):
        self.db = _MongoEngineSingleton.get_instance()

    def init_db(self, app):
        self.db.init_app(app)

    def instance(self):
        return self.db


mysql = MysqlInstance()
mongodb = MongoInstance()

import pytest
from app import create_app
from app.db import mysql as sql_db


@pytest.fixture(scope='session')
def app():
    app = create_app(config_name='config.test_config')
    return app


@pytest.fixture(scope='session')
def mysql(app, request):
    engine = sql_db.engine

    def teardown():
        with app.app_context():
            engine.drop_all()

    request.addfinalizer(teardown)
    return sql_db


@pytest.fixture(scope='function')
def client(app):
    return app.test_client()

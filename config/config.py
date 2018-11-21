import logging

DEBUG = True
TESTING = False
LOG_PATH = './log/app.log'
LOG_SIZE = 2048
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = '[%(asctime)-12s] %(levelname)s in %(module)s: %(message)s'

DATABASE_NAME = 'dev_db'
SQLALCHEMY_ECHO = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://jerry:password@localhost:3308/{database}'.format(database=DATABASE_NAME)
MONGODB_SETTINGS = {
    'db': 'tm_test',
    'host': '127.0.0.1',
    'port': 27018,
    'username': 'tester',
    'password': 'test_pwd'
}

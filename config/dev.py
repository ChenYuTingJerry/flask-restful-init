import logging

LOG_PATH = './log/app.log'
LOG_SIZE = 2048
LOG_LEVEL = logging.INFO
SQLALCHEMY_ECHO = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://jerry:password@localhost:3308/test_db'
MONGODB_SETTINGS = {
    'db': 'tm_test',
    'host': '127.0.0.1',
    'port': 27018,
    'username': 'tester',
    'password': 'test_pwd'
}
MONGODB_CONNECT = False

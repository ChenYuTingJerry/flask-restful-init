import logging

# settings
DEBUG = True
TESTING = False

# swagger
SWAGGER_TEMPLATE = {
  "swagger": "3.0",
  "info": {
    "title": "Contract Service",
    "description": "API for Contract service",
    "version": "0.0.1"
  },
  "host": "localhost:5000",  # overrides localhost:500
  "basePath": "/",  # base bash for blueprint registration
  "schemes": [
    "http",
    "https"
  ],
  "operationId": "getmyData"
}

# logger
LOG_PATH = './log/app.log'
LOG_SIZE = 2048
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = '[%(asctime)-12s] %(levelname)s in %(module)s: %(message)s'

# database
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

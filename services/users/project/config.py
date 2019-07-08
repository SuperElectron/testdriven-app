# services/users/project/config.py

import os


class BaseConfig:
    """Base configuration"""
    TESTING = False
    DEBUG = False
    SECRET_KEY = os.environ["SECRET_KEY"]


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    MONGODB_SETTINGS = {
        'db': 'devDB',
        'host': 'users-db',
        'port': 27017,
        # 'username': os.environ['MONGO_ROOT_USERNAME'],
        # 'password': os.environ['MONGO_ROOT_PASSWORD']
    }
    DEBUG_TB_ENABLED = True
    BCRYPT_LOG_ROUNDS = 4


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    MONGODB_SETTINGS = {
        'db': 'testDB',
        'host': 'users-db',  # MongoEngine uses database network name from docker-compose.yml
        'port': 27017,
        # 'username': os.environ['MONGO_ROOT_USERNAME'],
        # 'password': os.environ['MONGO_ROOT_PASSWORD']
    }
    BCRYPT_LOG_ROUNDS = 4
    TOKEN_EXPIRATION_DAYS = 0
    TOKEN_EXPIRATION_SECONDS = 3


class ProductionConfig(BaseConfig):
    """Production configuration"""
    MONGODB_SETTINGS = {
        'db': 'prodDB',
        'host': 'mongo',
        'port': 27017,
        # 'username': os.environ['MONGO_ROOT_USERNAME'],
        # 'password': os.environ['MONGO_ROOT_PASSWORD']
    }
    DEBUG = False

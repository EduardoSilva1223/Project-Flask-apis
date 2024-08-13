import os


class DevConfig():

    MONGODB_SETTINGS = {
        'db': os.getenv('MONGO_DB'),
        'host': os.getenv('MONGODB_HOST'),
        'username': os.getenv('MONGODB_USER'),
        'password': os.getenv('MONGODB_PASSWORD'),
    }


class ProdConfig:
    MONGOPRD_USER = os.getenv('MONGODB_USER')
    MONGOPRD_PASSWORD = os.getenv('MONGODB_PASSWORD')
    MONGOPRD_HOST = os.getenv('MONGODB_HOST')
    MONGOPRD_DB = os.getenv('MONGODB_DB')
    MONGODB_SETTINGS = {
        'host': 'mongodb+srv://%s:%s@%s/%s?retryWrites=true&w=majority' % (
            MONGOPRD_USER,
            MONGOPRD_PASSWORD,
            MONGOPRD_HOST,
            MONGOPRD_DB
        )
    }


class MockConfig():
    MONGODB_SETTINGS = {
        'db': 'users',
        'host': 'mongomock://localhost'
    }

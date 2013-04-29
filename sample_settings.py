import os
# Define data used in both Development and production
ADMIN = 'Eric'
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Development(object):
    DEBUG = True
    ADMIN = ADMIN
    BASEDIR = BASEDIR

    # local database login information
    configuration = {
        'db_user': '',
        'db_password': '',
        'port': 5432,
        'host': 'localhost',
        'db_name': 'website'
    }
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{db_user}:{db_password}@{host}:{port}/{db_name}'.format(**configuration)


class Production(object):
    DEBUG = False
    ADMIN = ADMIN
    BASEDIR = BASEDIR

    # local database login information
    configuration = {
        'db_user': '',
        'db_password': '',
        'port': 5432,
        'host': 'localhost',
        'db_name': 'website'
    }
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{db_user}:{db_password}@{host}:{port}/{db_name}'.format(**configuration)

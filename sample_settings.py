# Define data used in both Development and production
ADMIN = 'Eric'

class Development(object):
    DEBUG = True
    ADMIN = ADMIN

class Production(object):
    DEBUG = False
    ADMIN = ADMIN

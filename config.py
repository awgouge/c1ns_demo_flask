import os, uuid

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = uuid.uuid4().hex
    
class ProdConfig(Config):
    DEBUG = False
    SECRET_KEY = uuid.uuid4().hex

class DevConfig(object):
    DEBUG = True
    SECRET_KEY = uuid.uuid4().hex



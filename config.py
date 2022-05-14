import os
class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:4798@localhost/blogs'

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    pass

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    
}
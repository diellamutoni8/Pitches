import os

class Config:
   

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://diella:diella26@localhost/pitches'
    UPLOADED_PHOTOS_DEST ='app/static/photos'  

class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://diella:diella26@localhost/pitches_tests'

class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://diella:diella26@localhost/pitches'


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}

import os


class Config:
    """
    class that defines the app settings
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQL_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    """
    class that defines the settings when in development
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://qagz:password@localhost/blog'
    DEBUG = True


class ProdConfig(Config):
    """
    class that defines the settings for the deployed app
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestConfig(Config):
    """
    class that defines the config for the various tests
    """
    pass


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
import os


class Config:
    """
    class thet defines the app settings
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQL_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    """
    class that defines the settings when in development
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://qagz:password@localhost/pitch'
    DEBUG = True


class ProdConfig(Config):
    """
    class that defines the settings for the deployed app
    """
    pass


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
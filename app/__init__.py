from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


db = SQLAlchemy()

def create_app(config_name):
    """
    creating the app instance to take the specific config and runs the application
    :param config_name:
    :return:
    """

    app = Flask(__name__)

    # creating from config
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    # initialising the app components
    db.init_app(app)
    login_manager.init_app(app)

    # Registering authentication blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_simplemde import SimpleMDE
from flask_uploads import UploadSet, configure_uploads, IMAGES

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()
bootstrap = Bootstrap()
simple = SimpleMDE()
photos = UploadSet('photos', IMAGES)


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

    # Registering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # initialising the app components
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    simple.init_app(app)

    # Registering authentication blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    configure_uploads(app, photos)

    return app

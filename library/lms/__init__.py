from flask import Flask
from lms.config import Config
from lms.database import db
from lms.middleware import init_middlewares
from flask_swagger_ui import get_swaggerui_blueprint
from lms.marshmallow import ma


def create_app(test_config=None):
    app = Flask(__name__)

    swagger_blueprint = get_swaggerui_blueprint(
        Config.SWAGGER_URL,
        Config.API_URL,
        config={
            'app_name': "library management system"
        }
    )
    app.register_blueprint(swagger_blueprint, url_prefix=Config.SWAGGER_URL)

    if test_config is None:
        app.config.from_object(Config)
        # app.config.from_pyfile('config.py')
    else:
        app.config.from_object(test_config)

    db.init_app(app)
    ma.init_app(app)

    from lms.routes.user_route import user_route
    from lms.routes.book_route import book_route
    from lms.routes.library_route import library_route

    app.register_blueprint(user_route)
    app.register_blueprint(book_route)
    app.register_blueprint(library_route)

    init_middlewares(app)

    return app


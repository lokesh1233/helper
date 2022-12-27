from flask import Flask
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'

    from .helper_api import helper_api
    app.register_blueprint(helper_api, url_prefix='/')

    Swagger(app)

    return app

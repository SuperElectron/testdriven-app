#!/usr/bin/env python
# services/users/project/__init__.py

import os
from flask import Flask


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.environ["APP_SETTINGS"]
    app.config.from_object(app_settings)

    # print('secret_key: {}\n\n'.format(app.config['SECRET_KEY']))

    # initialize MongoEngine with app
    from project.db import database
    database.init_app(app)

    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'mongo': database.get_mongoDB()}

    return app

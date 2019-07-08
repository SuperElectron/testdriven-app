# services/users/project/db/database.py

from flask import current_app, g
# from flask.cli import with_appcontext
# from werkzeug.security import generate_password_hash
from project.api.models import User
from flask_mongoengine import MongoEngine

"""
Note:
app.teardown_appcontext(close_db) on line 42 can be commented out.
This gives you the ability to login to database ...
$ mongo --port 27107
> use devDB
> show collections
> db.users.find.pretty()
[lists the users in your database ...]
"""


def get_mongoDB(drop=False):
    """ this function avoids circular referencing when dealing with MongoEngine, or any other database
        Import this to any module/file/function using mongo: from db.db import get_mongoDB
    """
    if ('db' not in g) | (drop is True):
        # connect to mongoEngine and load configuration settings from config.py
        mongo = MongoEngine()
        db = current_app.config["MONGODB_SETTINGS"]['db']
        host = current_app.config["MONGODB_SETTINGS"]['host']
        port = current_app.config["MONGODB_SETTINGS"]['port']

        conn = mongo.connect(db, host=host, port=port, connect=False, alias='default')

        # connect to database and save database into flask's "g" variable
        database = mongo.get_db()

        # print(vars(g))
        # print(dir(mongo))

        if drop:
            conn.drop_database(db)
            return None
        g.db = database

    return g.db


def close_db(e=None):
    """ closes connection to database on port 27017 """
    # print("\n\nremoving mongo from g ...\n\n")
    db = g.pop('mongo', None)
    if db is not None:
        print('possible error disconnecting from mongo ... ')


def init_app(app):
    """ teardown after database request is complete AND initialize cli function """
    app.teardown_appcontext(close_db)  # disconnect DB


def recreate_db():
    """ populate database with admin user """
    db = get_mongoDB()
    collections = db.list_collection_names()

    for item in collections:
        db.drop_collection(item)
    entry = User(username="admin", email="test@gmail.com")
    entry.save()

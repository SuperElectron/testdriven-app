#!/usr/bin/env python
# services/users/manage.py


import sys
import unittest


from flask.cli import FlaskGroup
from project import create_app


app = create_app()
cli = FlaskGroup(create_app=create_app)


# command line actions
@cli.command('recreate_db')
def recreate_db():
    from project.db import database
    with app.app_context():
        database.recreate_db()


@cli.command()
def test():
    """Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)


@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    from project.db import database
    from project.api.models import User

    # get mongoDB connection and add two users
    db = database.get_mongoDB()
    userOne = User(username='matthew', email="matmccann@gmail.com")
    userOne.save()
    userTwo = User(username='bobby', email="bobby@fakeone.com")
    userTwo.save()


if __name__ == '__main__':
    cli()

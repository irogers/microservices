from flask_script import Manager
import unittest

from project import create_app, db
from project.api.models import User

app = create_app()
manager = Manager(app)


@manager.command
def recreate_db():
    """
    This registers a new command to the manager so that we
    can recreate the database from the command line.
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def test():
    """Runs the sests without code coverage."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@manager.command
def seed_db():
    """Seeds the database"""
    db.session.add(User(username='michael', email="michael@realpython.com"))
    db.session.add(User(username='michaelherman', email="michael@mherman.org"))
    db.session.commit()
    

if __name__ == '__main__':
    manager.run()

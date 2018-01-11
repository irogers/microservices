from flask_script import Manager
import unittest

from project import app, db


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

if __name__ == '__main__':
    manager.run()

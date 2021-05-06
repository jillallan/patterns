from patterns.models import User


def test_app(app):
    assert app.config['TESTING']


def test_database(app):
    database_path = app.config['SQLALCHEMY_DATABASE_URI']
    assert 'test' in database_path


def test_populate_database(app):
    user = User.query.filter_by(email='existing@example.com').first()
    assert user is not None

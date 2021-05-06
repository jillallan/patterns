from config import TestConfig
import pytest
from patterns import create_app, db
from patterns.models import User


class AuthActions:
    def __init__(self, client):
        self._client = client

    def login(self, email='existing@email.com', password='password'):
        return self._client.post(
            '/login',
            data={'email': email, 'password': password}
        )

    def logout(self):
        return self._client('/logout')


@pytest.fixture
def app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        populate_database()
        yield app
        db.session.close()
        db.drop_all()
        # db.session.commit()


@pytest.fixture
def client(app):
    # app = create_app()
    return app.test_client()


@pytest.fixture
def auth(client):
    return AuthActions(client)


def populate_database():
    existing_user = User(email='existing@example.com')
    existing_user.set_password('password')
    db.session.add(existing_user)
    db.session.commit()

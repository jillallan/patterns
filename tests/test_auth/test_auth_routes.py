import pytest
from patterns.models import User


@pytest.fixture
def sign_up_post_request(client):
    response = client.post(
        '/sign-up',
        data={
            'email': 'user1@example.com',
            'password': 'password',
            'confirm': 'password'
            }
        )
    return response


def test_sign_up_route(sign_up_post_request):
    assert b'success' in sign_up_post_request.data


def test_sign_up_model(sign_up_post_request, app):
    with app.app_context():
        user = User.query.filter_by(email='user1@example.com').first()
        assert user is not None


def test_sign_up(client, app):
    get_response = client.get('/sign-up')
    assert b'Sign Up' in get_response.data
    assert get_response.status_code == 200

    # post_response = client.post(
    #     '/sign-up',
    #     data={
    #         'email': 'user1@example.com',
    #         'password': 'password',
    #         'confirm': 'password'
    #         }
    #     )
    # assert b'success' in post_response.data

    # with app.app_context():
    #     user = User.query.filter_by(email='user1@example.com').first()
    #     assert user is not None


@pytest.mark.parametrize(
    ('email, password, confirm, message'),
    [
        ('', 'password', 'password', b'Please provide an email'),
        (
            'user.com', 'password',
            'password', b'Please provide a valid email address'
        ),
        ('user@example.com', '', '', b'Please provide a password'),
        (
            'user@example.com', 'pass', 'pass',
            b'Passwords must be between 8 and 25 characters'
        ),
        (
            'user@example.com',
            'passwordpasswordpasswordpassword',
            'passwordpasswordpasswordpassword',
            b'Passwords must be between 8 and 25 characters'
        ),
        (
            'user@example.com', 'password', '',
            b'Please confirm your password'
        ),
        (
            'user@example.com', 'password', 'password1',
            b'Passwords must match'
        ),
    ]
)
def test_sign_up_validation(client, email, password, confirm, message):
    post_response = client.post(
        '/sign-up',
        data={
            'email': email,
            'password': password,
            'confirm': confirm
            }
        )
    assert message in post_response.data


def test_login(client):
    response = client.get('/login')
    assert b'Login' in response.data
    assert response.status_code == 200


@pytest.mark.parametrize(
    ('email, password, message'),
    [
        ('', 'password', b'Please provide an email'),
        ('user.com', 'password', b'Please provide a valid email address'),
        ('user@example.com', '', b'Please provide a password')
    ]
)
def test_login_validation(client, email, password, message):
    response = client.post(
        '/login',
        data={'email': email, 'password': password}
    )
    assert message in response.data

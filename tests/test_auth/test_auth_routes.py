import pytest
from flask_login import current_user
from patterns.models import User


@pytest.fixture
def sign_up_post_request(client):
    response = client.post(
        '/sign-up',
        data={
            'email': 'user@example.com',
            'password': 'password',
            'confirm': 'password'
            }
        )
    return response


@pytest.fixture
def login_post_request(client):
    response = client.post(
        '/login',
        data={
            'email': 'existing@example.com',
            'password': 'password'
            }
        )
    return response


def test_sign_up(client, app):
    get_response = client.get('/sign-up')
    assert b'Sign Up' in get_response.data
    assert get_response.status_code == 200


def test_sign_up_route(sign_up_post_request):
    assert b'success' in sign_up_post_request.data


def test_sign_up_model(sign_up_post_request, app):
    with app.app_context():
        sign_up_post_request
        user = User.query.filter_by(email='user@example.com').first()
        assert user is not None


@pytest.mark.parametrize(
    ('email, password, confirm, message'),
    [
        # Check missing email
        ('', 'password', 'password', b'Please provide an email'),
        # Check invalid email
        (
            'user.com', 'password',
            'password', b'Please provide a valid email address'
        ),
        # Check missing password
        ('user@example.com', '', '', b'Please provide a password'),
        # Check short password
        (
            'user@example.com', 'pass', 'pass',
            b'Passwords must be between 8 and 25 characters'
        ),
        # Check long password
        (
            'user@example.com',
            'passwordpasswordpasswordpassword',
            'passwordpasswordpasswordpassword',
            b'Passwords must be between 8 and 25 characters'
        ),
        # Check missing confirmation password
        (
            'user@example.com', 'password', '',
            b'Please confirm your password'
        ),
        # Check passwords match
        (
            'user@example.com', 'password', 'password1',
            b'Passwords must match'
        ),
        # Check email already exists
        (
            'existing@example.com', 'password', 'password',
            b'Username taken'
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


def test_login_route(login_post_request):
    assert b'success' in login_post_request.data


def test_login_model(login_post_request, client):
    with client:
        login_post_request
        client.get('/success')
        assert current_user.is_authenticated is True


@pytest.mark.parametrize(
    ('email, password, message'),
    [
        ('', 'password', b'Please provide an email'),
        ('user.com', 'password', b'Please provide a valid email address'),
        ('user@example.com', '', b'Please provide a password'),
        ('user@example.com', 'password', b'Invalid username or password'),
    ]
)
def test_login_validation(client, email, password, message):
    response = client.post(
        '/login',
        data={'email': email, 'password': password}
    )
    assert message in response.data


def test_login_redirect(client, auth):
    response = client.get('/dashboard')
    # assert b'Login' in response.data
    assert response.status_code == 302
    assert response.headers['Location'] == \
        'http://localhost/login?next=home_bp.dashboard'

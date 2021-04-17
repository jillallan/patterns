import pytest


def test_sign_up(client):
    get_response = client.get('/sign-up')
    assert b'Sign Up' in get_response.data
    assert get_response.status_code == 200

    post_response = client.post(
        '/sign-up',
        data={
            'email': 'user@example.com',
            'password': 'password',
            'conmfirm': 'password'
            }
        )
    post_response
    assert 'http://localhost' == post_response.headers['Location']


@pytest.mark.parametrize(
    'email, password, confirm, message',
    [
        (
            'user@example.com', 'passw',
            'password12', b'Passwords must match'
        ),
        (
            'user.com', 'password123',
            'password123', b'Please provide a valid email address'
        ),
        (
            'user@example.com', 'pas', 'pas',
            b'Password length must be between 4 and 25 characters'
        ),
        (
            'user@example.com', 'password123',
            '', b'Please confirm your password'
        ),
        ('user@example.com', '', 'password123', b'Please provide a password'),
        ('', 'password123', 'password123', b'Please provide an email')

    ])
def test_sign_up_validation(client, email, password, confirm, message):
    response = client.post(
        '/sign-up',
        data={
            'email': email,
            'password': password,
            'conmfirm': confirm
            }
        )
    assert message in response.data

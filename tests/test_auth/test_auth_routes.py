import pytest


def test_sign_up(client):
    get_response = client.get('/sign-up')
    # assert b'Sign Up' in get_response.data
    get_response
    assert get_response.status_code == 200

    # post_response = client.post(
    #     '/sign-up',
    #     data={
    #         'email': 'user@example.com'
    #         },
    #     follow_redirects=True  # look this up
    #     )
    # assert request.path == 'http://localhost/success'
    # assert request.path == url_for('home_bp.success')
    # assert 'http://localhost/success' == post_response.headers['Location']


@pytest.mark.parametrize(
    ("email, password, confirm, message"),
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

class TestSignUp:
    def __init__(self, client, app):
        self._client = client
        self._app = app

    def test_get_request(self):
        response = self._client.get('/sign-up')
        assert b'Sign Up' in response.data
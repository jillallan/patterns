def test_hello(client):
    response = client.get('/')
    assert b'Hello world' in response.data
    assert response.status_code == 200

from fastapi.testclient import TestClient

from fast_zero.main import app

client = TestClient(app)


def test_root_return_200():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Olá Mundo!'}

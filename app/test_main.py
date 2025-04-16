import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_login_success(client):
    response = client.post('/login', json={'username': 'admin', 'password': 'password'})
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_login_failure(client):
    response = client.post('/login', json={'username': 'wrong', 'password': 'password'})
    assert response.status_code == 401
    assert response.json['msg'] == 'Bad username or password'

def test_get_notes(client):
    response = client.post('/login', json={'username': 'admin', 'password': 'password'})
    token = response.json['access_token']
    response = client.get('/notes', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    assert 'notes' in response.json

def test_missing_token(client):
    response = client.get('/notes')
    assert response.status_code == 401
    assert 'msg' in response.json

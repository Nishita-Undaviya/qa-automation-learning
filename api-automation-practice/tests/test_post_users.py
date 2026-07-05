from conftest import BASE_URL
import requests

def test_create_post():
    payload = {
        "userId" : 11,
        'title': 'Day 2 Task',
        "body" : 'basic API tests against JSONPlaceholder',
    }
    response = requests.post(f'{BASE_URL}/posts', json = payload)
    assert response.status_code == 201
    response_data = response.json()
    assert 'id' in response_data

def test_get_nonexistent_post():
    response = requests.get(f'{BASE_URL}/posts/99999')
    assert response.status_code == 404

def test_post_response_time():
    response = requests.get(f'{BASE_URL}/users')
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2
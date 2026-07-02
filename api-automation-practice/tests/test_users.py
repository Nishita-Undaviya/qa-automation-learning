import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_users_status_code():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200

def test_get_all_users_returns_ten():
    response = requests.get(f"{BASE_URL}/users")
    assert len(response.json()) == 10

def test_single_user_has_required_fields():
    response = requests.get(f"{BASE_URL}/users/1")
    user = response.json()
    assert "name" in user
    assert "email" in user
    assert "username" in user

def test_invalid_user_returns_404():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404
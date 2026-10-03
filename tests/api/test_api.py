import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_users():
    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0


def test_create_user():
    payload = {
        "name": "Rahul N N",
        "username": "rahulnn",
        "email": "rahul@example.com"
    }

    response = requests.post(
        f"{BASE_URL}/users",
        json=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Rahul N N"
    assert data["username"] == "rahulnn"
    assert data["email"] == "rahul@example.com"


def test_get_invalid_user():
    response = requests.get(f"{BASE_URL}/users/9999")

    assert response.status_code == 404
import uuid

import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    return  APIClient()

def test_get_users(api_client):
    response = api_client.get("users")
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_users(api_client, load_user_data):
    # user_data = {
    #     "name": "Kiran Kumar",
    #     "username": "development user",
    #     "email": "development@gmail.com"
    # }
    user_data = load_user_data["new_user"]
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    print(unique_email)
    user_data["email"] = unique_email
    response = api_client.post("users", user_data)
    print(response.json())
    assert response.status_code == 201
    assert response.json()['name'] == "Kiran Kumar"
    id = response.json()['id']
    id = id - 1
    # print(id, ' - 009')
    response = api_client.get(f"users/{str(id)}")
    print(response.json())
    assert response.status_code == 200
    assert response.json()['name'] == "Clementina DuBuque"


def test_update_users(api_client, load_user_data):
    # user_data = {
    #     "name": "Kiran K",
    #     "username": "development user",
    #     "email": "development@gmail.com"
    # }
    user_data = load_user_data["update_existing_user"]
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    print(unique_email)
    user_data["email"] = unique_email
    response = api_client.put("users/2", user_data)
    print(response.json())
    assert response.status_code == 200
    # assert response.json()['name'] == "Kiran K"
    # response = api_client.get(f"users/1")
    # print(response.json())


def test_delete_users(api_client):
    response = api_client.delete("users/1")
    print(response.json())
    assert response.status_code == 200


from starlette.testclient import TestClient
from app import app
# from ItemFactory import Item

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "hello world again!"}

def test_users_endpoint():
    response = client.get("users/1")
    assert response.status_code == 200
    assert response.json() == {"user_id": 1}


def test_item_have_positive_price():

    item = {
        "name": "product",
        "price": 50
    }
    response = client.post(f"/items/", json = item)

    assert response.status_code == 200

def test_item_have_negative_price():

    item = {
        "name": "product",
        "price": -50
    }
    response = client.post(f"/items/", json = item)
    assert response.status_code != 200 
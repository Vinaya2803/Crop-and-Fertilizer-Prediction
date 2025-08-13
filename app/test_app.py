import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home(client):
    """Test the home page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home" in response.data


def test_crop_recommend(client):
    """Test the crop recommendation page"""
    response = client.get("/crop-recommend")
    assert response.status_code == 200
    assert b"Crop" in response.data


def test_fertilizer(client):
    """Test the fertilizer recommendation page"""
    response = client.get("/fertilizer")
    assert response.status_code == 200
    assert b"Fertilizer" in response.data


def test_crop_prediction_valid(client):
    """Test crop prediction with valid input"""
    data = {
        "nitrogen": 100,
        "phosphorous": 40,
        "pottasium": 20,
        "ph": 7.4,
        "rainfall": 86.8,
        "city": "Mumbai",
    }
    response = client.post("/crop-predict", data=data)

    print(response.data)

    assert response.status_code == 200
    assert b"You should grow " in response.data
    assert b"in your farm" in response.data

    predicted_crop = response.data.decode("utf-8")
    assert "You should grow" in predicted_crop
    assert len(predicted_crop.split()) > 0


def test_crop_prediction_invalid_weather(client):
    """Test crop prediction when weather fetch fails (invalid city)"""
    data = {
        "nitrogen": 100,
        "phosphorous": 50,
        "pottasium": 60,
        "ph": 6.5,
        "rainfall": 100.0,
        "city": "InvalidCity",
    }
    response = client.post("/crop-predict", data=data)

    print(response.data)

    assert response.status_code == 200

    assert b"Try again" in response.data


def test_fertilizer_prediction(client):
    """Test fertilizer recommendation with valid input"""
    data = {"cropname": "Wheat", "nitrogen": 30, "phosphorous": 40, "pottasium": 50}
    response = client.post("/fertilizer-predict", data=data)
    assert response.status_code == 200
    assert b"fertilizer" in response.data


def test_fertilizer_prediction_invalid_crop(client):
    """Test fertilizer recommendation with invalid crop name"""
    data = {
        "cropname": "InvalidCrop",
        "nitrogen": 30,
        "phosphorous": 40,
        "pottasium": 50,
    }
    response = client.post("/fertilizer-predict", data=data)
    assert response.status_code == 200
    assert b"No fertilizer" in response.data

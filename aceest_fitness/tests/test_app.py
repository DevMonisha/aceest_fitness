import pytest
from aceest_fitness.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to ACEest Fitness and Gym!" in response.data

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok", "app": "ACEEST Fitness API"}

def test_members(client):
    response = client.get("/members")
    assert response.status_code == 200
    data = response.get_json()
    assert "members" in data
    assert len(data["members"]) == 3

def test_trainers(client):
    response = client.get("/trainers")
    assert response.status_code == 200
    data = response.get_json()
    assert "trainers" in data
    assert len(data["trainers"]) == 2

def test_workouts(client):
    response = client.get("/workouts")
    assert response.status_code == 200
    data = response.get_json()
    assert "workouts" in data
    assert len(data["workouts"]) == 3

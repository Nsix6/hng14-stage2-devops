import pytest
from api.main import app
from fastapi.testclient import TestClient


class MockRedis:
    def __init__(self):
        self.store = {}

    def lpush(self, key, value):
        self.store.setdefault(key, []).append(value)

    def hset(self, key, mapping=None, **kwargs):
        self.store[key] = mapping or kwargs

    def hget(self, key, field):
        return self.store.get(key, {}).get(field)


@pytest.fixture
def client(monkeypatch):
    mock = MockRedis()
    monkeypatch.setattr("api.main.r", mock)
    return TestClient(app)


def test_create_job(client):
    res = client.post("/jobs")
    assert res.status_code == 200
    assert "job_id" in res.json()


def test_get_job_not_found(client):
    res = client.get("/jobs/unknown")
    assert res.json()["error"] == "not found"


def test_job_lifecycle(client):
    res = client.post("/jobs")
    job_id = res.json()["job_id"]

    res2 = client.get(f"/jobs/{job_id}")
    assert res2.json()["status"] == "queued"

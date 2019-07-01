from api import app
from flask import json
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.app_context():
        client = app.test_client()
        yield client

def test_failure_no_args(client):
    response = client.get('/median_pickup_time')

    assert response.status_code == 400
    assert b"Please send appropriate request" in response.data

def test_failure_missing_arg(client):
    response = client.get(
        '/median_pickup_time',
        query_string={
            'location_id': '12',
            'start_time': '2019-01-09T11:00:00'
        }
    )
    assert response.status_code == 400
    assert b"Please send appropriate request" in response.data

def test_failure_character_location(client):
    response = client.get(
        '/median_pickup_time',
        query_string={
            'location_id': 'hello',
            'start_time': '2019-01-09T11:00:00',
            'end_time': '2019-01-09T12:00:00'
        }
    )
    assert response.status_code == 400
    assert b"Please send appropriate request" in response.data

def test_failure_character_time(client):
    response = client.get(
        '/median_pickup_time',
        query_string={
            'location_id': '12',
            'start_time': 'hello',
            'end_time': '2019-01-09T12:00:00'
        }
    )
    assert response.status_code == 400
    assert b"Please send appropriate request" in response.data

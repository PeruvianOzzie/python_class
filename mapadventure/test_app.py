import pytest
import requests
from unittest.mock import patch, Mock 
# from app import get_route, get_location, get_directions
import app 
from flask import Flask
from flask.wrappers import Response
from test.phoenix import get_phoenix
from test.routes import get_routes_resp

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_get_location_Success():
    expected_response = get_phoenix()
    openstreetmap_url = 'https://nominatim.openstreetmap.org/search'
    # openstreetmap_url = 'https://mytestmap.org/search'

    with patch('app.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response

    response = app.get_location("phoenix, AZ", openstreetmap_url)
    assert isinstance(response, list)
    assert all(isinstance(item, str) for item in response)
    assert response == ['33.4484367', '-112.074141']

@patch('app.get_route')
def test_get_route(client):
    expected_response = get_routes_resp()
    openstreetmap_url = 'http://router.project-osrm.org/route/v1/driving/'
    # openstreetmap_url = 'https://mytestmap.org/search'

    # with patch('app.requests.get') as mock_get:
    #     mock_get.return_value.status_code = 200
    #     mock_get.return_value.json.return_value = expected_response

    response = app.get_route(openstreetmap_url, ["37.7274692","-89.216655"], ["39.4842821","-88.3773279"])
    # response = client.get("/get_the_route")

    assert isinstance(response, Response)
    # assert response.destination == ["39.4842821","-88.3773279"]
#     assert response['origin'] == ["37.7274692","-89.216655"]
    # assert response['destination'] == ["39.4842821","-88.3773279"]
#     assert response['route'] == {"coordinates": [
#                         [
#                             -88.952438,
#                             39.845839
#                         ],
#                         [
#                             -88.953093,
#                             39.845818
#                         ],
#                         [
#                             -88.953192,
#                             39.845813
#                         ],
#                         [
#                             -88.953716,
#                             39.845805
#                         ]
#                     ],
#                     "type": "LineString"
#                 }

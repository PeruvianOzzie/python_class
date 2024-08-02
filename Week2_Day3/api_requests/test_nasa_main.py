import pytest
import requests
from unittest.mock import patch, Mock 
from nasa_api import get_nasa_apod




def test_get_nasa_apod_sucess():
    api_key = "valid_api_key"

    expected_response = {
        "date":'2024-07-26', 
        "explanation": "This is a test explanation",
        "url": "https://apod.nasa.gov/apod/image/2107/NGC3576_Hubble_960.jpg",
    }

    with patch('nasa_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response

        response = get_nasa_apod(api_key)
        assert response == expected_response


def test_get_nasa_apod_http_error():
    api_key = "invalid_api_key"

    with patch('nasa_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 403
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError

        response = get_nasa_apod(api_key)
        assert "HTTP error occurred" in response
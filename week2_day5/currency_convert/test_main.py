import pytest
import requests
import sample_peru
import sample_us
import rates_us
from unittest.mock import patch, Mock
from main import get_exchange_rate, convert_currency, get_rate

def test_get_exchange_rate_peruvian_to_dollar():

    expected_response = sample_peru.get_peru_info()

    with patch('main.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response

        response = get_exchange_rate("PEN", "USD")
        assert response == 0.267046
    
def test_get_exchange_rate_dollar_to_peruvian_sol():

    expected_response = sample_us.get_us_info()

    with patch('main.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response

        response = get_exchange_rate("USD", "PEN")
        assert response == 3.751545

def test_convert_currency_peruvian_to_dollar():

    expected_response = sample_peru.get_peru_info()
    with patch('main.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response

        response = convert_currency(100, "PEN", "USD")
        assert response == 26.7046


def test_convert_dollar_to_peruvian_sol():

    expected_response = sample_us.get_us_info()

    with patch('main.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response

        response = convert_currency(100, "USD", "PEN")
        assert response == 375.1545

def test_rates_us():
    
    rates_dic = rates_us.get_us_rates
    print(rates_dic)

    assert 3.751545 == get_rate(rates_dic, "PEN")
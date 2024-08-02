
import pytest
# print(pytest)
from app import greet, get_user_info

def test_greet(monkeypatch):
    # define a mock attribute

    mock_input = "Alice"

    # # use monkeypatch to replace input() with a lambda that returns the mock attribute

    monkeypatch.setattr('builtins.input', lambda _: mock_input)

    result = greet()

    # call the function to check the output 
    assert result == "Hello, Alice!"



def test_get_user_info(monkeypatch):
    
    inputs = iter(["Alice", "25"])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = get_user_info()
    assert result == "Hello, Alice! You are 25 years old."
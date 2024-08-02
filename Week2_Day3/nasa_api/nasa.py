import requests
api_key = "gkcz2AFSb6Sc7YXGLPdbzJLsxmUHhVCHG0uuu6rh"

API_URL = "https://api.nasa.gov/planetary/apod"

def get_nasa_apod(api_key, API_URL):
    
    params = {
        "api_key": api_key
    }

    response = requests.get(API_URL, params)
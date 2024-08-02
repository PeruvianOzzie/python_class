from IPython.display import Image
import requests



def get_location(api_key, query):
    url = 'https://us1.locationiq.com/v1/search.php'
    params = {
        'key': api_key,
        'q': query,
        'format': 'json',
        'limit': 1
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data:
        return data[0]
    return None

API_KEY = 'pk.41844037f8850043d6c80f45745d768e'
location = get_location(API_KEY, 'San Francisco, CA')
print(location)

def get_locationiq_static_image(api_key, lat, lon, zoom=10, width=600, height=400):
    url = f"https://us1.locationiq.com/v1/staticmap"
    params = {
        'key': api_key,
        'center': f'{lat},{lon}',
        'zoom': zoom,
        'size': f'{width}x{height}',
        'format': 'pgn'
    }
    response = requests.get(url, params=params)
    with open("locationiq_map.png", "wb") as file:
        file.write(response.content)
    return "locationiq_map.png"

# latitude = 37.7749
# longitude = -122.4194
latitude = location["lat"]
longitude = location["lon"]

image_path = get_locationiq_static_image(API_KEY, latitude, longitude)
Image(image_path)
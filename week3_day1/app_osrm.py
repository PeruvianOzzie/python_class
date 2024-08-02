from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

openstreetmap_url = 'https://nominatim.openstreetmap.org/search'
open_source_route_mgmt_url = 'http://router.project-osrm.org/route/v1/driving/'


@app.route('/')
def index():
    return render_template('index_osrm.html')

@app.route('/directions', methods=['POST'])
def get_directions():
    origin = request.form['origin']
    destination = request.form['destination']
    
    begin_coordinates = get_location(origin, openstreetmap_url)
    print(f"beggining coordinates: {begin_coordinates}")
    end_coordinates = get_location(destination, openstreetmap_url)
    print(f"ending coordinates: {end_coordinates}")
    
    if begin_coordinates and end_coordinates:
        route = get_route(open_source_route_mgmt_url, begin_coordinates, end_coordinates)
        if None != route:
             return route
             
    return jsonify({'error': 'Location not found'}), 404

def get_route(osrm_url, start_coordinates, end_coordinates):
    # Use OSRM for routing
        osrm_url = f'{osrm_url}{start_coordinates[1]},{start_coordinates[0]};{end_coordinates[1]},{end_coordinates[0]}'
        params = {'overview': 'full', 'geometries': 'geojson'}
        response = requests.get(osrm_url, params=params)
        data = response.json()
        if 'routes' in data and len(data['routes']) > 0:
            route = data['routes'][0]['geometry']
            return jsonify({
                'route': route,
                'origin': start_coordinates,
                'destination': end_coordinates
            })
        else:
             return None

def get_location(query, open_street_map_url):
    req_headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'q': query, 'format': 'json', 'limit': 1}
    response = requests.get(open_street_map_url, params=params, headers=req_headers)
    data = response.json()
    print(data)
    if data:
        return (data[0]['lat'], data[0]['lon'])
    return None

if __name__ == '__main__':
    app.run(debug=True)

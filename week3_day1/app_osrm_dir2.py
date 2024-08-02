from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/directions', methods=['POST'])
def get_directions():
    origin = request.form['origin']
    destination = request.form['destination']
    
    # Use Nominatim to get latitude and longitude
    nominatim_url = 'https://nominatim.openstreetmap.org/search'
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    def get_location(query):
        params = {'q': query, 'format': 'json', 'limit': 1}
        response = requests.get(nominatim_url, params=params, headers=headers)
        data = response.json()
        if data:
            return (data[0]['lat'], data[0]['lon'])
        return None
    
    origin_coords = get_location(origin)
    destination_coords = get_location(destination)
    
    if origin_coords and destination_coords:
        # Use OSRM for routing
        osrm_url = f'http://router.project-osrm.org/route/v1/driving/{origin_coords[1]},{origin_coords[0]};{destination_coords[1]},{destination_coords[0]}'
        params = {'overview': 'full', 'geometries': 'geojson', 'steps': 'true'}
        response = requests.get(osrm_url, params=params)
        data = response.json()
        if 'routes' in data and len(data['routes']) > 0:
            route = data['routes'][0]['geometry']
            steps = data['routes'][0]['legs'][0]['steps']
            print(f"These are the steps: \n {steps}")
            instructions = []
            for step in steps:
                print(f"This is a single step: \n {step}")
                instructions.append(step['maneuver']['instruction'])
            return jsonify({
                'route': route,
                'origin': origin_coords,
                'destination': destination_coords,
                'instructions': instructions
            })
    return jsonify({'error': 'Location not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
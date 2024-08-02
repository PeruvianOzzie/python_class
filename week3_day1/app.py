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
    
    open_street_url = 'https://nominatim.openstreetmap.org/search'
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    def get_location(query):
        params = {'q': query, 'format': 'json', 'limit': 1}
        response = requests.get(open_street_url, params=params, headers=headers)
        data = response.json()
        print(data)
        if data:
            return (data[0]['lat'], data[0]['lon'])
        return None
    


    origin_coords = get_location(origin)
    destination_coords = get_location(destination)
    
    if origin_coords and destination_coords:
        return jsonify({
            'origin': origin_coords,
            'destination': destination_coords
        })
    return jsonify({'error': 'Location not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

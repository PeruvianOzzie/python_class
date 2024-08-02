from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

openstreetmap_url = 'https://nominatim.openstreetmap.org/search'
open_source_route_mgmt_url = 'http://router.project-osrm.org/route/v1/driving/'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showmetheroute', methods=['POST'])
def get_directions():
    origin = request.form['origin']
    destination = request.form['destination']
    
    begin_coordinates = get_location(origin, openstreetmap_url)
    print(f"\n beggining coordinates: {begin_coordinates} \n")
    end_coordinates = get_location(destination, openstreetmap_url)
    print(f"\nending coordinates: {end_coordinates} \n")
    
    if begin_coordinates and end_coordinates:
        route = get_route(open_source_route_mgmt_url, begin_coordinates, end_coordinates)
        if None != route:
             print(f"This is the route to take: \n {route}")
             return route
             
    return jsonify({'error': 'Location not found'}), 404

def get_route(osrm_url, start_coordinates, end_coordinates):
    # Use OSRM for routing
        osrm_url = osrm_url + start_coordinates[1] + "," + start_coordinates[0] + ";" + end_coordinates[1] + "," + end_coordinates[0]
        print(f"osrm url to be called : \n {osrm_url}")
        params = {'overview': 'full', 'geometries': 'geojson', 'steps': 'true', 'annotations': 'true'}
        response = requests.get(osrm_url, params=params)
        data = response.json()
        with open("get_route_output.json", 'w') as file:
             json.dump(data, file, indent=4)
        if 'routes' in data and len(data['routes']) > 0:
            route = data['routes'][0]['geometry']
            return_info = {
                'route': route,
                'origin': start_coordinates,
                'destination': end_coordinates
            }
            # print(f"\nthis is the return from get_route: \n{return_info}\n\n")
            # print(type(jsonify(return_info)))
            return jsonify(return_info)
        else:
             return None

def get_location(query, open_street_map_url):
    return_data = []
    req_headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'q': query, 'format': 'json', 'limit': 1}
    response = requests.get(open_street_map_url, params=params, headers=req_headers)
    rest_data = response.json()
    print(type(rest_data))
    print(f"This is the location data: \n {rest_data}")
    if rest_data:
        return_lon = rest_data[0]['lon']
        print(f"Longitude: {return_lon}")
        return_lat = rest_data[0]['lat']
        print(f"Latitude {return_lat}")
        return_data.append(return_lat)
        return_data.append(return_lon)
        return return_data
    return None

if __name__ == '__main__':
    context = app.app_context()
    context.push()
    with context:
         pass
    app.run(debug=True)

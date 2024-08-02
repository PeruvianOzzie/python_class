def get_routes_resp():
    response = {
        "code": "Ok",
        "routes": [
            {
                "geometry": {
                    "coordinates": [
                        [
                            -88.952438,
                            39.845839
                        ],
                        [
                            -88.953093,
                            39.845818
                        ],
                        [
                            -88.953192,
                            39.845813
                        ],
                        [
                            -88.953716,
                            39.845805
                        ]
                    ],
                    "type": "LineString"
                },
                "legs": [
                    {
                       
                    }
                ],
                "weight_name": "routability",
                "weight": 9070.9,
                "duration": 9070.9,
                "distance": 215225.5
            }
        ],
        "waypoints": [
            {
                "hint": "q-gkgHZxFoQiAAAAIAAAAAAAAAAAAAAAped7Qu5-YEIAAAAAAAAAACIAAAAgAAAAAAAAAAAAAAAuZAAAirGy-s__XwKhsbL6KP5fAgAAvxCaVaLV",
                "distance": 47.007486288,
                "name": "West Eldorado Street",
                "location": [
                    -88.952438,
                    39.845839
                ]
            },
            {
                "hint": "CQI_gP___38eAAAAXQAAAAAAAAAAAAAAZjIIQkvTiUIAAAAAAAAAAB4AAABdAAAAAAAAAAAAAAAuZAAAp8uf-nxrTQJZy5_6vGpNAgAAvwaaVaLV",
                "distance": 22.369756295,
                "name": "Olive Street",
                "location": [
                    -90.190937,
                    38.62822
                ]
            }
        ]
    }

    return(response)
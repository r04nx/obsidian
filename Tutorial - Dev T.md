# Valhalla Routing API Tutorial for VIT Vellore

### API Basics

The Valhalla API operates via HTTP requests:
- Endpoint: `https://routes.alesaservices.com/route`
- Method: POST
- Content-Type: application/json
- Request body: JSON with locations and routing parameters

## Testing the Service

### Simple Test Script

You can test the service using the following script. Save this as `vit_vellore_route_test.sh`:

```bash
#!/bin/bash

# Demo curl request to test Valhalla routing in VIT Vellore
# This requests a route from the VIT Main Gate to the Academic Block

curl -X POST -H "Content-Type: application/json" \
  -d '{
    "locations": [
      {"lat": 12.9691, "lon": 79.1559, "name": "VIT Main Gate"},
      {"lat": 12.9715, "lon": 79.1586, "name": "Academic Block"}
    ],
    "costing": "auto",
    "directions_options": {
      "units": "kilometers",
      "language": "en-US"
    }
  }' \
  https://routes.alesaservices.com/route
```

Make the script executable:

```bash
chmod +x vit_vellore_route_test.sh
```

Run the script:

```bash
./vit_vellore_route_test.sh
```

### Pretty Output Version

If you have `jq` installed, you can use this script for better formatted output:

```bash
#!/bin/bash

# Demo curl request with pretty-printed output
echo "Requesting route from VIT Main Gate to Academic Block..."

curl -s -X POST -H "Content-Type: application/json" \
  -d '{
    "locations": [
      {"lat": 12.9691, "lon": 79.1559, "name": "VIT Main Gate"},
      {"lat": 12.9715, "lon": 79.1586, "name": "Academic Block"}
    ],
    "costing": "auto",
    "directions_options": {
      "units": "kilometers",
      "language": "en-US"
    }
  }' \
  https://routes.alesaservices.com/route | jq '
  {
    status: .trip.status_message,
    distance_km: .trip.summary.length,
    time_seconds: .trip.summary.time,
    directions: [.trip.legs[0].maneuvers[] | {
      instruction: .instruction,
      distance: .length,
      time: .time,
      street_names: (.street_names // [])
    }]
  }'
```

## Request Parameters in Detail

### Core Parameters

- **locations**: Array of points with coordinates
  ```json
  "locations": [
    {"lat": 12.9691, "lon": 79.1559, "name": "VIT Main Gate"},
    {"lat": 12.9715, "lon": 79.1586, "name": "Academic Block"}
  ]
  ```

- **costing**: Transportation mode
  - `auto`: Car routing
  - `bicycle`: Bicycle routing
  - `pedestrian`: Walking routes

- **directions_options**: Output preferences
  ```json
  "directions_options": {
    "units": "kilometers",  // or "miles"
    "language": "en-US"     // language for instructions
  }
  ```

### Additional Parameters

- **costing_options**: Customize routing behavior
  ```json
  "costing_options": {
    "auto": {
      "use_highways": 0.5,     // preference for highways (0-1)
      "use_tolls": 0.3,        // preference for toll roads (0-1)
      "max_speed": 100         // max speed in km/h
    }
  }
  ```

- **avoid_locations**: Points to avoid in routing
  ```json
  "avoid_locations": [
    {"lat": 12.9705, "lon": 79.1565} // avoid this coordinate
  ]
  ```

## VIT Vellore Landmark Coordinates

For testing purposes, here are key landmarks in VIT Vellore:

| Location | Latitude | Longitude |
|----------|----------|-----------|
| Main Gate | 12.9691 | 79.1559 |
| Academic Block | 12.9715 | 79.1586 |
| Men's Hostels | 12.9693 | 79.1528 |
| Ladies Hostels | 12.9740 | 79.1590 |
| Technology Tower | 12.9710 | 79.1570 |
| Library | 12.9705 | 79.1575 |
| Anna Auditorium | 12.9698 | 79.1566 |

## Example Scenarios

### Walking Route

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
    "locations": [
      {"lat": 12.9691, "lon": 79.1559, "name": "Main Gate"},
      {"lat": 12.9705, "lon": 79.1575, "name": "Library"}
    ],
    "costing": "pedestrian",
    "directions_options": {
      "units": "kilometers",
      "language": "en-US"
    }
  }' \
  https://routes.alesaservices.com/route
```

### Route from VIT to Vellore City

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{
    "locations": [
      {"lat": 12.9691, "lon": 79.1559, "name": "VIT Main Gate"},
      {"lat": 12.9167, "lon": 79.1325, "name": "Vellore City Center"}
    ],
    "costing": "auto",
    "directions_options": {
      "units": "kilometers",
      "language": "en-US"
    }
  }' \
  https://routes.alesaservices.com/route
```

## Understanding the Response

The API returns a JSON response with these key components:

1. **trip**: The main container for all route data
   - **status**: Status code (0 = success)
   - **status_message**: Human-readable status
   - **locations**: The input locations, possibly with side-of-street information
   - **legs**: Array of route segments between locations
     - **maneuvers**: Turn-by-turn instructions
       - **instruction**: Text instructions
       - **type**: Maneuver type
       - **street_names**: Names of streets
       - **time**: Estimated time in seconds
       - **length**: Distance in kilometers
     - **summary**: Statistics about the route leg
   - **summary**: Overall statistics
     - **length**: Total distance in kilometers
     - **time**: Total time in seconds
     - **min_lat**, **min_lon**, **max_lat**, **max_lon**: Bounding box
   - **shape**: Encoded polyline of the route geometry

### Example Simplified Response

```json
{
  "trip": {
    "status": 0,
    "status_message": "Found route between points",
    "legs": [{
      "maneuvers": [
        {
          "instruction": "Drive northwest.",
          "street_names": [],
          "time": 11.35,
          "length": 0.044
        },
        {
          "instruction": "Exit the roundabout.",
          "street_names": [],
          "time": 30.469,
          "length": 0.296
        },
        ...
      ],
      "summary": {
        "time": 346.91,
        "length": 3.093
      }
    }],
    "summary": {
      "time": 346.91,
      "length": 3.093
    }
  }
}
```

## Troubleshooting

### Common Issues

1. **404 Error**: The service endpoint is incorrect
2. **400 Error**: Malformed JSON request
3. **No Route Found**: The locations are unreachable from each other
4. **Empty Response**: Network connectivity issues

### Tips

- Double-check coordinate accuracy
- Ensure coordinates are in the correct order (latitude, longitude)
- For complex routes, try breaking into smaller segments
- If a route seems impossible, try a different transportation mode

## Conclusion

The Valhalla routing service at routes.alesaservices.com provides comprehensive coverage for both VIT Vellore campus and the surrounding Vellore area. It supports multiple transportation modes and provides detailed turn-by-turn directions between any two points.

This service can be integrated into applications requiring routing capabilities or used directly via API calls for testing and development purposes.

## References

- [Valhalla GitHub Repository](https://github.com/valhalla/valhalla)
- [Valhalla API Documentation](https://valhalla.readthedocs.io/en/latest/api/turn-by-turn/api-reference/)
- [OpenStreetMap](https://www.openstreetmap.org/)

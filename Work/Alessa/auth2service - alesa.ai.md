# Map Services API Documentation
> Created by: Rohan Pawar
> Last Updated: February 10, 2025

## 1. Tile Server API
**Base URL**: `https://maps.alesaservices.com`

### Endpoint Format
```
GET /tile/{z}/{x}/{y}.png
```
- z: zoom level (0-19)
- x: tile x coordinate
- y: tile y coordinate

### Example Usage
```javascript
// Example with Leaflet.js
var map = L.map('map').setView([18.5204, 73.8567], 13);
L.tileLayer('https://maps.alesaservices.com/tile/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap contributors'
}).addTo(map);
```

## 2. Routing API
**Base URL**: `https://routes.alesaservices.com`

### Basic Route
```
GET /route?loc={start_lat},{start_lon}&loc={end_lat},{end_lon}
```
### Body
```json
{
    "locations": [
        {
            "lat": 51.500729,
            "lon": -0.124625
        },
        {
            "lat": 51.505456,
            "lon": -0.075356
        }
    ],
    "costing": "auto"
}
```
### With Obstacle Avoidance
```
GET /route?loc={start_lat},{start_lon}&loc={end_lat},{end_lon}&avoid_polygons={encoded_polygon}
```

### Example Usage
```bash
# Simple Route (Pune City Center to Hinjewadi)
curl "https://routes.alesaservices.com/route?loc=18.5204,73.8567&loc=18.5912,73.7377"

# Route with Obstacle Avoidance
curl "https://routes.alesaservices.com/route?loc=18.5204,73.8567&loc=18.5912,73.7377&avoid_polygons=wpe%7BcB%7Dkj%60M%7C%40yGnI"
```

### Response Format
```json
{
    "trip": {
        "locations": [...],
        "legs": [{
            "maneuvers": [...],
            "summary": {
                "length": 12.543,
                "time": 1800
            }
        }]
    }
}
```

## Notes
- All coordinates should be in WGS84 format (latitude, longitude)
- Obstacle avoidance polygons must be encoded in polyline format
- Rate limits: 100 requests per minute per IP
- For production use, please contact admin for API keys

## Support
For technical support or access requests, contact:
- Admin: Rohan Pawar
- Email: rohan@alesa.ai
- System Status: https://status.alesaservices.com/status/
# OSM Services Deployment Guide

Our OpenStreetMap (OSM) services are currently deployed and running on VPS2. Here's a quick guide to the available services and their usage.

## Available Services

- **App Interface**: [app.vps2.noulez.app](https://app.vps2.noulez.app)
  - Web interface for testing and visualizing routes
- **Map Tiles**: [maps.vps2.noulez.app](https://maps.vps2.noulez.app)
  - Serves vector map tiles
- **Routing Service**: [routes.vps2.noulez.app](https://routes.vps2.noulez.app)
  - Provides routing APIs

## Quick API Usage Examples

### Basic Routing Request
```javascript
const response = await fetch('https://routes.vps2.noulez.app/route', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    locations: [
      {lat: 13.0827, lon: 80.2707},  // Chennai
      {lat: 12.9716, lon: 77.5946}   // Bangalore
    ],
    costing: 'auto'
  })
});
```

### Obstacle Avoidance Routing
```javascript
const response = await fetch('https://routes.vps2.noulez.app/route', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    locations: [
      {lat: 13.0827, lon: 80.2707},
      {lat: 12.9716, lon: 77.5946}
    ],
    costing: 'auto',
    costing_options: {
      auto: {
        avoid_polygons: [
          {
            // Polygon coordinates to avoid
            coordinates: [
              [lon1, lat1],
              [lon2, lat2],
              [lon3, lat3],
              [lon1, lat1]  // Close the polygon
            ]
          }
        ]
      }
    }
  })
});
```

## Status
All services are currently active and running. Regular updates and maintenance are performed to ensure reliable service.

## Documentation
For detailed documentation and advanced usage:
- Valhalla API Documentation: [https://valhalla.readthedocs.io/](https://valhalla.readthedocs.io/)
- Vector Tiles Documentation: [https://github.com/openmaptiles/openmaptiles](https://github.com/openmaptiles/openmaptiles)

## Notes
- The routing service supports multiple transportation modes (auto, bicycle, pedestrian)
- Custom costing options are available for fine-tuned routing
- Vector tiles support multiple zoom levels and styles

## Capturing Map Coordinates
You can capture coordinates by implementing click events on the map. Here's how:

```javascript
// Initialize the map
const map = L.map('map').setView([13.0827, 80.2707], 13);

// Add the tile layer from our map service
L.tileLayer('https://maps.vps2.noulez.app/styles/basic/{z}/{x}/{y}.png').addTo(map);

// Add click event handler to capture coordinates
map.on('click', function(e) {
    const lat = e.latlng.lat;
    const lng = e.latlng.lng;
    
    // Add a marker at the clicked location
    L.marker([lat, lng]).addTo(map)
        .bindPopup(`Latitude: ${lat}<br>Longitude: ${lng}`);

    // Save to database via API
    saveCoordinates(lat, lng);
});

// Function to save coordinates to database
async function saveCoordinates(lat, lng) {
    try {
        const response = await fetch('https://app.vps2.noulez.app/api/coordinates', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                latitude: lat,
                longitude: lng,
                timestamp: new Date().toISOString(),
                // Add any additional metadata you want to store
            })
        });
        
        if (response.ok) {
            console.log('Coordinates saved successfully');
        } else {
            console.error('Failed to save coordinates');
        }
    } catch (error) {
        console.error('Error saving coordinates:', error);
    }
}
```

### Database Schema Example
If you're using PostgreSQL, here's a sample table structure to store the coordinates:

```sql
CREATE TABLE map_coordinates (
    id SERIAL PRIMARY KEY,
    latitude DECIMAL(10, 8) NOT NULL,
    longitude DECIMAL(11, 8) NOT NULL,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    description TEXT,
    user_id INTEGER REFERENCES users(id),  -- If you have user authentication
    metadata JSONB  -- For any additional data
);

-- Create spatial index for better query performance
CREATE INDEX coordinates_spatial_idx ON map_coordinates USING GIST (
    ST_SetSRID(ST_MakePoint(longitude, latitude), 4326)
);
```

### Retrieving Saved Coordinates
To fetch saved coordinates and display them on the map:

```javascript
async function loadSavedCoordinates() {
    try {
        const response = await fetch('https://app.vps2.noulez.app/api/coordinates');
        const coordinates = await response.json();
        
        coordinates.forEach(coord => {
            L.marker([coord.latitude, coord.longitude]).addTo(map)
                .bindPopup(`Point ID: ${coord.id}<br>Created: ${coord.timestamp}`);
        });
    } catch (error) {
        console.error('Error loading coordinates:', error);
    }
}
```

This setup allows you to:
- Capture precise coordinates from map clicks
- Store coordinates with timestamps and additional metadata
- Retrieve and display saved coordinates
- Perform spatial queries on saved locations
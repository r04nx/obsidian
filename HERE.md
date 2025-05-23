![[Pasted image 20250523160633.png]]
we run the overpass turbo query to extract the data of mumbai for the road segments 
the query was this 
```python
[out:json][timeout:60];
// Define area
{{geocodeArea:Mumbai}}->.searchArea;

// Get all road segments in the area
(
  way["highway"]["name"](area.searchArea);
);
out body;
>;
out skel qt;
```

We got around 4MBs of data and i downloaded in the geojson file
Now i have built a flask web application which is viewing and displaying the map data in a colorful manner and black grey as the background
![[Pasted image 20250523162935.png]]

Now imlpemented the multiple modes from standard, dark theme, light theme, OSM, Streets, Outdoors, Satellite etc
![[Pasted image 20250523171108.png]]

[]

# src.copernicus_s5p_nrti_l3_co.py
import ee
import os
import folium
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Get the project key from the environment variables
gee_project = os.getenv('GEE_PROJECT')

# Authentication and initialization of Google Earth Engine
ee.Authenticate()
ee.Initialize(project=gee_project)

# Load the image collection of carbon monoxide (CO) from the Sentinel-5P satellite
collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_CO') \
    .select(['CO_column_number_density', 'H2O_column_number_density']) \
    .filterDate('2024-09-20', '2024-10-01')  # Filter the images by date range

# Configuration for the visualization of the CO band
band_viz = {
    'min': 0,  # Minimum value of CO for the color scale
    'max': 0.15,  # Adjusted maximum value for a more detailed color scale
    'palette': [
        'black',           # 0.00
        'darkblue',        # 0.01
        'mediumblue',      # 0.02
        'blue',            # 0.03
        'royalblue',       # 0.04
        'dodgerblue',      # 0.05
        'red',             # 0.06
        'darkred',         # 0.07
        'firebrick',       # 0.08
        'crimson',         # 0.09
        'orangered',       # 0.10
        'tomato',          # 0.11
        'coral',           # 0.12
        'salmon',          # 0.13
        'lightsalmon',     # 0.14
        'lightcoral'       # 0.15
    ]  # Expanded color palette for better differentiation, focusing on reds at higher concentrations
}

# Visualization configuration for water vapor
h2o_viz = {
    'min': 0,  # Keeps the minimum at 0
    'max': 4000,  # Adjusts the maximum to include approximately the mean plus two standard deviations
    'palette': ['blue', 'lightblue', 'green', 'yellow', 'orange', 'red']  # Extended color palette for finer gradations
}

# Calculate the mean images for CO and H2O bands
co_mean = collection.mean().select('CO_column_number_density')
h2o_mean = collection.mean().select('H2O_column_number_density')

# Set the map center at the border between Argentina and Brazil
center_lat = -26.0
center_lon = -53.2
zoom_level = 4

# Create a folium map centered at the specified location
map_center = [center_lat, center_lon]
m = folium.Map(location=map_center, zoom_start=zoom_level)

# Add the CO layer using the mean of the CO band
co_mapid = ee.Image(co_mean).getMapId(band_viz)
folium.TileLayer(
    tiles=co_mapid['tile_fetcher'].url_format,
    attr='Google Earth Engine',
    name='S5P CO',
    overlay=True,
    control=True
).add_to(m)

# Add the H2O layer using the mean of the H2O band
h2o_mapid = ee.Image(h2o_mean).getMapId(h2o_viz)
folium.TileLayer(
    tiles=h2o_mapid['tile_fetcher'].url_format,
    attr='Google Earth Engine',
    name='H2O Vapor',
    overlay=True,
    control=True
).add_to(m)

# Add layer control to switch between layers
folium.LayerControl().add_to(m)

# Save the map to an HTML file
m.save('map.html')
print('Map has been saved to map.html')

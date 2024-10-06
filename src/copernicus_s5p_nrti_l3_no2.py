# src.copernicus_s5p_nrti_l3_no2.py
import ee
import os
import geemap
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Get the project key from the environment variables
gee_project = os.getenv('GEE_PROJECT')

# Authentication and initialization of Google Earth Engine
ee.Authenticate()
ee.Initialize(project=gee_project)

# Load the image collection of nitrogen dioxide (NO2) from the Sentinel-5P satellite
collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_NO2') \
    .select('NO2_column_number_density') \
    .filterDate('2024-09-20', '2024-10-03')  # Filter images by date range

# Band display configuration
band_viz = {
    'min': 0,  # Minimum NO2 value for the color scale
    'max': 0.0002,  # Maximum NO2 value for the color scale
    'palette': ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']  # Color palette from low to high concentrations
}

# Compute the mean of the collection
mean_image = collection.mean()

# Create a map centered at the specified location
Map = geemap.Map(center=[-26.0, -53.2], zoom=4)

# Add the mean layer of the collection to the map with the visual configuration
Map.addLayer(mean_image, band_viz, 'S5P NO2')

# Display the map (this works in Jupyter notebooks)
Map

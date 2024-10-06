# src.copernicus_s5p_nrti_l3_hcho.py
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

# Load the image collection of formaldehyde (HCHO) from the Sentinel-5P satellite
collection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_HCHO') \
    .select('tropospheric_HCHO_column_number_density') \
    .filterDate('2024-09-15', '2024-10-03')  # Filter the images by date range

# Configuration for the visualization of the band
band_viz = {
    'min': 0.0,  # Minimum value of HCHO for the color scale
    'max': 0.0003,  # Maximum value of HCHO for the color scale
    'palette': ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']  # Color palette from low to high concentrations
}

# Compute the mean of the collection
mean_image = collection.mean()

# Create a map centered at the specified location
Map = geemap.Map(center=[-26.0, -53.2], zoom=4)

# Add the average of the collection to the map with the visual configuration
Map.addLayer(mean_image, band_viz, 'S5P HCHO')

# Display the map (this works in Jupyter notebooks)
Map
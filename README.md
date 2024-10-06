# NO₂, CO, and HCHO Animation for Latin America

## Overview

This project uses Google Earth Engine (GEE) and the `geemap` library to create animated GIFs and videos showing the density of different gases in the atmosphere over Latin America. The animations cover three compounds:
- Nitrogen Dioxide (NO₂)
- Carbon Monoxide (CO)
- Formaldehyde (HCHO)

These animations visualize the evolution of these pollutants over the selected months, providing an overview of how air quality changes over time.

## Datasets Used

For this project, the following satellite datasets provided by the Copernicus program and NASA were used:

1. **COPERNICUS/S5P/NRTI/L3_NO2**: NO₂ column density data.
2. **COPERNICUS/S5P/NRTI/L3_CO**: CO column density data.
3. **COPERNICUS/S5P/NRTI/L3_HCHO**: Formaldehyde (HCHO) column density data.
4. **NASA/FIRMS**: Fire Information for Resource Management System (FIRMS) fire data.

Each dataset contains information about the density of these gases in the atmosphere. The data was filtered for the desired time period (e.g., June 2024 to October 2024) and the region of interest, which includes Latin America from Brazil southwards.

## Visualization

The animated maps show the temporal evolution of NO₂, CO, and HCHO compounds over Latin America. Additionally, NASA FIRMS fire data is overlaid to visualize the impact of fire occurrences on gas concentrations. Each color in the visualization represents a range of gas density.


### Visualization Parameters:

- **NO₂ (Nitrogen Dioxide)**:
  - **Palette**: ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
  - **Range**: 0.0 to 0.0002 mol/m²
  - **Color Meaning**:
    - **Black**: Very low NO₂ concentration (0.0 - 0.00002 mol/m²)
    - **Blue**: Low NO₂ concentration (0.00002 - 0.00005 mol/m²)
    - **Purple**: Moderate NO₂ concentration (0.00005 - 0.00008 mol/m²)
    - **Cyan**: Moderately high NO₂ concentration (0.00008 - 0.00012 mol/m²)
    - **Green**: High NO₂ concentration (0.00012 - 0.00015 mol/m²)
    - **Yellow**: Very high NO₂ concentration (0.00015 - 0.00018 mol/m²)
    - **Red**: Extremely high NO₂ concentration (0.00018 - 0.0002 mol/m²)

- **CO (Carbon Monoxide)**:
  - **Palette**: ['black', 'navy', 'blue', 'dodgerblue', 'cyan', 'lime', 'yellow', 'orange', 'red', 'darkred']
  - **Range**: 0.0 to 0.05 mol/m²
  - **Color Meaning**:
    - **Black**: Very low CO concentration (0.0 - 0.005 mol/m²)
    - **Navy**: Low CO concentration (0.005 - 0.01 mol/m²)
    - **Blue**: Moderate CO concentration (0.01 - 0.015 mol/m²)
    - **Dodgerblue**: Moderately high CO concentration (0.015 - 0.02 mol/m²)
    - **Cyan**: High CO concentration (0.02 - 0.025 mol/m²)
    - **Lime**: Very high CO concentration (0.025 - 0.03 mol/m²)
    - **Yellow**: Very high CO concentration (0.03 - 0.035 mol/m²)
    - **Orange**: Extremely high CO concentration (0.035 - 0.04 mol/m²)
    - **Red**: Severe CO concentration (0.04 - 0.045 mol/m²)
    - **Dark Red**: Extremely severe CO concentration (0.045 - 0.05 mol/m²)

- **HCHO (Formaldehyde)**:
  - **Palette**: ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
  - **Range**: 0.0 to 0.0003 mol/m²
  - **Color Meaning**:
    - **Black**: Very low HCHO concentration (0.0 - 0.00005 mol/m²)
    - **Blue**: Low HCHO concentration (0.00005 - 0.0001 mol/m²)
    - **Purple**: Moderate HCHO concentration (0.0001 - 0.00015 mol/m²)
    - **Cyan**: Moderately high HCHO concentration (0.00015 - 0.0002 mol/m²)
    - **Green**: High HCHO concentration (0.0002 - 0.00025 mol/m²)
    - **Yellow**: Very high HCHO concentration (0.00025 - 0.00028 mol/m²)
    - **Red**: Extremely high HCHO concentration (0.00028 - 0.0003 mol/m²)

Country borders have been added to all visualizations to facilitate the identification of regions.

## Animation Generation

The code generates two types of output files for each compound:

1. **Animated GIFs**: An animated GIF showing the concentration changes over time.
2. **Videos Exported to Google Drive**: Videos are also exported directly to Google Drive for further use.

## Requirements

- Python 3.8+
- Libraries:
  - `earthengine-api`
  - `geemap`
  - `dotenv`

Make sure you have a Google Earth Engine account and that authentication is properly configured. We use a `.env` file to store the GEE project credentials.

## Usage

To run the script and generate the animations:

1. Clone the repository.
2. Create a `.env` file in the main directory with the content:
   ```
   GEE_PROJECT=your_gee_project
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script for each compound (NO₂, CO, HCHO):
   ```bash
   python src/animation_COPERNICUS_S5P_NRTI_L3_NO2.py
   ```

## Notes

- Adding text to the animations has not yet been implemented due to limitations of the Google Earth Engine API in Python.
- The animations are generated from 4-day average composites, which allows for visualizing general patterns without losing too much temporal resolution.

## Results

- **NO₂_Animation_LatinAmerica.gif**: Animation showing NO₂ levels.
- **CO_Animation_LatinAmerica.gif**: Animation showing CO levels.
- **HCHO_Animation_LatinAmerica.gif**: Animation showing HCHO levels.

These animations are useful for observing how pollution levels change in Latin America and can provide valuable information for environmental and air quality studies.

## Contribution

If you wish to contribute to the project, please fork the repository and open a Pull Request with your changes. Improvements to the analysis functionality or the implementation of new visualizations are welcome.

## License

This project is licensed under the MIT License.
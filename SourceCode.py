import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import gaussian_kde
import folium
from folium.plugins import MarkerCluster


autoBurglaryData = pd.read_csv()#<-- INSERT DATASET PATH LOCATION(LOOK AT DATASETDOWNLOAD.md)
autoBurglaryData.sort_values(by=['Incident Date'], inplace=True)

CleanedData = pd.DataFrame()
for index, row in autoBurglaryData.head(12000).iterrows():
    if row['Incident Subcategory'] in ['Motor Vehicle Theft', 'Larceny - From Vehicle']:
        CleanedData = pd.concat([CleanedData, row.to_frame().transpose()], ignore_index=True)

CleanedData = CleanedData.dropna(subset=['Latitude', 'Longitude'])

# Now, we are left with a clean dataset that contains ONLY auto burglary-related crimes 
# from the first 12000 rows. The dataset also omits any rows that have NA Latitude and
# Longitude values.

# Marker Cluster Map
map_center = [CleanedData['Latitude'].mean(), CleanedData['Longitude'].mean()]
sf_map = folium.Map(location=map_center, zoom_start=12)

# Create a MarkerCluster object
marker_cluster = MarkerCluster().add_to(sf_map)

# Add markers to the cluster
for idx, row in CleanedData.iterrows():
    folium.Marker(location=[row['Latitude'], row['Longitude']]).add_to(marker_cluster)

# Display the map
sf_map



#Matplotlib Kernel Density Estimation Map:


CleanedData['Latitude'] = pd.to_numeric(CleanedData['Latitude'], errors='coerce')
CleanedData['Longitude'] = pd.to_numeric(CleanedData['Longitude'], errors='coerce')

# Drop NaN values that could have appeared during the type conversion
CleanedData.dropna(subset=['Latitude', 'Longitude'], inplace=True)

# Set the size of the plot
plt.figure(figsize=(12, 8))

# Create the KDE plot
sns.kdeplot(data=CleanedData, x='Longitude', y='Latitude', cmap="Reds", shade=True, bw_adjust=0.5)

# Optionally add a scatter plot on top to show the individual points
sns.scatterplot(data=CleanedData, x='Longitude', y='Latitude', color='blue', alpha=0.1)

# Show the plot
plt.show()




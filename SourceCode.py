import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
import folium
from folium.plugins import HeatMap

autoBurglaryData = pd.read_csv()#<-- INSERT DATASET PATH LOCATION(LOOK AT DATASETDOWNLOAD.md)
autoBurglaryData.sort_values(by=['Incident Date'], inplace=True)

CleanedData = pd.DataFrame()
for index, row in autoBurglaryData.head(12000).iterrows():
    if row['Incident Subcategory'] in ['Motor Vehicle Theft', 'Larceny - From Vehicle']:
        CleanedData = pd.concat([CleanedData, row.to_frame().transpose()], ignore_index=True)

CleanedData = CleanedData.dropna(subset=['Latitude', 'Longitude'])

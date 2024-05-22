# Importing libaries

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Loading data
data = pd.read_parquet('DataGBIF_Final_smallV2.parquet')

# Ensure MKOOD column to string and adding "00" to match with shapefile format
data['MKOOD'] = data['MKOOD'].astype(str).str.zfill(4)

#Checking the data
data.head()


# Group by 'MKOOD' and calculating distinct species count
result = data.groupby('MKOOD')['species'].nunique().reset_index()

# Renaming the column to 'species_count'
result.rename(columns={'species': 'species_count'}, inplace=True)

#Importing counties shapefile
shapefile = gpd.read_file('maakond.shp')
shapefile['MKOOD'] = shapefile['MKOOD'].astype(str).str.strip()

Merging species count data with shapefile
merged = shapefile.merge(result, on='MKOOD')


# Plotting the species richness map
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
plot = merged.plot(column='species_count', 
                   cmap='YlOrRd', 
                   linewidth=0.8, 
                   ax=ax, 
                   edgecolor='0.8', 
                   legend=True)

leg = plot.get_legend()
if leg is not None:
    leg.set_bbox_to_anchor((1, 0.5))  # Adjust the position of the legend
    leg.set_title('Species Count', prop={'size': 10})  # Set the legend title size
    for text in leg.get_texts():
        text.set_fontsize(8)  # Set the legend text size

# title
ax.set_title('Species Richness Map', fontsize=15)
ax.set_axis_off()

# Saving as pdf if needed  (uncomment then)
#plt.savefig('species_richness_map.pdf', format='pdf')

# Show the plot
plt.show()


# Species density plot

# Extracting the latitude and longitude from data
x = data['decimalLongitude']
y = data['decimalLatitude']

# Createing the hexbin plot with colormap
plt.figure(figsize=(10, 8))
hb = plt.hexbin(x, y, gridsize=50, cmap='inferno', mincnt=1)

# Adding a color bar
cb = plt.colorbar(hb, label='Count')

# titles and labels
plt.title('Species Density Hexbin Plot', fontsize=15)
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Save the plot as a PDF if needed (uncomment then)
#plt.savefig('species_density.pdf', format='pdf')

# Show the plot
plt.show()

#Importing libaries
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Reading the data file
df=pd.read_csv("0007120-240506114902167.csv")


# Subsetting latitude and longitude
df_subset = df[['decimalLatitude', 'decimalLongitude']]

# Creating GeoDataFrame from points
geometry = [Point(xy) for xy in zip(df_subset['decimalLongitude'], df_subset['decimalLatitude'])]
gdf_points = gpd.GeoDataFrame(df, geometry=geometry)
gdf_points.set_crs(epsg=4326, inplace=True)

# Loading counties shapefile
gdf_counties = gpd.read_file('maakond.shp')
gdf_counties.to_crs(epsg=4326, inplace=True)

# Performing spatial join
gdf_joined = gpd.sjoin(gdf_points, gdf_counties, how="left", op="within")

# Merging the spatial join result with the original DataFrame
result = pd.merge(df, gdf_joined.drop(columns=['decimalLatitude', 'decimalLongitude']), left_index=True, right_index=True)

# Saving file as .csv file
subset_df.to_csv('DataGBIF_Final.csv', index=False)

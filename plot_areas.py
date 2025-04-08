
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

places = [
    (22052, 'Decatur'),
    (56112, 'North Decatur'),
    (24264, 'Druid Hills'),
    (56168, 'North Druid Hills')
]

shapefile_path = "data/tl_2024_13_place/tl_2024_13_place.shp"

# Read the shapefile into a GeoDataFrame
gdf = gpd.read_file(shapefile_path)

# the rows we care about
place_geos = [
    (gdf[gdf['PLACEFP'] == str(place_id)], place_name)
    for place_id, place_name in places
]

for (place, name) in place_geos:
    place.plot()
    plt.title(name)
plt.show()
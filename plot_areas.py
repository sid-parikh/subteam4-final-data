
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
from shapely.geometry import Point
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

stops_df = pd.read_csv('data/google_transit/stops.txt')

places = defaultdict(list)

for index, row in stops_df.iterrows():
    stop_lon = row['stop_lon']
    stop_lat = row['stop_lat']
    for (place, name) in place_geos:
        if any(place.geometry.contains(Point(stop_lon, stop_lat))):
            places[name].append((stop_lon, stop_lat))

for (place, name) in place_geos:
    place.plot()
    for (lon, lat) in places[name]:
        plt.scatter(lon, lat, color='black', s=5)
    plt.title(f'{name} Transit Stops')
    plt.savefig(f'data/places/{name}.png')
plt.show()
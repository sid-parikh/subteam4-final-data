import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# from data/places.txt
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

# plot each place
# for place in places:
#     place.plot()
# plt.show()

stops_df = pd.read_csv('data/google_transit/stops.txt')

# for each stop, check if the [stop_lon, stop_lat] is within any of the four geoids
stops_count = dict()
for index, row in stops_df.iterrows():
    stop_lon = row['stop_lon']
    stop_lat = row['stop_lat']
    for (place, name) in place_geos:
        if any(place.geometry.contains(Point(stop_lon, stop_lat))):
            stops_count[name] = stops_count.get(name, 0) + 1

print(stops_count)

# write the stops_count to a csv
with open('data/results.csv', 'w') as f:
    f.write("Place,Number of Stops\n")
    for name, count in stops_count.items():
        f.write(f"{name},{count}\n")

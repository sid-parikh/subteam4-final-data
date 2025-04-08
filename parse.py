import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point
from dataclasses import dataclass
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

stops_df = pd.read_csv('data/google_transit/stops.txt')

# results
@dataclass
class Place:
    total_stops: int
    num_wheelchair_stops: int

places = dict()

for index, row in stops_df.iterrows():
    stop_lon = row['stop_lon']
    stop_lat = row['stop_lat']
    for (place, name) in place_geos:
        if any(place.geometry.contains(Point(stop_lon, stop_lat))):
            places[name] = places.get(name, Place(0, 0))
            places[name].total_stops += 1
            if row['wheelchair_boarding'] == 1:
                places[name].num_wheelchair_stops += 1

# write to csv
with open('data/results.csv', 'w') as f:
    f.write("Place,Number of Stops,Number of Wheelchair Stops\n")
    for name, place in places.items():
        f.write(f"{name},{place.total_stops},{place.num_wheelchair_stops}\n")

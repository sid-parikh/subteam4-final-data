## Data
`data/tl_2024_13_place` is from [Census.gov](https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2024&layergroup=Places); it represents all the place-equivalents in GA as geometric shapes

`data/google_transit/stops.txt` is from [MARTA](https://www.itsmarta.com/app-developer-resources.aspx); it contains, among other things, a list of all stops in MARTA. It uses the [google transit](https://developers.google.com/transit/gtfs/) format. there is more data available but due to its size only stops.txt is tracked in git right now.

`data/places.txt` is from [Census.gov](https://www2.census.gov/geo/docs/reference/codes/PLACElist.txt). It's just to map place names to IDs.

`data/results.csv` is the output of `parse.py`. still a WIP but right now shows stops in each area specified

to run the script do `pip install -r requirements.txt` and `python parse.py`. the main libraries used are geopandas and pandas. you can also plot the shapes (looks pretty cool) with matplotlib.
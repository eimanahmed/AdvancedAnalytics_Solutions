import pandas as pd, folium, math
from folium.plugins import HeatMap

nypd_data = pd.read_csv("nypd_data.csv")

nypd_data.dropna()
latitude_mean = nypd_data["Latitude"].mean()
longitude_mean = nypd_data["Longitude"].mean()

map = folium.Map(location=[latitude_mean,longitude_mean],zoom_start=10.5)

list_of_datapoints = []
for index, each_row in nypd_data.iterrows():
    if not math.isnan(each_row["Latitude"]):
        list_points = []
        list_points.append(each_row["Latitude"])
        list_points.append(each_row["Longitude"])
        list_of_datapoints.append(list_points)

HeatMap(list_of_datapoints).add_to(map)
map.save("heatmap_nyc.html")
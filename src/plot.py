# Package Import
import os
import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np
from mpl_toolkits.basemap import Basemap
from dotenv import load_dotenv
from locations import locations

load_dotenv()
style.use('ggplot')

# Variables
home_lat = float(os.getenv("LAT"))
home_long = float(os.getenv("LONG"))
center_lat, center_lon = home_lat, home_long


# Initialize the map
plt.figure(figsize=(10, 8))
m = Basemap(projection='merc', llcrnrlat=center_lat-3, urcrnrlat=center_lat+3,
            llcrnrlon=center_lon-3, urcrnrlon=center_lon+3, resolution='l',)

# Draw coastlines, countries, and states
m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.drawlsmask(land_color='#34b238', ocean_color='#2c88ea', lakes=True)

# Plot points and connect them to the center point
offset=10000
for city, (lat, lon) in locations.items():
    x, y = m(lon, lat)
    m.plot(lon, lat, markersize=10, label=city)
    m.drawgreatcircle(center_lon, center_lat, lon, lat, linewidth=3, color='#fc74fc', alpha=0.8)
    print(
        f'City: {city} @ {x}, {y}'
    )
    if city!="Durham, ME":
        plt.text(x, y-offset, city, fontsize=8)
    else:
        plt.text(500000, y+offset, city, fontsize=8)

plt.savefig('output/result.png', format='png')
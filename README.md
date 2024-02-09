# connection-plot
a gift

#### How To
I'm sure there's an easier way, but the method I chose is to create a dictionary with key locations.
The key of the dict is the location name, and the value is a tuple with the lat and long. For example,
```python
locations={
    "New York City, NY": (40.7128, -74.0060),
}
```
Note these should be rounded to four decimal places, and also throw errors if they are too close together. 

I also chose to hide the lat long of the home address in an env file. You may choose to handle this
however you want. 

From there, you'll need to mess around with the offset params. For example in the below code:
```python
m = Basemap(projection='merc', llcrnrlat=center_lat-3, urcrnrlat=center_lat+3,
            llcrnrlon=center_lon-3, urcrnrlon=center_lon+3, resolution='l',)
```
The `llcrnrlat` etc. arguments have an abritrary offset. I just sort of eye-balled the results.
The offset params in the for-loop are similarly arbitrary.
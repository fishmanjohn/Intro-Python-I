# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class Latlon:
    def __init__(self,lat=0, lon=0):
        self.lat = lat 
        self.lon = lon
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(Latlon):
    def __init__(self,name,lat=0,lon=0):
        self.name = name
        super().__init__(lat,lon)
    def __str__(self):
        return f"Waypoint: {self.name}, {self.lat}, {self.lon}"

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self,name,difficulty,size,lat=0,lon=0):
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lat, lon)
    def __str__(self):
        return f"Geocache: {self.name}, {self.difficulty}, {self.size}, {self.lat}, {self.lon}"
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
#waypoint.__init__(name = "Catacombs", lat = 41.70505, lon = -121.51521)
catacombs =  Waypoint("Catacombs", 41.70505, -121.51521)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(catacombs)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
#geocache.__init__(name = "Newberry Views", difficulty = 1.5, size = 2, lat = 44.052137, lon = -121.41556)

newberry_views = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(newberry_views)

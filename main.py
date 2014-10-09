from GPSProximity import *
from correlateDataPoints import *
from getRefugeeData import *
from getWeatherData import *

weatherData = getRefugeeData()
refugeeData = getWeatherData()
results = correlateDataPoints(weatherData, refugeeData, 100000)
if len(results) > 0:
  print results[0]
else:
  print "No results!"

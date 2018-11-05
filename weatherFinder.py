from weather import Weather, Unit
from geotext import GeoText
import random

weather = Weather(unit=Unit.CELSIUS)
def getText():
	foo = ["What is the location?","Say the location.","Which city's weather is needed?","For which location?"]
	print(random.choice(foo))
	return GeoText(input())

def getCities (tex):
	return tex.cities

def printOut (city):
        location = weather.lookup_by_location(city[0])
        forecasts = location.forecast
        fc = forecasts[0]
        fcs = forecasts[1]
        print("In "+city[0]+" it is "+fc.text+" today . With a high of "+fc.high+" and a low of "+fc.low+".")
        print("In "+city[0]+" it will be "+fcs.text+" tomorrow . With a high of "+fcs.high+" and a low of "+fcs.low+".")

CITY = getText()
x = getCities(CITY)
printOut(x)

from weather import Weather, Unit

weather = Weather(Unit.CELSIUS)
lookup = weather.lookup_by_latlng(53.3494, -6.2601)
condition = lookup.condition
print(condition.text)

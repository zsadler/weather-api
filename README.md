weather-api
===========

[![Build
Status](https://travis-ci.org/AnthonyBloomer/weather-api.svg?branch=master)](https://travis-ci.org/AnthonyBloomer/weather-api)
[![codecov](https://codecov.io/gh/AnthonyBloomer/weather-api/branch/master/graph/badge.svg)](https://codecov.io/gh/AnthonyBloomer/weather-api)

A Python wrapper for the Yahoo Weather API.

With the API, you can get up-to-date weather information for any
location, including 5-day forecast, wind, atmosphere, astronomy
conditions, and more. You can lookup weather by woeid, city name or
lat/long.

For more information, check out the [API documentation](https://developer.yahoo.com/weather/documentation.html).

Install
-------

    pip install weather-api

Examples
--------

Lookup WOEID via <http://weather.yahoo.com>.

``` python
from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)

lookup = weather.lookup(560743)
condition = lookup.condition

print(condition.text)
```

Lookup via location name.

``` python
weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('dublin')
condition = location.condition
print(condition.text)
```

Get weather forecasts for the upcoming days.

``` python
weather = Weather(unit=Unit.CELSIUS)

forecasts = location.forecast
for forecast in forecasts:
    print(forecast.text)
    print(forecast.date)
    print(forecast.high)
    print(forecast.low)
```

Lookup via latitude and longitude

``` python
weather = Weather(Unit.CELSIUS)
lookup = weather.lookup_by_latlng(53.3494, -6.2601)
condition = lookup.condition
print(condition.text)
```

For more examples, check the [Examples folder](https://github.com/AnthonyBloomer/weather-api/tree/master/examples)

CLI Usage
---------

``` bash
usage: __main__.py [-h] [--unit [{c,f}]] [--log] [--start [START]]
                   [--end [END]]
                   location

positional arguments:
  location         The location to lookup.

optional arguments:
  -h, --help       show this help message and exit
  --unit [{c,f}]   The unit to be used. Default is Celsius.
  --log            Pass this argument to output logging
  --start [START]  The forecast start
  --end [END]      The forecast end

```

### Example

``` bash
$ weather dublin --u c
```

## Rate Limits

Use of the Yahoo Weather API should not exceed reasonable request volume. Access is limited to 2,000 signed calls per day.

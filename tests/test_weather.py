import unittest
from requests.exceptions import HTTPError
from weather import Weather, Unit


class WeatherTests(unittest.TestCase):
    def test_lookup(self):
        w = Weather(Unit.CELSIUS)
        data = w.lookup(woeid=560743)
        self.assertIsNotNone(data.print_obj)
        self.assertTrue('Dublin' in data.description)
        self.assertIsNotNone(data.astronomy.sunrise)
        self.assertIsNotNone(data.astronomy.sunset)
        self.assertIsNotNone(data.atmosphere.humidity)
        self.assertIsNotNone(data.atmosphere.pressure)
        self.assertIsNotNone(data.atmosphere.rising)
        self.assertIsNotNone(data.atmosphere.visibility)
        self.assertIsNotNone(data.condition.code)
        self.assertIsNotNone(data.condition.date)
        self.assertIsNotNone(data.condition.temp)
        self.assertIsNotNone(data.condition.text)
        self.assertIsNotNone(data.forecast)
        self.assertIsNotNone(data.image)
        self.assertIsNotNone(data.language)
        self.assertIsNotNone(data.last_build_date)
        self.assertIsNotNone(data.latitude)
        self.assertIsNotNone(data.location)
        self.assertIsNotNone(data.longitude)
        self.assertIsNotNone(data.title)
        self.assertIsNotNone(data.units.speed)
        self.assertIsNotNone(data.units.distance)
        self.assertIsNotNone(data.units.pressure)
        self.assertIsNotNone(data.wind)
        self.assertIsNotNone(data.wind.chill)
        self.assertIsNotNone(data.wind.direction)
        self.assertIsNotNone(data.wind.speed)

    def test_search(self):
        w = Weather(Unit.CELSIUS, log=True)
        data = w.lookup_by_location('Dublin')
        self.assertIsNotNone(data.print_obj)
        self.assertTrue('Dublin' in data.description)
        self.assertEquals(data.location.country, "Ireland")
        self.assertEquals(data.location.city, "Dublin")
        self.assertEquals(data.location.region.strip(), "DUB")

    def test_forecast(self):
        w = Weather(Unit.CELSIUS)
        location = w.lookup_by_location('Dublin')
        self.assertIsNotNone(location.print_obj)
        forecasts = location.forecast
        self.assertTrue(len(forecasts) > 0)
        first = forecasts[0]
        self.assertIsNotNone(first.text)
        self.assertIsNotNone(first.high)
        self.assertIsNotNone(first.low)
        self.assertIsNotNone(first.date)

    def test_condition(self):
        w = Weather(Unit.CELSIUS)
        location = w.lookup_by_location('Dublin')
        self.assertIsNotNone(location.print_obj)
        condition = location.condition
        self.assertIsNotNone(condition.text)
        self.assertIsNotNone(condition.temp)
        self.assertIsNotNone(condition.code)
        self.assertIsNotNone(condition.date)

    def test_invalid_lookup_value(self):
        w = Weather(Unit.CELSIUS)
        data = w.lookup(woeid=1)
        try:
            print(data.location)
        except AttributeError:
            self.assertTrue(True)
        except Exception as e:
            self.fail("Unexpected exception raised: " + e.message)

    def test_bad_request(self):
        w = Weather(Unit.CELSIUS)
        try:
            w.lookup(woeid="")
        except HTTPError:
            self.assertTrue(True)
        except Exception as e:
            self.fail("Unexpected exception raised: " + e.message)

    def test_lookup_via_latlng(self):
        w = Weather(Unit.CELSIUS)
        data = w.lookup_by_latlng(53.3494, -6.2601)
        self.assertTrue('Dublin' in data.description)

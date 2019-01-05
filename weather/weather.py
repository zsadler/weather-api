from yahoo_oauth import OAuth2
import logging
from .objects.weather_obj import WeatherObject
from .unit import Unit


class Weather(object):
    URL = 'http://query.yahooapis.com/v1/public/yql'
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    def __init__(self, client_id, client_secret, unit=Unit.CELSIUS, log=False):
        self.unit = unit
        self.log = log
        self.client_id = client_id
        self.client_secret = client_secret

    def lookup(self, woeid):
        url = "%s?q=select * from weather.forecast where woeid = '%s' and u='%s' &format=json" % (
            self.URL, woeid, self.unit)
        return self._call(url)

    def lookup_by_location(self, location):
        url = "%s?q=select* from weather.forecast " \
              "where woeid in (select woeid from geo.places(1) where text='%s') and u='%s' &format=json" % (
                  self.URL, location, self.unit)
        return self._call(url)

    def lookup_by_latlng(self, lat, lng):
        url = "%s?q=select* from weather.forecast " \
              "where woeid in (select woeid from geo.places(1) where text='(%s,%s)') and u='%s' &format=json" % (
                  self.URL, lat, lng, self.unit)
        return self._call(url)

    def _call(self, url):
        oauth = OAuth2(self.client_id, self.client_secret)
        if not oauth.token_is_valid():
            oauth.refresh_access_token()
        req = oauth.session.get(url)
        if self.log:
            self.logger.info("Request URL: %s" % req.url)
            self.logger.info("Status Code: %s" % req.status_code)
            self.logger.info("JSON Response: %s" % req.content)
        if not req.ok:
            req.raise_for_status()
        results = req.json()
        if self.log:
            self.logger.info(results)
        if int(results['query']['count']) > 0:
            wo = WeatherObject(results['query']['results']['channel'])
            return wo
        else:
            if self.log:
                self.logger.warn("No results found: %s " % results)
            return

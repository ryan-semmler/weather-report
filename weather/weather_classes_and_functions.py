import requests
import requests_mock
from datetime import time


def zip_string():
    return input('zip: ')


response = (requests.get("http://api.wunderground.com/api/08d877d9795fb7cb/forecast10day/alerts/astronomy/conditions/currenthurricane/q/" + zip_string() + ".json")).json()



class ForecastDay():

    def __init__(self, day, response):
        self.high = int(response['forecast']['simpleforecast']['forecastday'][day]['high']['fahrenheit'])
        self.low = int(response['forecast']['simpleforecast']['forecastday'][day]['low']['fahrenheit'])
        self.year = int(response['forecast']['simpleforecast']['forecastday'][day]['date']['year'])
        self.month = (response['forecast']['simpleforecast']['forecastday'][day]['date']['monthname'])
        self.day = (response['forecast']['simpleforecast']['forecastday'][day]['date']['day'])
        self.weekday = (response['forecast']['simpleforecast']['forecastday'][day]['date']['weekday'])
        self.conditions = (response['forecast']['simpleforecast']['forecastday'][day]['conditions']).lower()

    def __str__(self):
        return "{} {} -- High: {}, Low: {}. Conditions: {}".format(self.month, self.day, self.high, self.low, self.conditions)

    def __repr__(self):
        return "On {}, {} {}, {}, the temperature will range from {}-{}°F, and the weather will be {}.".format(self.weekday, self.month, self.day, self.year, self.low, self.high, self.conditions)


class Forecast10Day():

    def __init__(self, ForecastDay, response):
        self.forecast = []

    def populate(self, ForecastDay, response):
        for i in range(10):
            self.forecast.append(ForecastDay(i, response))

    def __str__(self):
        return str(self.forecast)


class CurrentConditions():

    def __init__(self, response):
        self.weather = response['current_observation']['weather']
        self.temp = response['current_observation']['temp_f']
        self.wind_mph = response['current_observation']['wind_mph']
        self.wind_dir = response['current_observation']['wind_dir']

    def __repr__(self):
        return "The current temperature is {}°F and the weather is {} with {}mph winds coming from the {}".format(self.temp, self.weather, self.wind_mph, self.wind_dir)


class SunriseSunset():

    def __init__(self, response):
        self.sunrise = str(response['moon_phase']['sunrise']['hour']) + ":" + str(response['moon_phase']['sunrise']['minute'])
        self.sunset = str(response['moon_phase']['sunset']['hour']) + ":" + str(response['moon_phase']['sunset']['minute'])

    def __repr__(self):
        return "The sun will rise at {} and set at {}".format(self.sunrise, self.sunset)


class Alert():

    def __init__(self, response):
        self.alert = response['alerts']

    def __repr__(self):
        if self.alert:
            return self.alert
        return "No alerts"


class Hurricane():

    def __init__(self, response, storm_number):
        self.name = response['currenthurricane'][storm_number]['stormInfo']['stormName']
        self.category = response['currenthurricane'][storm_number]['Current']['SaffirSimpsonCategory']
        self.latitude = response['currenthurricane'][storm_number]['Current']['lat']
        self.longitude = response['currenthurricane'][storm_number]['Current']['lon']

    def __repr__(self):
        return "Name: {}  Category: {}  Latitude: {}  Longitude: {}".format(self.name, self.category, self.latitude, self.longitude)


def print_10_day_forecast(ForecastDay, Forecast10Day, response):
    f = Forecast10Day(ForecastDay, response)
    f.populate(ForecastDay, response)
    for day in f.forecast:
        print(day)


def print_current_conditions(CurrentConditions, response):
    print(CurrentConditions(response))


def print_sunrise_sunset(SunriseSunset, response):
    print(SunriseSunset(response))


def print_alert(Alert, response):
    print(Alert(response))


def print_hurricanes(Hurricane, response):
    for i in range(len(response['currenthurricane'])):
        print(Hurricane(response, i))

#! python3
# quickWeather.py - Prints the weather location from the command line.

import json, requests, sys, textMyself, time, datetime

location = 'Reading,UK'

# Download the JSON data from OpenWeatherMap.org's API.
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=4aa494341a32c017b137e7e2800f31a8' % (location)

textAlreadySent = False
while True:
    dt = datetime.datetime.now()
    if dt.hour == 19:

        if not textAlreadySent:
            response = requests.get(url)
            response.raise_for_status()

            # Load JSON data into a Python variable.
            weatherData = json.loads(response.text)

            w = weatherData['list']

            if 'Rain' == w[0]['weather'][0]['main']:
                textMyself.textmyself('Don\'t forget your umbrella')
                textAlreadySent = True
    else:
        textAlreadySent = False
    time.sleep(60)
    

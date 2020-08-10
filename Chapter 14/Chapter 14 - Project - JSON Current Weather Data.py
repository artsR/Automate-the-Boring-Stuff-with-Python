#! python3
#  quickWeatherINFO.py - Downloads the weather forecast for the next few days 
#                      using OpenWeatherMap.org and prints it as plaintext.

import sys, requests, json

if len(sys.argv) < 2:
    print('Usage: you missed location...')
    location = input()
else:
    location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url) # Returns a 'Response' Object. 
response.raise_for_status() # if no exception is raise, the download text
#                           will be in 'response.text'.

# Convert JSON data obtained from website to Python format:
weatherData = json.loads(response.text)

# Print weather descriptions:
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])





## historical data for Varna, Bulgaria

# What more I can do:

## Collect weather forecasts for several campsites or hiking trails to see
    #which one will have the best weather.
## Schedule a program to regularly check the weather and send me a frost alert.
## Pull weather data from multiple sites to show all at once, or calculate and
    #show the average of the multiple weather predictions.

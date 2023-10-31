import requests
import json


response_API = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m')

data = response_API.text
parse_json = json.loads(data)

print(parse_json)
import requests
import json
from Models.models import *
from secrets import *

def getCoordinatesFromAPI():
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key={google_maps_api_key}')
    resp_json_payload = response.json()
    location = resp_json_payload['results'][0]['geometry']['location']
    coords = Coordinates(latitude=321, longtitude=123)
    return coords
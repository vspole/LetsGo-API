import json

def getValueWithKey(key: str):
    with open('Keys/Secrets.json') as json_file:
        data = json.load(json_file)
        return data[key]

def getClientAPIKey():
    return getValueWithKey("client_api_key")

def getMapsAPIKey():
    return getValueWithKey("google_maps_api_key")

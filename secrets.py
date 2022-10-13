import json

def getValueWithKey(key: str):
    with open('Keys/Secrets.json') as json_file:
        data = json.load(json_file)
        return data[key]

def getAPIKey():
    return getValueWithKey("apiKey")

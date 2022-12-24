from Models.models import *
from secrets import *
from typing import List
import requests


googleMapsKey = getMapsAPIKey()

def reccursiveReastaurant(location: Location, searchType: SearchType, searchTerm: SearchTerm, places = [], nextPageToken = None, count = 0) -> List[Place]:
    # Set the search radius to 10 miles
    radius = 32093.4

    # Build the API request URL
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location.latitude},{location.longitude}&radius={radius}"

    # Add the search term to the request URL if it is provided
    # Add the search type to the request URL if the search term is not provided
    if searchTerm != None:
        url += f"&keyword={searchTerm.term}"
    else:
        url += f"&type={searchType.type}"

    url += f"&key={googleMapsKey}"

    # Make the API request
    response = requests.get(url)

    # Parse the response to get a list of nearby places
    if response.status_code == 200:
        data = response.json()
        for result in data["results"]:
            photoReference = result["photos"][0]["photo_reference"] if "photos" in result else None
            place = Place(name = result["name"], rating = result["rating"], address = result["vicinity"], photoReference = photoReference)
            places.append(place)

    if "next_page_token" in data and count < 5:
        count += 1
        return reccursiveReastaurant(location, searchType, searchTerm, places,data["next_page_token"], count)
    else:
        return places

def fetchImageFromGoogle(photoReference: str):
    base_url = "https://maps.googleapis.com/maps/api/place/photo"
    params = {
        "photoreference": photoReference,
        "key": googleMapsKey,
        "maxwidth": 400
    }
    response = requests.get(base_url, params=params)
    return response

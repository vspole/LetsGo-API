from Models.models import *
from secrets import *
from typing import List
import requests, time, string

googleMapsKey = getMapsAPIKey()

def reccursiveFetchPlaces(location: Location, searchType: SearchType, searchTerm: SearchTerm, places = [], nextPageToken = None, count = 0) -> List[Place]:
    # Set the search radius to 10 miles
    radius = 32093.4

    # Build the API request URL
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?"

    # If nextPageToken has a value only include nextPageToken and Key in request
    if nextPageToken != None:
        url += f"&pagetoken={nextPageToken}"
    else:
        url += f"location={location.latitude},{location.longitude}&radius={radius}"

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
            if "photos" in result and "rating" in result:
                photoReference = result["photos"][0]["photo_reference"]
                type = string.capwords(result["types"][0].replace("_", " "))
                place = Place(name = result["name"], rating = result["rating"], address = result["vicinity"], photoReference = photoReference, numberOfRatings = result["user_ratings_total"], placeID = result["place_id"], category = type)
                places.append(place)

    if "next_page_token" in data and count < 5:
        count += 1
        time.sleep(2)
        return reccursiveFetchPlaces(location, searchType, searchTerm, places,data["next_page_token"], count)
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

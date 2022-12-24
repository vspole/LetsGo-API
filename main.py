from fastapi import FastAPI, Header, HTTPException, status
from starlette.responses import Response
from Models.models import *
from Firebase.firebase import *
from secrets import *
from GoogleMaps.maps import *
import json

app = FastAPI()
apiKey = getClientAPIKey()

@app.get("/")
async def root():
    return {"message": "Welcome to the API of Let's Go! Explore!"}

@app.get("/checkMinVersion", response_model = APIConfig)
async def checkMinVersion():
    currentConfig = APIConfig(minSupportedVersion = "1.4.0")
    return currentConfig

@app.post("/createUser", response_model = User )
async def createUser(user: User, userToken: str = Header(...), clientKey: str =  Header(...)):
    verifyAccess(userToken, clientKey)
    newUser = addUserToGroupFirebase(user)
    return newUser

@app.post("/fetchNearbyPlaces", response_model = NearbyPlacesReturnModel)
async def fetchNearbyPlaces(location: Location, searchType: SearchType = None, searchTerm: SearchTerm = None, userToken: str = Header(...), clientKey: str =  Header(...)):
    verifyAccess(userToken, clientKey)
    places = reccursiveReastaurant(location, searchType, searchTerm, [])
    return NearbyPlacesReturnModel(places = places, count = len(places))

@app.post("/fetchImage")
async def fetchImage(photoReference: str, userToken: str, clientKey: str):
    verifyAccess(userToken, clientKey)
    response = fetchImageFromGoogle(photoReference)
    return Response(response.content, media_type=response.headers['Content-Type'])

def verifyAccess(userToken: str, clientKey: str):
    if verifyIDToken(userToken) == False:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate User ID Token")
    if clientKey != apiKey:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate API Client Key")

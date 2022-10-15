from fastapi import FastAPI, Header, HTTPException, status
from Models.models import *
from Firebase.firebase import *
from secrets import *
import json



app = FastAPI()
apiKey = getClientAPIKey()

@app.get("/")
async def root():
    return {"message": "Welcome to the API of Let's Go! Explore!"}

@app.post("/createUser", response_model = User )
async def createUser(user: User, userToken: str = Header(...), clientKey: str =  Header(...)):
    verifyAccess(userToken, clientKey)
    newUser = addUserToGroupFirebase(user)
    return newUser


def verifyAccess(userToken: str, clientKey: str):
    if verifyIDToken(userToken) == False:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate User ID Token")
    if clientKey != apiKey:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate API Client Key")

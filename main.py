from fastapi import FastAPI
from Models.models import *
from Firebase.firebase import *

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the API of Let's Go! Explore!"}

@app.post("/createUser", response_model = User )
async def createUser(user: User):
    newUser = addUserToGroupFirebase(user)
    return newUser

from fastapi import FastAPI
from Models.models import *
from Firebase.firebase import *

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/createUser", response_model = User )
async def createUser(user: User):
    newUser = addUserToGroupFirebase(user)
    return newUser

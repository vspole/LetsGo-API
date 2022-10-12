import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from Models.models import *


cred = credentials.Certificate('Keys/FirebaseKey.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

def addUserToGroupFirebase(user: User):
    data = {
        "userID": user.userID,
        "PhoneNumber": user.phoneNumber,
        }
    db.collection("Users").document(str(user.userID)).set(data)
    return user

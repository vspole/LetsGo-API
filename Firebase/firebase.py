import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from Models.models import *


cred = credentials.Certificate('Keys/letsgo-69e94-06d6c9bc1328.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

def addUserToGroupFirebase(user: User):
    data = {
        "userID": user.userID,
        "PhoneNumber": user.phoneNumber,
        }
    db.collection("Users").document(str(user.userID)).set(data)
    return user

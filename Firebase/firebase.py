import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore, auth
from Models.models import *

cred = credentials.Certificate('Keys/FirebaseKey.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

def verifyIDToken(token: str):
    try:
        decoded_token = auth.verify_id_token(token)
    except:
        return False
    else:
        return True

def addUserToGroupFirebase(user: User):
    data = {
        "userID": user.userID,
        "PhoneNumber": user.phoneNumber,
        }
    db.collection("Users").document(str(user.userID)).set(data)
    return user

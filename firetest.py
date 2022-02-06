from firebase_admin import credentials, initialize_app, storage
import os

cred = credentials.Certificate("hacksc2022-4d22b-firebase-adminsdk-pymt0-852e6c81ac.json")
initialize_app(cred, {'storageBucket': 'hacksc2022-4d22b.appspot.com'})
fileName = 'latest.jpg'


uploadImage = True

#To be defined

if (uploadImage):
    os.system("raspistill -o latest.jpg")
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    blob.make_public()
    


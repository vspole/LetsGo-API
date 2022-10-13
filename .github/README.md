# lets-go-api

### About
Hello! This repo houses the API that powers the Let's Go! Explore! App. This API is designed using FastAPI and python to provide the lightest and fastest api to power our App.
This API integrates with Firebase to handle User Authentication as well as using Firestore for the database. 
Integration with Google Map Places Search API is coming soon. 

This API has a dual purpose. First of course is to power our app. The second is to showcase our skills while learning more. 

### Set Up
This API requires a Firebase Service Key JSON to access the Firebase project. Obviously, this JSON key is not added to the repo for anyone to access. If you would like to clone and use this template you will need to add your own `FirebaseKey.json`. Refer to `FirebaseKey.json.sample` for how this file should look. Once you have added the JSON key file you are read to run this locally.

1. First ensure you have Python3 installed by checking its version. In terminal run `python3 -V`. Install if needed. 

2. Next download the requirments for this project. Open terminal and CD into the path for the cloned repo and run `pip3 install -r requirements.txt`
3. Run the following command to start the local server `uvicorn main:app --reload`. If thius fails and tells you Uvicorn is not a recognized command use the following command instead `python3 -m uvicorn main:app --reload`.

4. That's it! Go to the url the last command printed to view the server root. Or go to `{url}/docs` to view the Swagger documentation.

### Deployment 
This repo is set up with CI/CD. After a merge into main the workflow will start up and test the code, add the FirebaseKey.json using Github Secrets, dockerise the api, and then deploy the server using Google's Cloud Run service. 

### Links 
+ [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/)
+ [Firebase Service Key Creation](https://firebase.google.com/docs/admin/setup#:~:text=To%20authenticate%20a%20service%20account,confirm%20by%20clicking%20Generate%20Key.)
+ [CI/CD Deployment using Google Cloud Run](https://cloud.google.com/community/tutorials/cicd-cloud-run-github-actions)

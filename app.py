#Create a New Python File and Import the Flask Dependency // will enable your code to access all that Flask has to offer.
from flask import Flask
#Create a New Flask App Instance // ready to create a new Flask app instance. "Instance" is a general term in programming to 
# refer to a singular version of something. Add the following to your code to create a new Flask instance called app:
app = Flask(__name__)
#Create Flask Routes // define the starting point, also known as the root.
@app.route('/')
def hello_world():
    return 'Hello World!'
#Run a Flask App // To run the app, we need to use the command line to navigate to the folder where we've saved our code.
# You should save this code in the same folder you've used in the rest of this module.
#For our FLASK_APP environment variable, we want to modify the path that will run our app.py file so that we can run our file.
#export FLASK_APP=app.py
# Python Library Imports

#Flask App
from flask import Flask, request
# JSON Parsing
import json
# MondoDB 
import pymongo
# Mongo Object  
from bson import json_util

# Creating Flask App object
app = Flask(__name__,
           static_url_path='',
           static_folder='static')

# Each method in the Flask app is tied to a url, which is wriiten using '@app.route()'
@app.route('/')
def root():
    # Default an HTML page
    return app.send_static_file('index.html')

# Regular GET method (doesn't receive information, sends back information)
@app.route('/view')
def viewItems():
    # TO-DO #1
    pass

# POST method (receives information, sends back information)
@app.route('/add', methods=['POST'])
def addItems():
    # TO-DO #2
    pass

# Runs Flask App
if __name__ == "__main__":
    app.run()
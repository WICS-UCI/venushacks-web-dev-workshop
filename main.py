# Python Library Import
#Flask App
from flask import Flask, request
# JSON Parsing
import json
# ENV Import
import os

# Creating Flask App object
app = Flask(__name__,
           static_url_path='',
           static_folder='static')\

issue_tracker = []

# Each method in the Flask app is tied to a url, which is wriiten using '@app.route()'
@app.route('/')
def root():
    # Default an HTML page
    return app.send_static_file('index.html')

# Regular GET method (doesn't receive information, sends back information)
@app.route('/view')
def viewItems():
    return json.dumps(issue_tracker)
    # mongourl = os.getenv('MONGOURL')
    # client = pymongo.MongoClient(mongourl)
    # db = client["Netflix"]
    # col = db['Logs']
    # log = list(col.find())
    # return json_util.dumps(log)

# POST method (receives information, sends back information)
@app.route('/add', methods=['POST'])
def addItems():
    item = {'item': request.form['item'], 'amount': request.form['amount'], 'category': request.form['category']}
    issue_tracker.append(item)
    return app.send_static_file('view.html')

# Runs Flask App
if __name__ == "__main__":
    app.run()
# Python Library Import
#Flask App
from flask import Flask, request, render_template
# JSON Parsing
import json
# ENV Import
import os

# Creating Flask App object
app = Flask(__name__, template_folder="templates")

issue_tracker = []
category = 'all'

# Each method in the Flask app is tied to a url, which is wriiten using '@app.route()'
@app.route('/')
def root():
    # Default an HTML page
    return render_template('index.html')

@app.route('/viewcat', methods=['POST'])
def changeCategory():
    global category
    category = request.form['cat']
    return render_template('view.html', ct=category)

# Regular GET method (doesn't receive information, sends back information)
@app.route('/view')
def viewItems():
    # print(request.form['cat'])
    if category == 'all':
        return json.dumps(issue_tracker)
    else:
        return json.dumps([i for i in issue_tracker if i['category'] == category])

# POST method (receives information, sends back information)
@app.route('/add', methods=['POST'])
def addItems():
    item = {'item': request.form['item'], 'amount': request.form['amount'], 'category': request.form['category']}
    issue_tracker.append(item)
    return render_template('view.html')

# Runs Flask App
if __name__ == "__main__":
    app.run()
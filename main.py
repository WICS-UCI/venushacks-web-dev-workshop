from flask import Flask, request
import json
import time
import pymongo
from bson import json_util

app = Flask(__name__,
           static_url_path='',
           static_folder='static')

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/view')
def viewItems():
    client = pymongo.MongoClient("mongodb+srv://gayatrs:Bridge1!@cluster0.u03w3.mongodb.net/Netflix?retryWrites=true&w=majority")
    db = client["Netflix"]
    col = db['Logs']
    log = list(col.find())
    return json_util.dumps(log)

@app.route('/add', methods=['POST'])
def addItems():
    client = pymongo.MongoClient("mongodb+srv://gayatrs:Bridge1!@cluster0.u03w3.mongodb.net/Netflix?retryWrites=true&w=majority")
    db = client["Netflix"]
    col = db['Logs']
    col.insert_one({'name': request.form['name'], 'time': request.form['time'], 'genre': request.form['genre']})
    return app.send_static_file('view.html')

# app.run(host="127.0.0.1")
if __name__ == "__main__":
    app.run()
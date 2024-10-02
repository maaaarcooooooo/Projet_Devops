from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.devOps_bdd
collection = db.sons

@app.route('/')
def index():
    sons = collection.find()
    return render_template('index.html', sons=sons)

if __name__ == '__main__':
    app.run(debug=True)

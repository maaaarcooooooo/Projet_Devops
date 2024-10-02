# app.py
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('Spotify_Song_Attributes.csv')

@app.route('/')
def home():
    # Convert DataFrame to HTML
    table = df.to_html(classes='table table-striped')
    return render_template('index.html', table=table)

if __name__ == '__main__':
    app.run(debug=False)

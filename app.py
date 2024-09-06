#import packages
from flask import Flask, render_template, request, jsonify
import folium
from IPython.display import HTML, display
import json
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from collections import Counter
import io
import smtplib
from email.mime.text import MIMEText
from waitress import serve
import requests

#from your_database_module import search_function

#name app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'greenstreets'

#setup JSONBin.io 
JSONBIN_ACCESS_KEY = '$2a$10$J23yWei2a5JsxL9JkiWOXuZsgZ.qR/GRj74Jre.4i/Te3XjaT0A2y'
JSONBIN_API_URL = f'https://api.jsonbin.io/v3/b/66db2f75ad19ca34f8a0f264'

#tell flask to read home page
@app.route('/')
def index(): 
    return render_template('apphome.html')

#tell flask to read about page
#@app.route('/about')
#def about(): 
    #return render_template('about.html')

#tell flask to read contact page
#@app.route('/contact')
#def conact(): 
    #return render_template('contact.html')

#tell flask to read defs page
@app.route('/defs')
def defs(): 
    return render_template('defs.html')

#tell flask to read dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


#tell flask how to add event to JSONBin
@app.route('/add-feature', methods=['POST'])
def add_feature():
    new_feature = request.json  # Get the new feature from the request body
    
    # Fetch the current data from JSONBin
    headers = {
        'X-Master-Key': JSONBIN_ACCESS_KEY,
    }
    response = requests.get(JSONBIN_API_URL, headers=headers)

    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch data from JSONBin.io'}), response.status_code

    # Add the new feature to the existing data
    data = response.json()['record']
    data['features'].append(new_feature)

    # Update the JSONBin with the new data
    update_response = requests.put(JSONBIN_API_URL, headers=headers, json=data)

    if update_response.status_code == 200:
        return jsonify(update_response.json()), 200
    else:
        return jsonify({'error': 'Failed to update data in JSONBin.io'}), update_response.status_code
#Tell Flask how to read bin
@app.route('/get-map-data',  methods=['GET'])
def get_map_data():
    headers = {
        'X-Master-Key': JSONBIN_ACCESS_KEY,
    }
    response = requests.get(JSONBIN_API_URL, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # Extract the actual GeoJSON data from the "record" key
        if 'record' in data:
            geojson_data = data['record']
            return jsonify(geojson_data), 200
        else:
            return jsonify({'error': 'Unexpected data format from JSONBin'}), 500
    else:
        return jsonify({'error': 'Failed to fetch data from JSONBin.io'}), response.status_code


#tell flask run app
if __name__ == '__main__':
    serve(app, host="127.0.0.1", port=8080)
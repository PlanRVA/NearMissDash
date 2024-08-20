from flask import Flask, render_template, request, jsonify, Response
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

#from your_database_module import search_function

#name app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'greenstreets'

#tell flask to read home page
@app.route('/')
def index(): 
    return render_template('apphome.html')

#tell flask to read about page
@app.route('/about')
def about(): 
    return render_template('about.html')

#tell flask to read contact page
@app.route('/contact')
def conact(): 
    return render_template('contact.html')

#tell flask to read contact page
@app.route('/defs')
def defs(): 
    return render_template('defs.html')

#tell flask to read dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


#tell flask how to open events geojson
@app.route('/geojson')
def geojson():
    with open('json/events.geojson') as f:
        geojson_data = json.load(f)
    return jsonify(geojson_data)

#tell flask to submit and save form to geojson
@app.route('/add_event', methods=['POST'])
def add_event():
    new_event = request.json
    # Load existing GeoJSON data
    with open('json/events.geojson') as f:
        geojson_data = json.load(f)
    # Add the new event to the features list
    geojson_data['features'].append(new_event)
    # Save the updated GeoJSON data
    with open('json/events.geojson', 'w') as f:
        json.dump(geojson_data, f, indent=4)
    return jsonify({'status': 'success'}), 200


#tell flask how to submit contact form
def send_email(subject, sender, recipients, text_body):
    msg = MIMEText(text_body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    try:
        with smtplib.SMTP_SSL('smtp.live.com', 465) as server:
            server.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))
            server.sendmail(sender, recipients, msg.as_string())
    except Exception as e:
        print(f"Failed to send email: {e}")
#tell flask to submit form, success message and reroute home
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    subject = "New Form Submission"
    sender = os.getenv('EMAIL_USER')
    recipients = ["egreenwell@planrva.org"]
    text_body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    send_email(subject, sender, recipients, text_body)
    # Return JSON response
    return jsonify({"message": "Thank you for your request."})


#tell flask run app
if __name__ == '__main__':
    serve(app, host="127.0.0.1", port=8080)
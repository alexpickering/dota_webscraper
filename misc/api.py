#!/usr/bin/env python3
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the home page'

@app.route('/heroes')
def display_hero_data():
    with open('heroes.csv', 'r') as f:
        csv_data = f.read()
    return render_template('heroes.html', csv_data=csv_data)

@app.route('/csv.html')
def display_csv_as_html():
    return render_template('csv.html')

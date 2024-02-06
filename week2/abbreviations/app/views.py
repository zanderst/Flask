from flask import render_template, request
from . import app
from datetime import datetime
import requests

ABBREVIATIONS_URL = 'https://github.com/ePADD/muse/blob/master/WebContent/WEB-INF/classes/dictionaries/en-abbreviations.txt'

def get_abbreviations():
    response = requests.get(ABBREVIATIONS_URL)
    lines = response.text.splitlines()
    abbreviations = []
    for line in lines:



        if not line.startswith('#') and '\t' in line:
            print(True)
            split_line = line.split('\t')

            if len(split_line) > 1:
                abbreviations.append((split_line[0], split_line[1]))   #makes a tuple of the abbreviation and the meaning
    return abbreviations

@app.route('/')
@app.route('/home')
def home(): #first 10 abbreviations are displayed on the home page
    abbreviations = get_abbreviations()

    return render_template('home.html', abbreviations=abbreviations[:10])



@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/datetime')
def date_time():
    now = datetime.now()
    return render_template('datetime.html', now=now)


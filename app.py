from flask import Flask, render_template, request, redirect
import pandas as pd
import requests
import dill
import math

with open('first_model') as handler:
    model = dill.load(handler)

app = Flask(__name__)

@app.route('/')
def main():
  return render_template('index.html', my_string="")


@app.route('/', methods=['POST'])
def my_form_post():

    city = request.form['city']
    zipcode = request.form['zipcode']
    state = request.form['state']
    bedrooms = request.form['bedrooms']
    bathrooms = request.form['bathrooms']
    floorsize = request.form['floorsize']
    lotsize = request.form['lotsize']
    built_in = request.form['built_in']
    stories = request.form['stories']
    unitcount = request.form['unitcount']
    alltimeviews = 0
    
    if not zipcode: zipcode = '11379'
    if not city: city = 'Brooklyn'
    if not state: state = 'NY'
    if not bedrooms: bedrooms = 3
    if not bathrooms: bathrooms = 2
    if not floorsize: floorsize = 1787.0
    if not lotsize: lotsize = 2500.00
    if not built_in: built_in = 1945.0
    if not alltimeviews: alltimeviews = 2073.7686
    if not stories: stories = 2.00
    if not unitcount: unitcount = 1.0

    d = {
        'zipcode':zipcode,
        'city':city,
        'state':state,
        'beds':int(bedrooms),
        'baths':int(bathrooms),
        'floorsize':int(floorsize),
        'lot':int(lotsize),
        'built_in':int(built_in),
        'alltimeviews':alltimeviews,
        'stories':int(stories),
        'unitcount':int(unitcount)
        }

    output = model.predict(d)
    display_estimate = "Estimate: $" + str(math.ceil(output[0]))
    return render_template('index.html', display_estimate=display_estimate, scroll='estimator')


if __name__ == '__main__':
  app.run(port=33507)

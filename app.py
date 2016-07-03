from flask import Flask, render_template, request, redirect
import pandas as pd
import requests
from bokeh.charts import TimeSeries, show, output_file, vplot
from bokeh.embed import components
from bokeh.resources import CDN

app = Flask(__name__)

@app.route('/')
def main():
  return render_template('index.html')

@app.route('/estimator')
def main():
  return render_template('estimator.html')


@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['ticker']
    url1 = 'https://www.quandl.com/api/v3/datasets/WIKI/'
    url2 = text
    url3 = '/data.json?start_date=2015-05-01&end_date=2015-05-31'

    url = url1 + url2 + url3
    r = requests.get(url)

    data = r.json()
    data2 = data['dataset_data']['data']
    data3 = pd.DataFrame(data2,columns = data['dataset_data']['column_names'])


    data = {}
    data[text] = data3['Adj. Close']
    data['Date'] =data3['Date']

    tsline = TimeSeries(data,
        x='Date', y=[text],
        color=[text], dash=[text],
        title="Timeseries", ylabel='Stock Prices', legend=True)


    script, div = components(tsline,CDN)
    return render_template('graph.html', script=script, div=div)


if __name__ == '__main__':
  app.run(port=33507)

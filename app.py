from flask import Flask, render_template, request, redirect
import pandas as pd
import requests

app = Flask(__name__)

@app.route('/')
def main():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33507)

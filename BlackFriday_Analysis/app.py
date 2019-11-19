import os

import pandas as pd
import numpy as np

from flask import Flask, jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup 
#################################################

app = Flask(__name__)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/model")
def model():
    
    return render_template("Analysis_Processing_Model.html")

@app.route("/dataTable")
def testTable():
    
    return jsonify("testTableFinalCLEAN100.json")

if __name__ == '__main__':
    app.run(debug = True, port = 5021)  #
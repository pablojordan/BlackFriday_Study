import os
import pandas as pd
import numpy as np
from flask import Flask, jsonify, render_template, request, redirect
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor  
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import metrics
from sklearn.model_selection import cross_val_score

#################################################
# Flask Setup 
#################################################

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    
    print("we hit the home function")
    output1 = ""
    output2 = ""
    output3 = ""
    output4 = ""
    output5 = ""
    output6 = ""
    output7 = ""
    output8 = ""
    output9 = ""
    output10 = ""
    output11 = ""

    if request.method == "POST":
        pickle_in = open("treeRegressor.pickle","rb")
        model = pickle.load(pickle_in)
        print("we are now in post")
        print("form", request.form)
        gender = float(request.form["gender"])
        age = float(request.form["age"])
        occupation = float(request.form["occupation"])
        city = float(request.form["city"])
        currentCity = float(request.form["currentCity"])
        marital = float(request.form["marital"])
        prodCat1 = float(request.form["prodCat1"])
        prodCat2 = float(request.form["prodCat2"])
        prodCat3 = float(request.form["prodCat3"])

        # data must be converted to df with matching feature names before predict
        data = pd.DataFrame(np.array([[gender, age, occupation, city, currentCity, marital, prodCat1, prodCat2, prodCat3]]), columns=[gender, age, occupation, city, currentCity, marital, prodCat1, prodCat2, prodCat3])
        print("model options", dir(model)) # Print model variables
        result = model.predict(data)
        if gender == 0:
            response1 = "Female"
        else:
            response1 = "Male"
                
        if age == 0:
            response2 = '0-17'
        elif age == 1:
            response2 = '18-25'
        elif age == 2:
            response2 = '26-35'
        elif age == 3:
            response2 = '36-45'
        elif age == 4:
            response2 = '46-50'
        elif age == 5:
            response2 = '51-55'
        else:
            response2 = '55+'   

        if city == 0:
            response3 = "A"
        elif city == 1:
            response3 = "B"
        else:
            response3 = "C"
       
        if currentCity == 0:
            response4 = "0"
        elif currentCity == 1:
            response4 = "1"
        elif currentCity == 2:
            response4 = "2"
        elif currentCity == 3:
            response4 = "3"
        else:
            response4 = "+4"

        if marital == 0:
            response5 = "Single"
        else: 
            response5 = "Married"

        result = result[0]
        
        output1 = f"The predicted purchase amount is {result:.2f}." 
        output2 = f"The buyer's profile is:"
        output3 = f"Marital Status: {response5}"
        output4 = f"Gender: {response1}"
        output5 = f"Age Range: {response2}"
        output6 = f"Occupation: {occupation}"
        output7 = f"Current City: {response3}"
        output8 = f"Stay in Current City: {response4} years"
        output9 = f"Product Category 1: {prodCat1}"
        output10 = f"Product Category 2: {prodCat2}"
        output11 = f"Product Category 3: {prodCat3}"

    return render_template("index.html", message1 = output1, message2 = output2, message3 = output3, message4 = output4, message5 = output5, message6 = output6, message7 = output7, message8 = output8, message9 = output9, message10 = output10, message11 = output11)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/model")
def model():
    
    return render_template("Analysis_Processing_Model.html")

@app.route("/otherModels")
def otherModels():
    
    return render_template("Other_Model.html")

@app.route("/dataTable")
def testTable():
    
    return render_template("testTableFinalCLEAN100.json")

if __name__ == '__main__':
    app.run(debug = True, port = 5021)  #
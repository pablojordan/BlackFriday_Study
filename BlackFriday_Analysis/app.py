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

@app.route("/predictor", methods=["GET", "POST"])
def predictor():
    # print("we hit the home function")
    output1 = ""
    output2 = ""
    marital3 = ""
    gender4 = ""
    age5 = ""
    occupation6 = ""
    city7 = ""
    current8 = ""
    cat1_9 = ""
    cat2_10 = ""
    cat3_11 = ""

    if request.method == "POST":
        with open('BlackFriday_Analysis/treeRegressor.pickle', 'rb') as fh:
            model = pickle.load(fh)
        # print("model options 2", dir(model))

        # pickle_in = open("treeRegressor.pickle","rb")
        
        # model = pickle.load(pickle_in)
        # print("we are now in post")
        # print("form", request.form)
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
        # print("model options", dir(model)) # Print model variables
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
        
        output1 = f"The predicted purchase amount is {result:.2f}" 
        output2 = f"Buyer's profile:"
        marital3 = f"{response5}"
        gender4 = f"{response1}"
        age5 = f"{response2}"
        occupation6 = f"{occupation}"
        city7 = f"{response3}"
        current8 = f"{response4} years"
        cat1_9 = f"{prodCat1}"
        cat2_10 = f"{prodCat2}"
        cat3_11 = f"{prodCat3}"

    return render_template("predictor.html", message1 = output1, message2 = output2, message3 = marital3, message4 = gender4, message5 = age5, message6 = occupation6, message7 = city7, message8 = current8, message9 = cat1_9, message10 = cat2_10, message11 = cat3_11)



@app.route("/about")
def about():
    
    return render_template("about.html")

@app.route("/dataTable")
def testTable():
    
    return render_template("testTableFinalCLEAN100.json")

if __name__ == '__main__':
    app.run(debug = True, port = 5022)  #
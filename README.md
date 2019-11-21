# Black Friday Study

> Undestand the customer purchase behavior (specifically, purchase amount) against various products of different categories. 

### Can we estimate the consumer purchase amount against various products categories during Black Friday?

![](https://github.com/pablojordan/BlackFriday_Study/blob/master/BlackFriday_Analysis/static/images/Main.png)

## Scope

>* Understand the factors affecting purchase.
>* Perform data analysis of customer demographics (age, gender, marital status, city_type, stay_in_current_city), product category details and total purchase_amount from previous month.
>* There is a strong need to build a model to predict the purchase amount against vaious products which will help them to create personalized offer for customers against different products. 

### Application Website
>* [Black Friday Study](https://blackfridaystudy.herokuapp.com/)

### Dataset source
>* [ Analytics Vidhya - Black Friday Contest](https://datahack.analyticsvidhya.com/contest/black-friday/)

### Data Features
![](https://github.com/pablojordan/BlackFriday_Study/blob/master/BlackFriday_Analysis/static/images/Data.png)

## Getting Started

### Installing

Ensure to have up to date the following modules

```python
pip install flask
pip install glueviz
pip install jinja2
pip install pandas
pip install numpy
```

### Prerequisites

Load the following dependencies into python file. 
```python
import os
import pandas as pd
import numpy as np
from flask import Flask, jsonify, render_template, request, redirect
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.tree import DecisionTreeRegressor  
from sklearn import metrics
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus

```
## Exploratory Data Analysis
> The data analysis was performed using Tableau. Access to Tableau Public with all graphs in the link below.
>* [Data Analysis Tableau](https://public.tableau.com/profile/pablo.jordan#!/)


## Model Results & Evaluation

> Decision tree regression observes features of an object and trains a model in the structure of a tree to predict data in the future to produce meaningful continuous output. Continuous output means that the output/result is not discrete, i.e., it is not represented just by a discrete, known set of numbers or values. Decision tree regressor uses MSE and similar metrics to determine splits.

>* RMSE: 2992.87
>* Coefficient of Determination (a.k.a R2 in LR): 0.6425

![](https://github.com/pablojordan/BlackFriday_Study/blob/master/BlackFriday_Analysis/static/images/regressor.png)

> Decision Tree Regressor output 

![](https://github.com/pablojordan/BlackFriday_Study/blob/master/BlackFriday_Analysis/static/images/regressor_tree.png)

## Files Navigation

>* [BlackFriday Analysis - Main Folder](https://github.com/pablojordan/BlackFriday_Study)
>* [Application File (app.py)](https://github.com/pablojordan/BlackFriday_Study/tree/master/BlackFriday_Analysis)
>* [Main HTML Index](https://github.com/pablojordan/BlackFriday_Study/tree/master/BlackFriday_Analysis/templates)
>* [Static Files (python/css/images)](https://github.com/pablojordan/BlackFriday_Study/tree/master/BlackFriday_Analysis/static)
>* [Data Files](https://github.com/pablojordan/BlackFriday_Study/tree/master/BlackFriday_Analysis/data)


## Authors

* **Pablo Jordan** - [LinkedIn](https://www.linkedin.com/in/pablojordanmba/)

* **Meng Chen** - [LinkedIn](https://www.linkedin.com/in/meng-chen-86405749/)


## Acknowledgments

* Support & Inspiration: [Jeff Anderson](https://www.linkedin.com/in/jeff-h-anderson-solution/) & [Gage Grewal](https://www.linkedin.com/in/gage-grewal/) 


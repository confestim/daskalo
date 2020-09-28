from flask import render_template, Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import numpy as np
import requests

app = Flask(__name__)


@app.route(/, methods=['post','get'])\
def index():

    # add threshold of division by the second polynomial
    x = np.array([1,-3,0,-4,0,1,-1])
    y = np.array([1,1,1])
    if request.method == "POST":
        print(f"Stepen na rezultata {len(x)-len(y)}")
        pedal, pedal2 = np.polydiv(x,y)
        pedalList = list(pedal)
        pedal2List = list(pedal2)

        a = list(map(int, range(len(pedalList))))
        a = a[::-1]
        publicListA = []
        publicListB = []
        
        print("Rezultat:")
        for i in range(len(pedalList)):
            publicListA.append(int(pedalList[i])}x^{a[i])
            print(f"{int(pedalList[i])}x^{a[i]}")
            

        b = list(map(int, range(len(pedal2List)))) 
        b = b[::-1]

        print("Ostatuk")
        for i in range(len(pedal2List)):
            publicListA.append(int(pedal2List[i])}x^{b[i])
            print(f"{int(pedal2List[i])}x^{b[i]}")

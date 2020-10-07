from flask import render_template, Flask, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import numpy as np
import requests

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'




@app.route('/', methods=['post','get'])
def index():
    lastResult = str()
    # add threshold of division by the second polynomial
    if request.method == "POST":
        publicListA = request.form.get('publicA')
        publicListB = request.form.get('publicB')
        x = np.array(list(map(int, publicListA.split(","))))
        y = np.array(list(map(int, publicListB.split(","))))
        print(x,y)
        print(f"Stepen na rezultata {int(len(x)-len(y))}")
        pedal, pedal2 = np.polydiv(x,y)
        print(pedal, pedal2)
        pedalList = list(pedal)
        pedal2List = list(pedal2)
        reformedPedal1 = []
        reformedPedal2 = []
                
        a = list(map(int, range(len(pedalList))))
        a = a[::-1]
  
        print("Rezultat:")
        for i in range(len(pedalList)):
            if "0x" in f"{int(pedalList[i])}x^{a[i]}":
                pass
            elif "1x" in f"{int(pedalList[i])}x^{a[i]}":
                reformedPedal1.append(f"{a[i]}")
    
            else:
                reformedPedal1.append(f"{int(pedalList[i])}x^{a[i]}")
                print(f"{int(pedalList[i])}x^{a[i]}")
            

        b = list(map(int, range(len(pedal2List)))) 
        b = b[::-1]

        print("Ostatuk")
        for i in range(len(pedal2List)):
            if "0x" in f"{int(pedal2List[i])}x^{b[i]}":
                pass
            elif "1x" in f"{int(pedal2List[i])}x^{b[i]}":
                reformedPedal2.append(f"{b[i]}")

            else:
                reformedPedal2.append(f"{int(pedal2List[i])}x^{b[i]}")
                print(f"{int(pedal2List[i])}x^{b[i]}")

        flash(f"Резултат = {reformedPedal1}, Остатък = {reformedPedal2}")

    return render_template('index.html', lastResult=lastResult)


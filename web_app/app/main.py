#!/usr/bin/env python3
import sys
  
from flask import Flask, request, render_template, jsonify, redirect, url_for, request, session

from flask_cors import CORS
from PresentationBackend import cardDemo
from pyscardscript import send_request

# appending the parent directory path

app = Flask(__name__)
cors = CORS(app)
app.secret_key = "dis is a secret key"

@app.route('/')
def home_view():
    return render_template('index.html')

@app.route('/cardpage', methods=['GET', 'POST'])
def cardpage():      
    session.permanent = True
    # data = cardDemo()

    data =   {'atr':     {'atr': '3B 6E 00 00 80 31 80 66 B0 84 0C 01 6E 01 83 00 90 00', 'atrFlag': False, 'atrID': ''}, 'name': 'CARD/S-E VISA DB ONL ACP  ', 'number': '43 18 71 19 91 39 94 79', 'effectiveDate': '28/11/2016', 'expirationDate': '30/11/2019', 'currency': 'Euro', 'country': 'The Republic of Finland', 'log': [
{'amount': '0.01', 'date': '09/09/2021', 'currency': 'Euro'},
{'amount': '0.55', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '0.11', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '5.55', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '0.01', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '0.11', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '0.01', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '0.06', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '1.23', 'date': '19/02/2021', 'currency': 'Euro'}, {'amount': '30.00', 'date': '16/01/2020', 'currency': 'Euro'}]}


    session["data"] = data
    card_logo = ""
#    if data["visa"] == "TRUE":
#        card_logo = "../static/assets/img/visacard.png"
#    else :
#        card_logo = "../static/assets/img/mastercard.png"
    card_logo = "../static/assets/img/visacard.png"
    
    print(data)
        
    return render_template('cardpage.html', data_list = data, card_link = card_logo) 

@app.route('/log')
def log():
    
    data = session["data"]
    return render_template('log.html', data_list = data)


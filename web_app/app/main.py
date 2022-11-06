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

    #data = {'atr': {'atr': '3B 6D 00 00 00 73 C8 00 13 64 54 37 44 33 00 90 00', 'atrFlag': 'possible matched card', 'atrID': {'3B 6D 00 00 00 73 C8 00 13 64 54 37 44 33 00 90 00': ['Deutsche Bank MasterCard Credit Card (Bank)', 'https://www.deutsche-bank.de/pfb/content/pk-konto-und-karte-kreditkarte.html']}}, 'name': ['0x5F20: 54 45 53 54 20 43 41 52 44 2F 45 4D 56 20 42 49 4E 2D 32', 'TEST CARD/EMV BIN-2'], 'number': ['0x57: 22 23 00 00 10 01 26 46', '2223 0000 1001 2646'], 'effectiveDate': ['0x5F25: 15 11 01', '01/11/2015'], 'expirationDate': ['0x5F24: 19 12 31', '31/12/2019'], 'currency': ['0x9F42: 0840', 'ISO currency code: 0840'], 'country': ['0x5F28: 0840', 'ISO country code: 0840'], 'log': [{'amount': '1.23', 'date': '01/11/2022', 'currency': 'Euro'}, {'amount': '1.23', 'date': '01/11/2022', 'currency': 'Euro'}, {'amount': '1.23', 'date': '01/11/2022', 'currency': 'Euro'}, {'amount': '1.23', 'date': '01/11/2022', 'currency': 'Euro'}, {'amount': '0.01', 'date': '27/10/2022', 'currency': 'Euro'}, {'amount': '0.01', 'date': '27/10/2022', 'currency': 'Euro'}, {'amount': '70.00', 'date': '06/10/2022', 'currency': 'Euro'}, {'amount': '32.01', 'date': '06/10/2022', 'currency': 'Euro'}, {'amount': '12.81', 'date': '06/10/2022', 'currency': 'Euro'}, {'amount': '0.06', 'date': '06/10/2022', 'currency': 'Euro'}]}
    data = {}
    if "data" in session:
        print("calc data")
        data = session["data"]
    else:
        print("carDemo")
        session["data"]= cardDemo()

    card_logo = "../static/assets/img/visacard.png"

    return render_template('cardpage.html', data_list = data, card_link = card_logo) 

@app.route('/log')
def log():
    data = session["data"]
    data_clean = {}
    for x in data:
        if x != "atr" and x != "log":
            data_clean[x.upper()]= data[x]
    data_history = data["log"]
    if not data_history:
        data_history["a"] = "empty"

    data_atr = data["atr"]
    return render_template('log.html', data_list = data_clean, data_hist = data_history, data_at = data_atr)

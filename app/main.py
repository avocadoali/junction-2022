#!/usr/bin/env python3
import sys
  
from flask import Flask, request, render_template, jsonify, redirect, url_for, request, session
from flask_cors import CORS
# from PresentationBackend import cardDemo

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
    data = {'atr': {'atr': '3B 6E 00 00 80 31 80 66 B0 84 0C 01 6E 01 83 00 90 00', 'atrFlag': 'possible matched card', 'atrID': {'3B 6E 00 00 80 31 80 66 B0 84 0C 01 6E 01 83 00 90 00': ['Optelio Cards (D72 R4 WR)', 'Nordea (a Skandinavian bank) eID card', 'http://linux.fi/wiki/Nordea_eID', 'Nordea Mastercard card', 'Nordea Visa card', 'RBC Royal Bank Client Card (bank in Canada)', 'Banco Santander TUI/USC R7', 'Gemalto Optelio/Desineo D72 (JavaCard) with WG10 and Maestro (JavaCard) (Bank)', 'Carte Ticket Restaurant with MasterCard', 'Citigold VISA Debit for Citibank, Australia', 'Platinum VISA card for Citibank, Australia', 'VISA Infinite issued by RBC Royal Bank (Canada)', 'http://www.rbc.com/', 'Postepay Evolution - Poste Italiane (mastercard)', '"la Caixa" (Spain) (VISA Electron) debit card (Bank)', 'https://www.lacaixa.es/', 'Italian Webank.it BPM Banca Popolare di Milano Bancomat & Maestro Card (Bank)', 'Sberbank of Russia MIR debit card (Bank)']}}, 'name': ['0x5F20: 43 41 52 44 2F 53 2D 45 20 56 49 53 41 20 44 42 20 4F 4E 4C 20 41 43 50 20 20', 'CARD/S-E VISA DB ONL ACP  '], 'number': ['0x57: 43 18 71 19 91 39 94 79', '4318 7119 9139 9479'], 'effectiveDate': ['0x5F25: 16 11 28', '28/11/2016'], 'expirationDate': ['0x5F24: 19 11 30', '30/11/2019'], 'currency': ['0x9F42: 0978', 'Euro'], 'country': ['0x5F28: 0246', 'The Republic of Finland'], 'log': [{'amount': '0.01', 'date': '09/09/2021', 'currency': 'Euro'}, {'amount': '0.55', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '0.11', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '5.55', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '0.01', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '0.11', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '0.01', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '0.06', 'date': '24/06/2021', 'currency': 'Euro'}, {'amount': '1.23', 'date': '19/02/2021', 'currency': 'Euro'}, {'amount': '30.00', 'date': '16/01/2020', 'currency': 'Euro'}]}
    session["data"]= data
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

#!/usr/bin/env python3
from flask import Flask, request, render_template, jsonify, redirect, url_for, request, session

from flask_cors import CORS
from pyscardscript import send_request

app = Flask(__name__)
cors = CORS(app)
app.secret_key = "dis is a secret key"

@app.route('/')
def home_view():
    return render_template('index.html')

@app.route('/cardpage', methods=['GET', 'POST'])
def cardpage():      
    session.permanent = True
    data = send_request()
    session["data"] = data
    return session["data"]

#!/usr/bin/env python3

from flask import Flask
from flask import request, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():

    d = datetime.datetime.now()
        
    return render_template("index.html", d=d)

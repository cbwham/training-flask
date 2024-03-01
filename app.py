#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/hallo")
def hallo():
    return "hallo"

@app.route("/feierabend")
def fa():
    return "11 uhr 15"

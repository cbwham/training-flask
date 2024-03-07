#!/usr/bin/env python3

from flask import Flask, jsonify
from healthcheck import HealthCheck

app = Flask(__name__)
health = HealthCheck()

# Add a flask route to expose information
app.add_url_rule('/healthcheck', 'healthcheck', view_func=lambda: health.run())

@app.route("/")
def index():
    return '<!doctype html><html lang=en><head><meta charset=utf-8><title>CBW</title></head><body><p>FSH35!</p></body></html>'

if __name__ == "__main__":
    app.run()

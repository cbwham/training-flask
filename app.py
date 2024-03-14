#!/usr/bin/env python3

"""Module providing a basic example on the use of Flask."""

import datetime
from flask import Flask
from healthcheck import HealthCheck

app = Flask(__name__)
health = HealthCheck()

# Add a flask route to expose information
app.add_url_rule('/healthcheck', 'healthcheck', view_func=lambda: health.run()) # pylint: disable=W0108


# "index"
@app.route("/") # noqa: DC002
def index():
    return '<!doctype html><html lang=en><head><meta charset=utf-8><title>CBW</title></head><body><p>FSH35!</p></body></html>'  # string


# dynamic content
@app.route('/name/<name>') # noqa: DC002
def show(name):
    return f'<!doctype html><html lang=en><head><meta charset=utf-8><title>CBW - Azure Wars</title></head><body ><p>Greetings, Master {name}!</p></body></html>'  # string

# happy day?
def is_friday(dt):
    return dt.weekday() == 4  # 0=monday


@app.route("/pause") # noqa: DC002
def pause():
    """
    Returns True if the current time is in the following ranges: 9:30-9:45, 11:15-11:30, 12:15-12:45 on Fridays
    """
    # current time
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    # .. in central europe
    now_cet = now.astimezone(tz=datetime.timezone(datetime.timedelta(hours=1)))
    # DEBUG
    print(repr(now_cet))

    # define condition of classroom pauses
    cond = bool((9 <= now_cet.hour <= 9 and 30 <= now_cet.minute <= 45)
        or (11 <= now_cet.hour <= 11 and 15 <= now_cet.minute <= 30)
        or (12 <= now_cet.hour <= 15 and 12 <= now_cet.minute <= 45
            and is_friday(now_cet)))
    return {"datetime": now_cet, "pause": cond}  # json


if __name__ == "__main__":
    app.run(debug=True)

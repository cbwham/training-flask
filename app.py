#!/usr/bin/env python3

from flask import Flask
from healthcheck import HealthCheck

app = Flask(__name__)
health = HealthCheck()

# Add a flask route to expose information
app.add_url_rule('/healthcheck', 'healthcheck', view_func=lambda: health.run())

@app.route("/pause", methods=["GET"])
def pause():
    """
    Returns True if the current time is in the following ranges: 9:30-9:45, 11:15-11:30
    """
    import datetime
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    now_cet = now.astimezone(tz=datetime.timezone(datetime.timedelta(hours=1)))
    cond = str(
        (
            (9 <= now_cet.hour <= 9 and 30 <= now_cet.minute <= 45)
            or (11 <= now_cet.hour <= 11 and 15 <= now_cet.minute <= 30)
        )
    )
    return {"pause": cond}

@app.route("/")
def index():
    return '<!doctype html><html lang=en><head><meta charset=utf-8><title>CBW</title></head><body><p>FSH35!</p></body></html>'

if __name__ == "__main__":
    app.run()

import psutil
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

"""
APIs for various values to pull for the graphs
"""


@app.route("/api/cpu-load")
def cpu_load_chart():
    cpu_load = psutil.cpu_percent()
    return {'CPU Load': cpu_load}


@app.route("/api/temperature")
def get_api_temperature():
    return {"Temperature": 32}


@app.route("/api/pressure")
def get_api_pressure():
    return {"Pressure": 40}


@app.route("/api/humidity")
def get_api_humidity():
    return {"Humidity": 70}


if __name__ == '__main__':
    app.debug = True
    app.run()

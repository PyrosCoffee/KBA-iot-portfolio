import psutil
from flask import Flask, render_template, jsonify

monitor_app = Flask(__name__)


@monitor_app.route("/")
def index():
    return render_template("/index.html")


@monitor_app.route("/api/cpu-load")
def cpu_load_chart():
    cpu_load = psutil.cpu_percent()
    return {'CPU Load': cpu_load}


@monitor_app.route("/api/environment")
def get_api_environment():
    return {"Temperature": None, "Pressure": None, "Humidity": None}


@monitor_app.route("/api/temperature")
def get_api_temperature():
    return {"Temperature": fixed_temp(1)}


@monitor_app.route("/api/temperature/{qty}")
def fixed_temp(qty=1):
    return {"28 Celsius"}


@monitor_app.route("/api/pressure")
def get_api_pressure():
    return {"Pressure": None}


@monitor_app.route("/api/humidity")
def get_api_humidity():
    return {"Humidity": None}


@monitor_app.route("/api/does-not-exist")
def get_api_does_not_exist():
    return {"ERROR": "Route Not Implemented"}


if __name__ == '__main__':
    monitor_app.run()

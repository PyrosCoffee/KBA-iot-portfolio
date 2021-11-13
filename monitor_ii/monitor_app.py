import psutil
from flask import Flask

monitor_app = Flask(__name__)


@monitor_app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@monitor_app.route("/api/device-load")
def handle_form():
    cpu_load = psutil.cpu_percent()
    return {'CPU Load': cpu_load}


@monitor_app.route("/api/environment")
def get_api_environment():
    return {"Temperature": None, "Pressure": None, "Humidity": None}


@monitor_app.route("/api/temperature")
def get_api_temperature():
    return {"Temperature": None}


@monitor_app.route("/api/pressure")
def get_api_pressure():
    return {"Pressure": None}


@monitor_app.route("/api/humidity")
def get_api_humidity():
    return {"Humidity": None}


if __name__ == '__main__':
    monitor_app.run()

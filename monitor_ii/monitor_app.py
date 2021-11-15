import psutil
from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
from db import Base, db_folder, db_name, EnvironmentTPH

monitor_app = Flask(__name__)


@monitor_app.route("/")
def index():
    return render_template("index.html")
    # intellisense says index not found idk why


@monitor_app.route("/api/cpu-load")
def cpu_load_chart():
    cpu_load = psutil.cpu_percent()
    return {'CPU Load': cpu_load}
    # gets current cpu load


@monitor_app.route("/api/temperature")
def get_api_temperature():
    DBE = create_engine(f"sqlite:///{db_name}")
    Base.metadata.create_all(DBE)
    session = sessionmaker(bind=DBE)()
    environData = session.query(EnvironmentTPH).limit(1)
    for data in environData:
        temp = data.temp
        return {"Temperature": temp}


@monitor_app.route("/api/pressure")
def get_api_pressure():
    DBE = create_engine(f"sqlite:///{db_name}")
    Base.metadata.create_all(DBE)
    session = sessionmaker(bind=DBE)()
    environData = session.query(EnvironmentTPH).limit(1)
    for data in environData:
        pressure = data.pressure
        return {"Pressure": pressure}


@monitor_app.route("/api/humidity")
def get_api_humidity():
    DBE = create_engine(f"sqlite:///{db_name}")
    Base.metadata.create_all(DBE)
    session = sessionmaker(bind=DBE)()
    environData = session.query(EnvironmentTPH).limit(1)
    for data in environData:
        humidity = data.humidity
        return {"Humidity": humidity}


@monitor_app.route("/api/environment")
def get_api_environment():
    DBE = create_engine(f"sqlite:///{db_name}")
    Base.metadata.create_all(DBE)
    session = sessionmaker(bind=DBE)()
    environData = session.query(EnvironmentTPH).limit(1)
    displayData = []
    for data in environData:
        temp = data.temp
        pressure = data.pressure
        humidity = data.humidity
        environment = {"Temperature": temp, "Pressure": pressure, "Humidity": humidity}
        displayData.append(environment)


@monitor_app.route("/api/does-not-exist")
def get_api_does_not_exist():
    return {"ERROR": "Route Not Implemented"}


if __name__ == '__main__':
    monitor_app.run()

import psutil
from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from db import Base, db_folder, db_name, EnvironmentTPH

_db_filename = db_folder + db_name
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
    dbe = create_engine(f"sqlite:///{_db_filename}")
    Base.metadata.create_all(dbe)
    session = sessionmaker(bind=dbe)()
    environData = session.query(EnvironmentTPH).limit(-1)
    for data in environData:
        temperature = data.temperature
    return {"Temperature": temperature}


# api for temperature
@monitor_app.route("/api/temperature/<quantity>")
def get_api_temperature_details(quantity):
    dbe = create_engine(f"sqlite:///{_db_filename}")
    Base.metadata.create_all(dbe)
    session = sessionmaker(bind=dbe)()
    # problem code
    environData = session.query(EnvironmentTPH).limit(quantity)
    _xList = []
    _yList = []
    for data in environData:
        _yList.append(data.temperature)
        _xList.append(data.created_at.strftime("%m-%d-%y %H:%M"))
    # import pdb;pdb.debug_trace()
    return jsonify({'x': _xList, 'y': _yList})


# api for pressure
@monitor_app.route("/api/pressure")
def get_api_pressure():
    dbe = create_engine(f"sqlite:///{_db_filename}")
    Base.metadata.create_all(dbe)
    session = sessionmaker(bind=dbe)()
    environData = session.query(EnvironmentTPH).limit(-1)
    for data in environData:
        pressure = data.pressure
    return {"Pressure": pressure}


# api for humidity
@monitor_app.route("/api/humidity")
def get_api_humidity():
    dbe = create_engine(f"sqlite:///{_db_filename}")
    Base.metadata.create_all(dbe)
    session = sessionmaker(bind=dbe)()
    environData = session.query(EnvironmentTPH).limit(-1)
    for data in environData:
        humidity = data.humidity
    return {"Humidity": humidity}


# api for environment
@monitor_app.route("/api/environment/")
def get_api_environment():
    dbe = create_engine(f"sqlite:///{_db_filename}")
    Base.metadata.create_all(dbe)
    session = sessionmaker(bind=dbe)()
    environData = session.query(EnvironmentTPH).limit(-1)
    displayData = []
    for data in environData:
        temperature = data.temperature
        pressure = data.pressure
        humidity = data.humidity
        environment = {"Temperature": temperature, "Pressure": pressure, "Humidity": humidity}
        displayData.append(environment)
    return environment

# line-chart page
@monitor_app.route("/about/")
def about():
    return render_template("line-chart.html")


# ignore - test
@monitor_app.route("/api/does-not-exist")
def get_api_does_not_exist():
    return {"ERROR": "Route Not Implemented"}


if __name__ == '__main__':
    monitor_app.run()

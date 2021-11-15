"""
modified monitor.py to suit environment needs
"""

import psutil
from time import sleep
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from mypi import get_host_name, get_serial, get_mac
from db import Base, EnvironmentTPH, db_name, db_folder

_db_filename = db_folder + db_name


def save_enviro_data():
    counter = 0
    launch = True

    while launch:
        engine = create_engine(f"sqlite:///{db_name}")
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        environmentData = EnvironmentTPH()
        environmentData.cpu_load = psutil.cpu_percent()
        environmentData.device_name = get_host_name()
        environmentData.device_serial = get_serial()
        environmentData.device_mac = get_mac()
        environmentData.temperature = 26.5
        environmentData.pressure = 986
        environmentData.humidity = 35.7
        environmentData.created_at = datetime.now()
        session.add(environmentData)
        session.commit()

        print("Device Name:", environmentData.device_name, "Serial: ", environmentData.device_serial, "MAC:",
              environmentData.device_mac,)
        sleep(5)
        counter += 1
        if counter < 12:
            launch = True
        else:
            launch = False


if __name__ == "__main__":
    save_enviro_data()

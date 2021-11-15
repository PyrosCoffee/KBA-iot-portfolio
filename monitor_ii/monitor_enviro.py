
"""
modified monitor.py to suit environment needs
"""

import psutil
from time import sleep
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Base, db_name, db_folder
from cpu import CPU
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
        # dont know if i have to leave CPU here? fix later
        cpu_usage = psutil.cpu_percent()


        print("Date:", cpu_date, "Time: ", cpu_time, " CPU Load At:", cpu_usage, "%")
        sleep(5)
        counter += 1
        if counter < 12:
            launch = True
        else:
            launch = False
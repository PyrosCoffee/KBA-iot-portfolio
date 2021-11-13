"""
Monitors cpu load and prints to screen every 5 seconds
"""

import psutil
from time import sleep
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Base, db_name, db_folder
from cpu import CPU
from datetime import datetime

_db_filename = db_folder + db_name


def save_cpu_data():
    counter = 0
    launch = True

    while launch:
        engine = create_engine(f"sqlite:///{db_name}")
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        cpu_save = CPU()

        cpu_usage = psutil.cpu_percent()
        cpu_dt = datetime.now()

        cpu_save.cpu_load = cpu_usage
        cpu_save.created_at = cpu_dt
        session.add(cpu_save)
        session.commit()
        cpu_time = cpu_dt.strftime("%H:%M:%S")
        cpu_date = cpu_dt.date()
        print("Date:", cpu_date, "Time: ", cpu_time, " CPU Load At:", cpu_usage, "%")
        sleep(5)
        counter += 1
        if counter < 12:
            launch = True
        else:
            launch = False


"""
Old code that I might use -- Ignore
def get_cpu_load():
    interval = 0
    launch = True

    while launch:
        print("CPU Load At:", psutil.cpu_percent(), "%")
        sleep(5)
        interval += 1
        if interval < 12:
            loop = True
        else:
            loop = False
"""

if __name__ == "__main__":
    save_cpu_data()

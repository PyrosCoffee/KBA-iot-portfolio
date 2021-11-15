"""
Edited the db.py that was in the base components to suit the needs of the project
"""

import os
from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


# data folder doesnt get things added to it, fix later
db_folder = "./data/"
db_name = "enviromon.db"

if not os.path.isdir(db_folder):
    os.makedirs(db_folder)
    print(f"Created {db_folder} folder")
Base = declarative_base()


# class for storing environment details
class EnvironmentTPH(Base):
    __tablename__ = "tph_storage"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    device_name = Column(String)
    device_mac = Column(String)
    device_serial = Column(String)
    temperature = Column(Float)
    pressure = Column(Float)
    humidity = Column(Float)
    created_at = Column(DateTime)

    def __init__(self):
        self.device_name = "UKNOWN"
        self.device_mac = "ZZ:ZZ:ZZ:ZZ:ZZ:ZZ"
        self.device_serial = "UNKNOWN"
        self.temperature = None
        self.pressure = None
        self.humidity = None
        self.created_at = datetime.now()

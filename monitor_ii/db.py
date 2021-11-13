"""
Edited the db.py that was in the base components to suit the needs of the project
"""

import os
from sqlalchemy import Column, DateTime, Float, func, Integer, null
from sqlalchemy.ext.declarative import declarative_base

db_folder = "./data/"
db_name = "monitoring_cpu.db"

if not os.path.isdir(db_folder):
    os.makedirs(db_folder)
    print(f"Created {db_folder} folder")
Base = declarative_base()

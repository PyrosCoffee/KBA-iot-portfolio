from db import Base
from sqlalchemy import Column, Integer, Float, DateTime, func


# cpu class for storing info
class CPU(Base):
    __tablename__ = 'cpu'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    cpu_load = Column(Float)
    created_at = Column(DateTime, server_default=func.now())

    def __init__(self):
        self.cpu_load = -1

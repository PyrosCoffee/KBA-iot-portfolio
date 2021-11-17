"""
Accesses and displays data stored in monitoring_cpu.db
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Base
from cpu import CPU

db_filename = "monitoring_cpu.db"


# opens db and displays info
def main():
    engine = create_engine(f"sqlite:///{db_filename}")
    active_session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)

    cpu = active_session.query(CPU).limit(10)

    table("Date:", 16, "Time:", 16, "CPU Load:", 16, '-', '+', '|')
# loop collects and prints data stored in item properties
    for item in cpu:
        cpu_time = item.created_at.strftime("%H:%M:%S")
        cpu_date = item.created_at.strftime("%d-%m-%y")
        print(f"| {cpu_date:>15}| {cpu_time:>15}| {item.cpu_load:<14.2f}%|")


# creates table boundaries for the headers/columns
def table(column1, column1_width, column2, column2_width, column3, column3_width, horizontal, cross, vertical):
    print(f"{cross}{horizontal * column1_width}{cross}{horizontal * column2_width}{cross}"
          f"{horizontal * column3_width}{cross}")
    print(f'| {column1:<{column1_width - 1}s}{vertical} {column2:<{column2_width - 1}s}'f''
          f'{vertical} {column3:<{column3_width - 1}s}'f'{vertical}')
    print(f"{cross}{horizontal * column1_width}{cross}{horizontal * column2_width}{cross}"
          f"{horizontal * column3_width}{cross}")


if __name__ == "__main__":
    main()

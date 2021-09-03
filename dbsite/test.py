import os
import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=os.environ.get("HOME")+"/Downloads/instantclient_19_8")

connection = cx_Oracle.connect(
    user="PMADADI",
    password="PM_ORACLE",
    dsn="localhost:1521/ORCL")

print("Successfully connected to Oracle Database")


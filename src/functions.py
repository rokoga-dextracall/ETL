import urllib
import models as md
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import credentials
import extract as e
import transform as t
import load as l

## loading db info
conn_prod = credentials.conn_prod
conn_mirror = credentials.conn_mirror

def database_session(conn_str):

    quoted_conn_str = urllib.parse.quote_plus(conn_str)
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={quoted_conn_str};")
    md.Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    return session

# reports/logging

# 
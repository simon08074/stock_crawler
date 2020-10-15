# -*- coding: utf-8 -*-
"""
Created on Sun May 26 00:34:01 2019

@author: simon
"""

from datetime import date,timedelta
from urllib.request import urlopen
from dateutil import rrule
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import numpy as np
import json
import time
import pymysql
from sqlalchemy import create_engine
from tqdm import tqdm
import query.sqlQuery


def create_sql_cursor(db_conn):
    db = pymysql.connect(
        host=db_conn['host'], port=db_conn['port'], user=db_conn['user'],
        passwd=db_conn['passwd'], db='financial', charset='utf8'
    )
    cursor = db.cursor()
    return cursor


def read_sql_table(db_conn, sql):
    engine = create_engine(
        "mysql+pymysql://{user}:{pw}@localhost/{db}"
        .format(
            user=db_conn['user'],
            pw=db_conn['passwd'],
            db=db_conn['db']
        )
    )
    db_connection = engine.connect()
    table_df = pd.read_sql(sql, db_connection)
    return table_df


def insert_data(db_conn, df, table_name):
    engine = create_engine(
        "mysql+pymysql://{user}:{pw}@localhost/{db}"
        .format(
            user=db_conn['user'],
            pw=db_conn['passwd'],
            db=db_conn['db']
        )
    )
    db_connection = engine.connect()
    try:
        df.to_sql(table_name, db_connection, if_exists='append', index=False)
    except ValueError as vx:
        print(vx)
    except Exception as ex:
        print(ex)
    else:
        print("Table %s created successfully." % table_name)
    finally:
        db_connection.close()


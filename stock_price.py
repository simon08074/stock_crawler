# -*- coding: utf-8 -*-
"""
Created on Sat May 18 00:22:33 2019

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
from tqdm import tqdm


def craw_one_month(stock_number, date):
    url = (
        "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=" + date.strftime('%Y%m%d') +
        "&stockNo=" +
        str(stock_number)
    )
    data = json.loads(urlopen(url).read())
    return pd.DataFrame(data['data'], columns=data['fields'])


def craw_stock(stock_number, start_month):
    b_month = date(*[int(x) for x in start_month.split('-')])
    now = datetime.datetime.now().strftime("%Y-%m-%d")         # 取得現在時間
    e_month = date(*[int(x) for x in now.split('-')])
    
    result = pd.DataFrame()
    for dt in rrule.rrule(rrule.MONTHLY, dtstart=b_month, until=e_month):
        result = pd.concat([result, craw_one_month(stock_number, dt)], ignore_index=True)
        time.sleep(2000.0/1000.0)
    
    return result


df = craw_stock(2330, "2019-05-23")
df.insert(0, 'stock_no', '2330')
df.insert(0, 'id', None)
df.columns = [
    'id', 'stock_no', 'date', 'trade_volume', 'trade_value', 'open', 'high', 'low',\
    'close', 'change', 'transaction'
]

params = {
    "response": "json",
    "date": "20190518",
    "stockNo": "2330"
}


# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:22:23 2019

@author: simon
"""

import os
import requests
from io import StringIO
import pandas as pd
from datetime import datetime, date

# 爬取資料
def crawl_legal_person(date):
    
#    datestr = date.strftime('%Y%m%d')
    datestr = date
    try:
        r = requests.get('http://www.tse.com.tw/fund/T86?response=csv&date='+datestr+'&selectType=ALLBUT0999')
    except:
        return None

    try:
        df = pd.read_csv(StringIO(r.text), header=1).dropna(how='all', axis=1).dropna(how='any')
    except:
        return None
    
    df = df.astype(str).apply(lambda s: s.str.replace(',',''))

    df['證券代號'] = df['證券代號'].str.replace('=', '').str.replace('"', '')


    # 設定index
    df.insert(0, 'date', datestr)
    return df

test = crawl_legal_person("20190523")

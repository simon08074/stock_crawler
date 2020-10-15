# -*- coding: utf-8 -*-
"""
Created on Sun May 26 00:09:46 2019

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
import data_transmit


s_ex_url = 'https://isin.twse.com.tw/isin/C_public.jsp?strMode=2'
otc_url = 'https://isin.twse.com.tw/isin/C_public.jsp?strMode=4'

s_ex_pd = pd.read_html(s_ex_url)[0]

s_ex_pd.columns = [
    'code', 'isin_code', 'list_date', 'market_class', 'industry', 'cficode',
    'remarks'
]
s_ex_pd = s_ex_pd[s_ex_pd['cficode'] == 'ESVUFR']
s_ex_pd = s_ex_pd.drop('remarks', axis=1)
s_ex_pd = s_ex_pd.reset_index(drop=True)
code_name = [i.replace('\u3000', ' ') for i in list(s_ex_pd['code'])]
code_name = [i.split(' ') for i in code_name]
code = [i[0] for i in code_name]
company_name = [i[1] for i in code_name]
s_ex_pd['code'] = code
s_ex_pd.insert(1, 'company_name', company_name)


otc_pd = pd.read_html(otc_url)[0]
otc_pd.columns = [
    'code', 'isin_code', 'list_date', 'market_class', 'industry', 'cficode',
    'remarks'
]
otc_pd = otc_pd[otc_pd['cficode'] == 'ESVUFR']
otc_pd = otc_pd.drop('remarks', axis=1)

def get_stock_info(cf, stock_info_url):
    stock_code_pd = pd.read_html(stock_info_url)[0]
    stock_code_pd.columns = [
        'stock_no', 'isin_code', 'list_date', 'market_class', 'industry', 'cficode',
        'remarks'
    ]
    stock_code_pd = stock_code_pd[stock_code_pd['cficode'] == 'ESVUFR']
    stock_code_pd = stock_code_pd.drop('remarks', axis=1)
    stock_code_pd = stock_code_pd.reset_index(drop=True)
    code_name = [i.replace('\u3000', ' ') for i in list(stock_code_pd['stock_no'])]
    code_name = [i.split(' ') for i in code_name]
    code = [i[0] for i in code_name]
    company_name = [i[1] for i in code_name]
    stock_code_pd['stock_no'] = code
    stock_code_pd.insert(1, 'company_name', company_name)
    stock_code_pd.insert(0, 'id', None)
    data_transmit.insert_data(cf.db_conn, stock_code_pd, 'stock_code')
    return stock_code_pd

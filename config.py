# -*- coding: utf-8 -*-
"""
Created on Sun May 26 00:46:28 2019

@author: simon
"""

db_conn = {
    'host': '127.0.0.1',
    'db': 'financial',
    'port': 3306,
    'user': 'root',
    'passwd': 'freedom0874'
}

crawl_start_date = '2012-01-01'
crawl_end_date = '2019-05-26'

# 上市公司
on_shelf_url = 'https://isin.twse.com.tw/isin/C_public.jsp?strMode=2'
# 上櫃公司
otc_url = 'https://isin.twse.com.tw/isin/C_public.jsp?strMode=4'


# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:25:47 2019

@author: simon
"""

import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

stock_code = '2330'
basic_url = 'https://tw.stock.yahoo.com/d/s/company_{stock_code}.html'.format(stock_code=stock_code)

html = requests.get(basic_url)
soup = BeautifulSoup(html.text, 'html.parser')

capital_value = soup.find_all("td")
type(capital_value[4]) 

tags = soup.find_all('td', attrs = {'class' : 'yui-td-left'})

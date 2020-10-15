# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 21:02:51 2019

@author: simon
"""
import re
import requests
import pandas as pd
from io import StringIO

# 開啟瀏覽器
ses = requests.Session()

# 打開登入網頁
d = ses.get('https://bsr.twse.com.tw/bshtm/bsMenu.aspx')

# 此函式會找特定的value，如「__VIEWSTATE」等
def find_value(name, web):
    reg = 'name="' + name + '".+value="(.*)" />'
    pattern = re.compile(reg)
    result  = pattern.findall(web.text)
    try:
        return result[0]
    except:
        return ""

# 使用方式
viewState = find_value('__VIEWSTATE', d)
eventValidation = find_value('__EVENTVALIDATION', d)
payload = {
    '__EVENTTARGET':'',
    '__EVENTARGUMENT':'',
    '__LASTFOCUS':'',
    '__VIEWSTATE' : viewState,                      #encode_viewstate[:-1],
    '__EVENTVALIDATION' : eventValidation,          #encode_eventvalidation[:-1],
    'RadioButton_Normal' : 'RadioButton_Normal',
    'TextBox_Stkno' : '2330',
    'CaptchaControl1 ' : 'Z67YB',
    'btnOK' : '%E6%9F%A5%E8%A9%A2',
}


url = 'http://www.jb51.net/test/demo.zip'
r = requests.post(url, ) 
with open("2330.csv", "wb") as code:
    code.write(r.content)
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil.relativedelta import relativedelta
import re

def get_date(date, day):
    return str(datetime.date(date - relativedelta(days=day)))
url = 'http://gall.dcinside.com/board/lists?id=f_drama&page='
def crawling(date):
    i = 0
    today = True
    while today:
        i += 1
        html = requests.get(url+str(i)).text
        soup = BeautifulSoup(html, 'html.parser')
        dramaList = soup.find_all('tr',{'class':'ub-content'})
        for drama in dramaList:
            if drama.find('td',{'title':re.compile(get_date(date, 0))}):
                distribute(drama.find('td',{'class':'gall_tit ub-word'}).text.replace('\n',''))
            elif drama.find('td',{'title':re.compile(get_date(date, 1))}):
                today = False
                break
def distribute(text):
    p = re.compile('기묘한[\s|\S]*이야기')
    if p.findall(text):
        print(text)
crawling(datetime.today() - relativedelta(days=1))
# crawling(datetime(2019,2,1))


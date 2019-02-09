# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil.relativedelta import relativedelta
import re


def get_date(date, day):
    return str(datetime.date(date - relativedelta(days=day)))


def crawling(date, url):
    i = 0
    today = True
    dramaList = []
    while today:
        i += 1
        html = requests.get(url + str(i)).text
        soup = BeautifulSoup(html, 'html.parser')
        crawlList = soup.find_all('tr', {'class': 'ub-content'})
        for crawl in crawlList:
            if crawl.find('td', {'title': re.compile(get_date(date, 0))}):
                dramaList.append(crawl.find('td', {'class': 'gall_tit ub-word'}).text.replace('\n', ''))
            elif crawl.find('td', {'title': re.compile(get_date(date, 1))}):
                today = False
                break
    return dramaList
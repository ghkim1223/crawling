from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:/Users/dream/crawling/chromedriver')
url = 'https://www.appannie.com/kr/apps/google-play/top/south-korea/application/communication/'
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
itemLIst = soup.find_all('div', {'class':'item'})
rank = 0
title = ''
company = ''
for item in itemLIst:
    rank = item.find('span', {'class':'number'}).text
    title = item.find('span', {'class':'product-name'}).text
    company = item.find('span', {'class':'publisher-name'}).text
    print(rank + ';' + title + ';' + company)
driver.close()
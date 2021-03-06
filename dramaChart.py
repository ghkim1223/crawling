from datetime import datetime
from dateutil.relativedelta import relativedelta
import crawling
import distribute
import database

url = 'http://gall.dcinside.com/board/lists?id=f_drama&page='
# date = datetime(2019,2,14)
date = datetime.today() - relativedelta(days=1)
dramaList = crawling.crawling(date, url)
# for drama in dramaList:
#     print(drama)
sortList = distribute.distribute(dramaList)
dramaDailyList = []
year, month, day = date.year, date.month, date.day
for sort in sortList.items():
    dramaDailyList.append({'name':sort[0], 'count':len(sort[1]), 'year':year, 'month':month, 'day':day})
# database.insertDramaDaily(dramaDailyList)
print(date)


from datetime import datetime
from dateutil.relativedelta import relativedelta
import crawling
import distribute

url = 'http://gall.dcinside.com/board/lists?id=f_drama&page='
# date = datetime(2019,2,1)
date = datetime.today() - relativedelta(days=1)
print(date)
dramList = crawling.crawling(date, url)
# for drama in dramList:
#     print(drama)
sortList = distribute.distribute(dramList)
for sort in sortList.items():
    print(sort[0], len(sort[1]))

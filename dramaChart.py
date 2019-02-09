import crawling
import distribute
from datetime import datetime
from dateutil.relativedelta import relativedelta

url = 'http://gall.dcinside.com/board/lists?id=f_drama&page='

# crawling(datetime(2019,2,1))

dramList = crawling.crawling(datetime.today() - relativedelta(days=1), url)
# for drama in dramList:
#     print(drama)
sortList = distribute.distribute(dramList)
for sort in sortList.items():
    print(sort[0], len(sort[1]))

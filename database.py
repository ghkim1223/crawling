from pymongo import MongoClient

client = MongoClient('mongodb://admin1:admin1@ds133275.mlab.com:33275/movieproj')
db = client.movieproj
dramaDaily = db.dramaDaily


def insertDramaDaily(dramaDailyList):
    dramaDaily.insert_many(dramaDailyList)


def getDramaCount(name):
    count = 0
    for r in dramaDaily.find({'name':name}):
        count += r['count']
    return name, count


for drama in map(getDramaCount, ['기묘한 이야기', '킹덤', '나르코스', '바이킹스']):
    print(drama)


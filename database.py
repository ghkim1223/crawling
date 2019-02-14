from pymongo import MongoClient

client = MongoClient('mongodb://admin1:admin1@ds133275.mlab.com:33275/movieproj')
db = client.movieproj
dramaDaily = db.dramaDaily
dramaInfo = db.dramaInfo


def insertDramaDaily(dramaDailyList):
    dramaDaily.insert_many(dramaDailyList)


def getDramaCount(name):
    count = 0
    for r in dramaDaily.find({'name':name}):
        count += r['count']
    return name, count


def getDramaInfo():
    return dramaInfo.find()

# dramaName = []
# for dramaInfo in getDramaInfo():
#     dramaName.append(dramaInfo['name'])
# for drama in map(getDramaCount, dramaName):
#     print(drama)


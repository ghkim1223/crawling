from pymongo import MongoClient

client = MongoClient('mongodb://admin1:admin1@ds133275.mlab.com:33275/movieproj')
db = client.movieproj
dramaDaily = db.dramaDaily


def insertDramaDaily(dramaDailyList):
    dramaDaily.insert_many(dramaDailyList)


def selectDramaDaily(year, month, day):
    return dramaDaily.find({'year':year, 'month':month, 'day':day})


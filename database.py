from pymongo import MongoClient

username = 'admin1'
password = 'admin1'
client = MongoClient('mongodb://admin1:admin1@ds133275.mlab.com:33275/movieproj')
db = client.test_database
collection = db.test_collection

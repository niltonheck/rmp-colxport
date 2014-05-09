from pymongo import MongoClient

def stablishCon(database, collection):
  client = MongoClient('localhost', 27017)
  db = client[database]
  collection = db[collection]

  return collection

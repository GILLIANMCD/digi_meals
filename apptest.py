import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "digi_meals"
COLLECTION_NAME = "utensils"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

conn = mongo_connect(MONGODB_URI)

coll = conn[digi_meals][utensils]




documents = coll.find()

for doc in documents:
    print(doc)
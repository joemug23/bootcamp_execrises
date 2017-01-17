import pymongo


class Database(object):

    uri = "mongodb://127.0.0.1:27017"
    DBase = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.uri)
        Database.DBase = client['scrumit']

    @staticmethod
    def insert(collection, data):
        # inserting into the database
        Database.DBase[collection].insert(data)
        return "Data inserted Successfully"

    

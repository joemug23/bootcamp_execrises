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

    @staticmethod
    def delete(collection, data):
        # delete a row of a given data
        results = Database.DBase[collection].find(data)
        if results:
            Database.DBase[collection].remove(data)
            return "Data deleted!"
        else:
            return "No record found"

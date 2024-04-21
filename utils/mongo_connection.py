from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

"""
This class MongoDB is used to access the mongoDB database.
DataBase structure:
users
└─ ip -> username-private_key(encrypted by given auth_key)
message
└─ ip -> encrypted_msg-send_to_username-timer_deletion
"""
class MongoDB:
    def __init__(self):
        self.mongo_uri = "mongodb://admin:password@localhost:27017"
        self.client = MongoClient(self.mongo_uri)

    def get_collection_users(self, ip) -> Collection | None:
        return self.client.get_database("users")[ip]

    def get_collection_messages(self, ip) -> Collection | None:
        return self.client.get_database("message")[ip]

    def get_database(self, database_name) -> Database | None:
        return self.client.get_database(database_name)

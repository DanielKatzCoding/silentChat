from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from .pydantic_forms import *

__all__ = ["MongoDB", "Msgs", "User"]

"""
This class MongoDB is used to access the mongoDB database.
DataBase structure:
users
└─ username -> ip-private_key(encrypted by given auth_key)
msgs
└─ username -> encrypted_msg-send_to_username-timer_deletion
"""


class MongoDB:
    def __init__(self):
        self.mongo_uri = "mongodb://admin:password@localhost:27017"
        self.client = MongoClient(self.mongo_uri)

    def insert_users(self, obj: User) -> None:
        self.__insert_col(obj, self.client["users"])

    def insert_msg(self, obj: Msgs) -> None:
        self.__insert_col(obj, self.client["msgs"])

    @staticmethod
    def __insert_col(obj, db):
        obj_modified = obj.dict()
        obj_modified.pop("username")
        db[obj.username].insert_one(obj_modified)

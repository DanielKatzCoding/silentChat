from pymongo import MongoClient
from utils.pydantic_forms import *

__all__ = ["MongoDB", "Msg", "User"]

"""
This class MongoDB is used to access the mongoDB database.
DataBase structure:
users
└─ ip -> username-private_key(encrypted by given auth_key)
msgs
└─ ip -> encrypted_msg-from_ip-timer_deletion
"""


class MongoDB:
    def __init__(self):
        self.mongo_uri = "mongodb://admin:password@localhost:27017"
        self.client = MongoClient(self.mongo_uri)

    def insert_user(self, obj: User) -> None:
        self.__insert_col(obj, self.client["users"])

    def insert_msg(self, obj: Msg) -> None:
        self.__insert_col(obj, self.client["msgs"])

    @staticmethod
    def __insert_col(obj, db):
        obj_modified = obj.dict()
        obj_modified.pop("ip")
        db[obj.ip].insert_one(obj_modified)

    def get_user(self, ip) -> list[User] | None:
        col = self.client["users"][ip]
        return [User(**doc) for doc in self.__get_docs(col, **{'ip': col.name})]

    def get_msg(self, ip) -> list[Msg] | None:
        col = self.client["msgs"][ip]
        return [Msg(**doc) for doc in self.__get_docs(col, **{'ip': col.name})]

    @staticmethod
    def __get_docs(col, **kwargs) -> list[dict]:
        return [{**doc, **kwargs} for doc in col.find() if doc.pop('_id', None) is not None or True]


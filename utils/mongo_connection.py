from pymongo import MongoClient

# Connection string with the root user credentials

# Create a MongoClient to connect to MongoDB
client = MongoClient(mongo_uri)

# Access a database (or create it if it doesn't exist)
db = client['test_database']

# Access a collection and insert a document
collection = db['example_collection']
document = {"name": "John Doe", "age": 30}
result = collection.insert_one(document)

print("Document inserted with ID:", result.inserted_id)
"""
This class MongoDB is used to access the mongoDB database.
DataBase structure:
users
└─ cred -> username-ip-private_key(encrypted by given auth_key)
message
└─ ip -> encrypted_msg-send_to_username-timer_deletion
"""
class MongoDB:
    def __init__(self):
        self.mongo_uri = "mongodb://admin:password@localhost:27017"
        self.client = MongoClient(self.mongo_uri)

    def get_collection(self, ):


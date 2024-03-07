from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

client = MongoClient("mongodb://Admin:admin@localhost:27017/")
db = client["injozi"]
users_collection = db["users"]

class User:
    @staticmethod
    def create(username, password, role):
        hashed_password = generate_password_hash(password)
        user = {"username": username, "password": hashed_password, "role": role}
        users_collection.insert_one(user)

    @staticmethod
    def find_by_username(username):
        return users_collection.find_one({"username": username})

    @staticmethod
    def find_by_id(user_id):
        return users_collection.find_one({"_id": user_id})

    @staticmethod
    def update(user_id, data):
        users_collection.update_one({"_id": user_id}, {"$set": data})

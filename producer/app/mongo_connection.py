from pymongo import MongoClient
import os
import json

MONGO_URI = os.getenv("MONGO_URI") 

class MongoManager:
    client = None
    def __init__(self):
        try:
            if not MongoManager.client:
                MongoManager.client = MongoClient(MONGO_URI)
            self.client = MongoManager.client
        except Exception as e:
            raise Exception(f"Could not connect to MongoDB, Error: {str(e)}")
        
    def get_client(self):
        return self.client
    
    def init_db(self, collection):
        try:
            with open('./suspicious_customers_orders.json') as file:
                data = json.load(file)
                collection.insert_many(data)
        except Exception as e:
            raise Exception(f"Could not seed data to MongoDB, Error: {str(e)}")
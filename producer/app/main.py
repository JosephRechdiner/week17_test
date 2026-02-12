from mongo_connection import MongoManager
from kafka_publisher import send_to_kafka
import os

MONGO_DATABASE_NAME = os.getenv("MONGO_DATABASE_NAME")
MONGO_COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME")


def main():
    # init mongo manager
    mongo_manager = MongoManager()

    # init variables
    client = mongo_manager.get_client()
    database = client[MONGO_DATABASE_NAME]
    collection = database[MONGO_COLLECTION_NAME]

    # init db
    mongo_manager.init_db(collection)

    # activate sending to kafka algorithm
    send_to_kafka(collection)

if __name__ == "__main__":
    main()
from confluent_kafka import Producer
import os
import json
import time

KAFKA_BOOOTSTRAP = os.getenv("KAFKA_BOOOTSTRAP")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

producer_config = {
    "bootstrap.servers": KAFKA_BOOOTSTRAP
}

producer = Producer(producer_config)

def get_data_from_collection(collection, skip, limit):
    data = list(collection.find({"_id": 0}).skip(skip).limit(limit))
    return data

def send_to_kafka(collection):
    batches = 30
    skip = 0

    while True:
        data = get_data_from_collection(collection, skip=skip, limit=batches)
        if not data:
            break

        for document in data:
            value = json.dumps(document).encode("utf-8")
            producer.produce(topic=KAFKA_TOPIC, value=value)
            producer.flush()

            time.sleep(0.5)
       
        skip += 30
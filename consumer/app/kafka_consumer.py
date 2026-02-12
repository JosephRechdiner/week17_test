from confluent_kafka import Consumer
import json
import os
from handler import EventsHandler

KAFKA_BOOOTSTRAP = os.getenv("KAFKA_BOOOTSTRAP")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

consumer_config = {
    "bootstrap.servers": KAFKA_BOOOTSTRAP,
    "group.id": "customers-orders",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)

consumer.subscribe([KAFKA_TOPIC])

def listen():
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Error:", msg.error())
            continue

        value = msg.value().decode("utf-8")
        event = json.loads(value)

        if event["type"] == "customer":
            EventsHandler.insert_customer(event)
        if event["type"] == "order":
            EventsHandler.insert_order(event)

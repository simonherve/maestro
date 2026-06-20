import uuid
import json
from confluent_kafka import Producer

PRODUCER_CONFIG = {
    "bootstrap.servers": "localhost:9092"
}

def print_callback(err, msg):
    if err:
        print(f"Delivery fail: {err}")
    else:
        print(f"Delivery succeed: {msg.value().decode('utf-8')}")

producer = Producer(PRODUCER_CONFIG)

message = json.dumps({
    "order_id": str(uuid.uuid4()),
    "user": "Simon",
    "item": "book",
    "quantity": 3
}).encode("utf-8")

producer.produce(
    topic="command",
    value=message,
    callback=print_callback
)

producer.flush()


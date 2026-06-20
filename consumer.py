import json
from confluent_kafka import Consumer

CONSUMER_CONFIG = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "oder-tracker",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(CONSUMER_CONFIG)

consumer.subscribe(["command"])

print("Consumer is running and subscribed to orders topic")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"error: {msg.error()}")
            continue
        value = msg.value().decode("utf-8")
        order = json.loads(value)
        print(f'received order: {order["quantity"]} x {order["item"]} from {order["user"]}')
except KeyboardInterrupt:
    print("Stopping consumer")
finally:
    consumer.close()
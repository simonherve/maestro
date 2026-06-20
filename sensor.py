import random
import time
from faker import Faker
import string

def stable_temperature_sensor(tBase, tdelta, sleep):
    fake = Faker()
    sensorId = fake.bothify(text="???-######", letters=string.ascii_uppercase)
    while True:
        temp = tBase + random.uniform(-tdelta, tdelta)
        data = {
            "source": sensorId,
            "metric": "temperature",
            "value": round(temp, 3),
            "unit": "celsius",
            "timestamp": time.time()
        }
        time.sleep(sleep)
        yield data

if __name__ == "__main__":
    for data in stable_temperature_sensor(60, 0.5, 0.3):
        print(data)
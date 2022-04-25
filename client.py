import time
import random
import json
import paho.mqtt.client as mqtt

class Network:
    def __init__(self, address, port, topic):
        self.address = address
        self.port = port
        self.topic = topic
        self.client_id = f"car-{random.randint(0, 100)}"
        self.client = mqtt.Client(self.client_id)

    def start(self, handle_message_func):
        self.handle_message_func = handle_message_func

        self.client.on_connect = self.on_connect
        self.client.connect(self.address, self.port)

        self.client.on_message = self.on_message
        self.client.subscribe(self.topic)

    def loop(self):
        self.client.loop()

    def send(self, data):
        new_dict = {**data, **{"client_id": self.client_id}}
        raw = json.dumps(new_dict)
        self.client.publish(self.topic, payload=raw)

    # Private callbakcs
    def on_connect(self, client, userdata, flags, rc):
        print("Connected to server")

    def on_message(self, client, userdata, msg):
        raw = msg.payload.decode()

        try:
            decoded = json.loads(raw)
        except json.decoder.JSONDecodeError:
            print("Invalid data received")
            return

        if decoded['client_id'] == self.client_id:
            return
        self.handle_message_func(decoded)

net = Network("54.36.103.5", 1883, "update")
net.start(lambda received: print(received))
while True:
    net.send({"connard": True})
    net.loop()
    time.sleep(1)

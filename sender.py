import time
import random
from client import Network

net = Network("54.36.103.5", 1883, "update", f"car-{random.randint(0, 100)}")

net.start(lambda s: s)
net.loop()

speed = 0

try:
    while True:
        net.send({"speed": speed})
        speed += 1
        time.sleep(1)
except KeyboardInterrupt:
    net.disconnect()
    print("Interrupted by user")

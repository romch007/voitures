import time
import random
from client import Network

net = Network("54.36.103.5", 1883, "update", f"gros_bg-{random.randint(0, 100)}")

net.start(lambda s: s)
net.loop()

try:
    while True:
        net.send({"logan": "t'es vraiment pd"})
        time.sleep(1)
except KeyboardInterrupt:
    net.disconnect()
    print("Interrupted by user")

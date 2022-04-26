import time
import random
from client import Network

net = Network("54.36.103.5", 1883, "update", f"LE PLUS GROS PUCEAU n{random.randint(0, 1000)}")

net.start(lambda s: s)
net.loop()

try:
    speed= 0
    while True:
        net.send({"qui": f"c'est moi mdr ejac en {speed}"})
        speed += 1
        time.sleep(1)
except KeyboardInterrupt:
    net.disconnect()
    print("Interrupted by user")

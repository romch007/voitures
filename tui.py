import random
from client import Network
from ui import UI

ui = UI()
net = Network("54.36.103.5", 1883, "update", f"display-{random.randint(0, 100)}")

def handle_receive(data):
    ui.handle_update(data)

net.start(handle_receive)
try:
    net.loop(forever=True)
except KeyboardInterrupt:
    net.disconnect()
    print("Interrupted by user")



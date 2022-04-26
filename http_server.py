import random
from flask import Flask, render_template
from client import Network
from flask_socketio import SocketIO, emit

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='static')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# MQTT configuration
net = Network("54.36.103.5", 1883, "update", f"display-{random.randint(0, 100)}")

def handle_mqtt_receive(payload):
    socketio.emit('update', payload, broadcast=True)

net.start(handle_mqtt_receive)
net.loop(forever=False)

@socketio.on('connect')
def handle_new_connection():
    print("New client connected")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app)

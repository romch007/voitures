from __future__ import print_function
import time
import chalk
import platform
import os

green = chalk.Chalk('green')
bold = chalk.utils.FontFormat('bold')

class UI:
    def __init__(self):
        self.cars = {}

    def handle_update(self, payload):
        client_id = payload['client_id']
        self.cars[client_id] = payload
        self.clear()
        self.print_ui()

    def print_ui(self):
        for client_id, data in self.cars.items():
            print(bold(client_id) + " - " + green(data))

    def clear(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

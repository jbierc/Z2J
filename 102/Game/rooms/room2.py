from room import Room
from room3 import Room3

class Room2(Room):
    def __init__(self):
        super().__init__("room2")

    def handle_command(self, command):
        if command == "turn":
            pass
        else:
            pass
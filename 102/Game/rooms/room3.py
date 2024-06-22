from room import Room
from room2 import Room2

class Room3(Room):
    def __init__(self):
        super().__init__("room1")

    def handle_command(self, command):
        if command == "turn":
            pass
        else:
            pass
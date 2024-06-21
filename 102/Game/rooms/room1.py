from room import Room


class Room1(Room):
    def __init__(self):
        super().__init__('room1')

    def handle_command(self, command):
        if command == "turn":
            pass
        else:
            pass
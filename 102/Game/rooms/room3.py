from room import Room


class Room3(Room):
    def __init__(self):
        super().__init__('room1')

    def handle_command(self, command):
        if command == "turn":
            return Room2()
        else:
            print("Nieznane polecenie.")
            return None
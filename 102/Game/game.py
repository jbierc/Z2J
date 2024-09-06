"""
Potem zrób wpis na p-102-egzamin 
Wpis ma zawierać 4 elementy:

1. Napisz co sprawiło Ci największy problem i jak udało Ci się z tym poradzić.
2. Daj link do nagrania rozgrywki.
3. Daj link do repozytorium z kodem (publicznie dostępne).
4. Jeśli do rozwiązania były Ci potrzebne inne materiały niż książka, wrzuć linki.
"""

from rooms.room1 import Room1, Room1_1, Room1_2
from rooms.room2 import Room2
from items.gear import Wheel
from items.pedestal import Pedestal
from items.doors import Door1, Door2

class Game:
    def __init__(self):
        self.player = Player()
        self.is_playing = True
        self.current_room = Room1()
        self.current_item = None
        self.items = {
            "door": Door1(),
            "door2": Door2(),
            "wheel": Wheel(),
            "pedestal": Pedestal()
        }
        # buttons state
        self.left = False
        self.centre = False
        self.right = False
        self.used_items = {}
        self.commands = {
            "help": self.show_help,
            "describe": self.describe_room,
            "items": self.player.list_items,
            "quit": self.quit_game,
            "door": self.door1,
            "wheel": self.wheel,
            "pedestal": self.pedestal,
            "take": self.take_item,
            "use": self.use_item
        }

    def start(self):
        self.player.player_name()
        self.intro()
        while self.is_playing:
            self.user_input()

    def intro(self):
        print(f"Welcome in the Game {self.player.name}, find the Treasure! Type 'help' to display a list of commmands...")
        print("*UPPER CASE letters indicate keywords you can type in*")

    def user_input(self):
        command = input("> ").strip().lower()
        self.handle_command(command)

    def handle_command(self, command):
        if command in ["left", "centre", "right"]:
            self.minigame(command)
        else:
            action = self.commands.get(command, self.unknown_command)
            action()

    def describe_room(self):
        self.current_room.display_description()

    def door1(self):
        if "wheel" in self.used_items:
            self.items["door"].used()
            self.current_room = Room2()
        else:
            self.items["door"].display_description()
    
    def wheel(self):
        if "wheel" in self.player.items:
            self.current_item = self.items["wheel"]
            print("Would you like to USE it on PEDESTAL?")
        elif "wheel" in self.used_items:
            self.current_item = self.used_items["wheel"]
            self.current_item.used()
            self.current_item = None
        else:
            self.current_item = self.items["wheel"]
            self.current_item.display_description()

    def pedestal(self):
        if "wheel" not in self.used_items:
            self.items["pedestal"].display_description()
        else:  
            self.describe_room()

    def minigame(self, command):
        if command == "left":
            if self.centre == True:
                print("""                *** SUCCESS! ***                        
   _______          _______          _______ 
  |       |        |       |        |       |""")
            else:
                self.left = True
                self.centre = False
                self.right = True
                print("""                    _______                 
   _______         |       |         _______ 
  |       |        |       |        |       |""")
        if command == "centre":
            if self.left == True:
                self.left = False
            self.centre = True
            if self.right == True:
                self.right = False
            print("""   _______                           _______
  |       |         _______         |       |
  |       |        |       |        |       |
""")
        if command == "right":
            self.left = True
            if self.centre == True:
                self.centre = False
            if self.right == False:
                self.right = True
            print("""                    _______                 
   _______         |       |         _______ 
  |       |        |       |        |       |""")
        
        
    def take_item(self):
        if self.current_item:
            self.player.items[self.current_item.name] = self.current_item
            print(f"You took {self.current_item.name.upper()} to your backpack.")
            self.current_item = None
        else:
            print("What item would you like to take? Maybe I can DESCRIBE this room for you?")
        if "wheel" in self.player.items:
            self.current_room = Room1_1()
    
    def use_item(self):
        if self.current_item:
            self.current_item.use()
            if self.current_item.name in self.player.items:
                self.used_items[self.current_item.name] = self.current_item
                del self.player.items[self.current_item.name]
            self.used_items[self.current_item.name] = self.current_item
            if "wheel" in self.used_items:
                self.current_room = Room1_2()
            self.current_item = None
        else:
            if self.player.items:
                print(f"What item would you like to use? You have {', '.join(self.player.items.keys()).upper()} in your backpack.")
            else:
                print("You have no items in your backpack.")

    def show_help(self):
        print("Type 'describe' to display a description of your surroundings...")
        print("Type 'items' to display a list of items...")
        print("Type 'quit' to exit the game...")

    def quit_game(self):
        self.is_playing = False
        print("Quitting the game...")

    def unknown_command(self):
        print("Unknown command. Type 'help' to see the list of available commands.")
    
    '''
    def save_game(self):
        with open("savegame.txt", "w") as f:
            f.write(self.current_room)

    def load_game(self):
        if os.path.exists("savegame.txt"):
            with open("savegame.txt", "r") as f:
                self.current_room = f.read().strip()
        else:
            print("No saved game.")
    '''

class Player:

    def __init__(self):
        self.name = None
        self.items = {}

    def player_name(self):
        print("Type your name:")
        self.name = input("> ")

    def list_items(self):
        if self.items:
            print(f"You have {', '.join(self.items.keys()).upper()} in your backpack.")
        else:
            print("You have no items in your backpack.")

game = Game()
game.start()
from rooms.room1 import Room1, Room1_1, Room1_2
from rooms.room2 import Room2, Room2_1, Room2_2
from rooms.room3 import Room3
from items.wheel import Wheel
from items.pedestal import Pedestal
from items.key import Key
from items.door import Door

class Game:
    def __init__(self):
        self.player = Player()
        self.is_playing = True

        self.current_room = Room1()
        self.current_item = None

        self.items = {
            "door": Door(),
            "wheel": Wheel(),
            "pedestal": Pedestal(),
            "key": Key()
        }
        self.used_items = {}

        # buttons state
        self.minigame_state = False
        self.left = False
        self.centre = False
        self.right = False

        self.commands = {
            "help": self.show_help,
            "describe": self.describe_room,
            "items": self.player.list_items,
            "quit": self.quit_game,
            "door": self.door,
            "wheel": self.wheel,
            "pedestal": self.pedestal,
            "key": self.key,
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
        if command in ["left", "centre", "right"] and isinstance(self.current_room, Room2) and self.minigame_state == False:
            self.minigame(command)
        else:
            action = self.commands.get(command, self.unknown_command)
            action()

    def describe_room(self):
        self.current_room.display_description()

    def door(self):
        if "wheel" in self.used_items:
            self.items["door"].used()
            self.current_room = Room2()
        else:
            self.items["door"].display_description()
    
    def wheel(self):
        if "wheel" in self.player.items:
            self.current_item = self.items["wheel"]
            print("Would you like to USE it on a PEDESTAL?")
        elif "wheel" in self.used_items:
            self.used_items["wheel"].used()
        else:
            self.current_item = self.items["wheel"]
            self.current_item.display_description()

    def pedestal(self):
        if "wheel" not in self.used_items:
            self.items["pedestal"].display_description()
        else:  
            self.describe_room()
    
    def key(self):
        if "key" in self.player.items:
            self.current_item = self.items["key"]
            print("Would you like to USE it on a keyhole?")
        else:
            self.current_item = self.items["key"]
            self.current_item.display_description()

    def minigame(self, command):
        if command == "left":
            if self.centre == True:
                print("""                *** SUCCESS! ***                        
   _______          _______          _______ 
  |       |        |       |        |       |
                      """)
                Room2_1().display_description()
                self.minigame_state = True
                self.current_room = Room2_1()
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
        if "key" in self.player.items:
            self.current_room = Room2_2()
    
    def use_item(self):
        if self.current_item:
            self.current_item.use()
            if self.current_item.name in self.player.items:
                del self.player.items[self.current_item.name]
            self.used_items[self.current_item.name] = self.current_item
            if "wheel" in self.used_items:
                self.current_room = Room1_2()
            if "key" in self.used_items:
                self.current_room = Room3()
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
        print("Wrong command. Type 'help' to see the list of available commands.")

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
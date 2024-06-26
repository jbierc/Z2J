"""
Napisz prostą grę tekstową. Wymyśl prostą zagadkę, zaprojektuj jedno, max dwa pomieszczenia,
dodaj możliwość zdobywania i używania przedmiotów. Pozwól nam przeżyć jakąś mini przygodę.

help - wyświetli listę dostępnych instrukcji
describe - opisuje aktualne pomieszczenie
items - wyświetli listę przedmiotów
take PRZEDMIOT
use PRZEDMIOT

Dodaj komendy, które uznasz jeszcze za potrzebne.
Użyj klas i operacji wejścia/wyjścia.

Potem zrób wpis na p-102-egzamin 
Wpis ma zawierać 4 elementy:

1. Napisz co sprawiło Ci największy problem i jak udało Ci się z tym poradzić.
2. Daj link do nagrania rozgrywki.
3. Daj link do repozytorium z kodem (publicznie dostępne).
4. Jeśli do rozwiązania były Ci potrzebne inne materiały niż książka, wrzuć linki.
"""

from rooms.room1 import Room1


class Game:
    def __init__(self):
        self.player = Player()
        self.is_playing = True
        self.current_room = Room1()
        self.commands = {
            "help": self.show_help,
            "describe": self.describe_room,
            "items": self.player.list_items,
            "quit": self.quit_game,
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
        action = self.commands.get(command, self.unknown_command)
        action()

    def show_help(self):
        print("Type 'describe' to display a description of your surroundings...")
        print("Type 'items' to display a list of items...")
        print("Type 'quit' to exit the game...")

    def describe_room(self):
        self.current_room.display_description()

    def quit_game(self):
        self.is_playing = False
        print("Exiting the game...")

    def unknown_command(self):
        print("Unknown command. Type 'help' to see the list of available commands.")
    
    '''
    def save_game(self):
        with open("savegame.txt", "w") as f:
            f.write(self.location)

    def load_game(self):
        if os.path.exists("savegame.txt"):
            with open("savegame.txt", "r") as f:
                self.location = f.read().strip()
        else:
            print("Brak zapisanego stanu gry.")
    '''

class Player:
    items = []

    def __init__(self):
        self.name = None

    def player_name(self):
        print("Type your name:")
        self.name = input("> ")

    def list_items(self):
        print(", ".join(self.items))

    def take_item(self, item):
        self.items.append(item)


game = Game()
game.start()
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
        self.is_playing = True
        self.current_room = Room1()

    def start(self):
        self.intro()
        while self.is_playing:
            self.user_input()

    def intro(self):
        print("Welcome in the Game, find the Treasure!")
        print("Type 'help' to display list of commmands...")
        #print("Type 'describe' to display a decription of surroundings...")
        #print("Type 'items' to display a decription of surroundings...")

    def user_input(self):
        command = input("> ").strip().lower()
        if command == "quit":
            self.is_playing = False
        else:
            self.handle_command(command)

    def handle_command(self, command):
        if command == "help":
            print()
        if command == "describe":
            self.current_room.display_description()

game = Game()
game.start()
from pathlib import Path

class Room:
    def __init__(self, name):
        self.name = name
        self.description = self.load_description(name)
    
    def __str__(self):
        return self.description

    def load_description(self, name):
        path = Path(__file__).parent / 'rooms' / 'descriptions' / f'{name}.txt'
        with path.open(encoding='utf-8') as file:
            for line in file.readlines():
                print(line, end='')

    
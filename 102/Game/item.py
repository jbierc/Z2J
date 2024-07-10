from pathlib import Path

class Item:
    def __init__(self, name):
        self.name = name
        self.description = self.load_description(name)

    def load_description(self, name):
        path = Path(__file__).parent / "items" / "descriptions" / f"{name}.txt"
        with path.open(encoding="utf-8") as file:
            return file.readlines()
        
    def display_description(self):
        for line in self.description:
            print(line.strip())
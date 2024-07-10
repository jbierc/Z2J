from item import Item

class Door1(Item):
    def __init__(self):
        super().__init__("door1")
        self.open = False
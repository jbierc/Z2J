from item import Item

class Gear(Item):
    def __init__(self):
        super().__init__("a gear")
        self.used = False
        self.taken = False
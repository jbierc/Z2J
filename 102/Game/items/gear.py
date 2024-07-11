from item import Item

class Wheel(Item):
    def __init__(self):
        super().__init__("wheel")
        self.used = False
        self.taken = False
    def use(self):
        
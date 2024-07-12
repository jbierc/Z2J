from item import Item

class Door1(Item):
    def __init__(self):
        super().__init__("door1")
        self.open = False

    def used(self):
        self.description = self.load_description("door1_1")
        self.display_description()

class Door2(Item):
    def __init__(self):
        super().__init__("door2")
        self.open = False
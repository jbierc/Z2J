from item import Item

class Door(Item):
    
    def __init__(self):
        super().__init__("door")

    def used(self):
        self.description = self.load_description("door used")
        self.display_description()
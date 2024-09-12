from item import Item

class Key(Item):

    def __init__(self):
        super().__init__("key")

    def use(self):
        self.description = self.load_description("key use")
        self.display_description()
    
    def used(self):
        self.description = self.load_description("key used")
        self.display_description()
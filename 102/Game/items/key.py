from item import Item

class Key(Item):

    def __init__(self):
        super().__init__("key")

    def use(self):
        self.description = self.load_description("use key")
        self.display_description()
    
    def used(self):
        self.description = self.load_description("used key")
        self.display_description()
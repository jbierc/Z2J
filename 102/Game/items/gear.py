from item import Item

class Wheel(Item):

    def __init__(self):
        super().__init__("wheel")

    def use(self):
        self.description = self.load_description("use wheel")
        self.display_description()
    
    def used(self):
        self.description = self.load_description("used wheel")
        self.display_description()
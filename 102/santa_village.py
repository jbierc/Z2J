class Building:
    def __init__(self, name, open = False):
        self.name = name
        self.open = open
    
    def __str__(self):
        return f'building: {self.name}.'
    
    def open_for_visitors(self):
        self.open = True
        print(f"{self.name} welcomes visitors!")
    
    def close_for_visitors(self):
        self.open = False
        print(f"Sorry, the {self.name} is now closed...")
    
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name: {self.name} age: {self.age}'
        
class Elf:
    def __init__(self, name, age, allocation):
        self.name = name
        self.age = age
        self.allocation = allocation

    def __str__(self):
        return f'name: {self.name} age: {self.age} allocation: {self.allocation}'
    
class Reindeer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class SantaHome(Building):
    residents = []

    def add_resident(self, resident):
        self.residents.append(resident)

class PostOffice(Building):
    
    def review_letters(self):
        print("All kids were polite this year.")

class Factory(Building):
    
    def pack_presents(self):
        print("Presents are packed and ready to go.")

class Stable(Building):
    reindeers = []

    def add_reindeer(self, reindeer):
        self.reindeers.append(reindeer)
    
    def prepare_sledge(self):
        print("Sledge are prepared and ready to go.")

class Santa(Human):
    
    def christmas_time(self):
        print("Santa Claus has all the presents and has started delivering them.")

class SantaWife(Human):
    
    def bake_cookies(self):
        print("Freshly baked cookies are ready to fill the elves bellies")

class ElfManager(Elf):

    def start_shift(self):
        print(f'Shift started working at {self.allocation.name}.')

class ElfWorker(Elf):

    def __init__(self, name, age, allocation, profession):
        super().__init__(name, age, allocation)
        self.profession = profession

class Visitor(Human):

    def __init__(self, name, age, days_of_visit):
        super().__init__(name, age)
        self.days_of_visit = days_of_visit



santa_home = SantaHome("Santa Claus Home")
post_office = PostOffice("Post Office")
factory = Factory("Factory")
stable = Stable("Stable")

santa = Santa("Santa Claus", 777)
santa_wife = SantaWife("Santa Wife", 777)

elf_post_manager = ElfManager("Zephyr", 78, post_office)
elf_factory_manager = ElfManager("Thistle", 65, factory)
elf_stable_manager = ElfManager("Willow", 58, stable)
elf_postman = ElfWorker("Bumble", 68, post_office, "postman")
elf_constructor = ElfWorker("Sparkle", 83, factory, "constructor")
elf_stableman = ElfWorker("Twinkle", 47, stable, "stableman")

reindeer = Reindeer("Blizzard", 12)
visitor = Visitor("Olaf", 14, 4)

santa_home.add_resident(santa)
santa_home.add_resident(santa_wife)
santa_home.open_for_visitors()
santa_wife.bake_cookies()

elf_post_manager.start_shift()
post_office.review_letters()
elf_factory_manager.start_shift()
factory.pack_presents()
stable.add_reindeer(reindeer)
stable.prepare_sledge()

santa.christmas_time()

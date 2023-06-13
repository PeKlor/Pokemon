import random

from Type import Type


class Pokemon:

    def __init__(self, name, its_type: Type, moveset, cry):
        self.name = name
        self.its_type = its_type
        self.moveset = ["", "", "", ""]
        self.moveset = moveset
        self.cry = cry

    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.its_type

    def get_moveset(self):
        return self.moveset

    def get_cry(self):
        return self.cry

    def use_attack(self):
        return random.choice(self.get_moveset())

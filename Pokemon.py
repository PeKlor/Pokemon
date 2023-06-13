from Type.py import Type

def initialize_Moveset(moveset):
        moveset = ["", "", "", ""]

class Pokemon():

    def __init__(self, name, type: Type, moveset, cry):
        self.name = name
        self.type = type
        self.moveset = moveset
        initialize_Moveset(self.moveset)
        self.cry = cry

    def get_Name(self):
        return self.name
    
    def get_Type(self):
        return self.type

    def get_Cry(self):
        return self.cry



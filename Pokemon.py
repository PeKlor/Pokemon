from Type.py import Type

class Pokemon():

    def __init__(self, name, type, moveset):
        self.name = name
        self.type = type
        self.moveset = moveset

    def get_Name(self):
        return self.name
    
    def get_Type(self):
        return self.type


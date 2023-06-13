# Welcome to the world of Pokemon!
import Type.py
from Pokemon import Pokemon

available_Types = ["Fire", "Water", "Grass"]

charmander_Moveset = ["Tackle", "Ember", "Tail Whip", "Growl"]
charmander = Pokemon("Charmander", "Fire", charmander_Moveset, "Char Char!")

print(charmander.get_Name() + " attacks! " + charmander.get_Cry())



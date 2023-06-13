# Welcome to the world of Pokemon!
from Type import Type
from Pokemon import Pokemon

its_type = Type()
charmander_moveset = ["Tackle", "Ember", "Tail Whip", "Growl"]
charmander = Pokemon("Charmander", its_type.set_type("Fire"), charmander_moveset, "Char Char!")

print(charmander.get_name() + " attacks! " + charmander.get_cry())

# Welcome to the world of Pokemon!
from Type import Type
from Pokemon import Pokemon
from Menu import Menu


new_menu = Menu()
new_menu.show_dialog()
player_choice = input(new_menu.give_choice())
its_type = Type()
starter_pokemon = Pokemon("", its_type.set_type(""), ["", "", "", ""], "")
# while player_choice not in range(1, 3):
if player_choice == 1:
    moveset = ["Tackle", "Growl", "Leech Seed", "Vine Whip"]
    pokemon_choice = Pokemon("Bulbasaur", its_type.set_type("Grass"), moveset, "Bul Ba!")
    starter_pokemon.becomes(pokemon_choice)
elif player_choice == 2:
    moveset = ["Scratch", "Growl", "Ember", "Leer"]
    pokemon_choice = Pokemon("Charmander", its_type.set_type("Fire"), moveset, "Char Char!")
    starter_pokemon.becomes(pokemon_choice)
elif player_choice == 3:
    moveset = ["Tackle", "Tail Whip", "Bubble", "Water Gun"]
    pokemon_choice = Pokemon("Squirtle", its_type.set_type("Water"), moveset, "Squirtle!")
    starter_pokemon.becomes(pokemon_choice)

print("You chose " + starter_pokemon.get_name() + " ! " + starter_pokemon.get_cry())
# cpu_choice =

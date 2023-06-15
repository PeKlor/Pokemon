from Pokemon import Pokemon


class Pokedex:

    def __init__(self):
        self.dex = []

    def add_pokemon(self, new_pokemon: Pokemon):
        self.dex.append(new_pokemon)

    def get_size(self):
        return len(self.dex)



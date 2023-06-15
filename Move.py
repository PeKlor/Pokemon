from Type import Type


class Move:

    def __init__(self, name: str, its_type: Type, damage: int):
        self.name = name
        self.type = its_type
        self.damage = damage

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_type(self):
        return self.type

    def set_type(self, its_type):
        self.type = its_type

    def get_damage(self):
        return self.damage

    def set_damage(self, damage):
        self.damage = damage

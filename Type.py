class Type:
    
    def __init__(self, type_name=""):
        self.type_name = type_name
        # self.available_types = ["Fire", "Water", "Grass"]

    def get_type(self):
        return self.type_name

    def set_type(self, string):
        self.type_name = string

    def is_weak_to(self, other_type):
        if self.type_name == "Fire" and other_type == "Water":
            return True
        elif self.type_name == "Water" and other_type == "Grass":
            return True
        elif self.type_name == "Grass" and other_type == "Fire":
            return True
        return False
    
    def is_effective_on(self, other_type):
        if self.type_name == "Fire" and other_type == "Grass":
            return True
        elif self.type_name == "Water" and other_type == "Fire":
            return True
        elif self.type_name == "Grass" and other_type == "Water":
            return True
        return False

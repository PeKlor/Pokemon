class Type():

    def __init__(self, type):
        self.type = type

    def get_Type(self):
        return self.type

    def is_Weak_To(self, other_type):
        if self.type == "Fire" and other_type == "Water":
            return True
        elif self.type == "Water" and other_type == "Grass":
            return True
        elif self.type == "Grass" and other_type == "Fire":
            return True
        return False
    
    def is_Effective_On(self, other_type):
        if self.type == "Fire" and other_type == "Grass":
            return True
        elif self.type == "Water" and other_type == "Fire":
            return True
        elif self.type == "Grass" and other_type == "Water":
            return True
        return False

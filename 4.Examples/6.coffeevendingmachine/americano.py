from coffee import Coffee

class Americano(Coffee):
    def __init__(self):
        self.ingredients = ["coffee beans", "water", "milk"]
        self.cost = 8
        self.description = "Americano"



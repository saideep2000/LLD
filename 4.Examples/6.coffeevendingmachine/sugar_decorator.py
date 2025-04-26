from coffee_decorator import CoffeeDecorator

class SugarDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
        self.ingredients = ["sugar"]
        self.cost = 0.2
        self.description = "sugar"
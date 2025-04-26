from coffee_decorator import CoffeeDecorator

class CaramelDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
        self.ingredients = ["caramel"]
        self.cost = 0.7
        self.description = "caramel"
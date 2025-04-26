from coffee_decorator import CoffeeDecorator
from typing import List

class MilkDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
        self.ingredients = ["milk"]
        self.cost = 0.5
        self.description = "milk"

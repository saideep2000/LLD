"""

Ingredients
Coffee
Americano(Coffee)
Espresso(Coffee)
CoffeeDecorator
SugarDecorator(CoffeeDecorator)
MilkDecorator(CoffeeDecorator)
CarmelDecorator(CoffeeDecorator)

"""


# class Ingredients():
#     def __init__(self):
#         pass

class Coffee():
    def __init__(self):
        self.ingredients = []
        self.description = ""
        self.cost = 0
    
    def get_cost(self):
        return self.cost
    
    def get_ingredients(self):
        return self.ingredients
    
    def get_description(self):
        return self.description

class Americano(Coffee):
    def __init__(self):
        self.ingredients = ["coffee beans", "milk"]
        self.cost = 8
        self.description = "Americano"

class Espresso(Coffee):
    def __init__(self):
        self.ingredients = ["coffee beans", "water"]
        self.cost = 6
        self.description = "Espresso"

class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee
        super().__init__()

    def get_cost(self):
        return self.cost + self.coffee.get_cost()
    
    def get_ingredients(self):
        return self.ingredients + self.coffee.get_ingredients()
    
    def get_description(self):
        return self.description + self.coffee.get_description()



class SugarDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
        self.ingredients = ["Sugar"]
        self.cost = 2
        self.description = "Sugar"

class MilkDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
        self.ingredients = ["Milk"]
        self.cost = 4
        self.description = "Milk"

class CarmelDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
        self.ingredients = ["Caramel"]
        self.cost = 3
        self.description = "Caramel"

from typing import List

class CoffeeVendingMachine():
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CoffeeVendingMachine, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, "initialised"):
            self.initialised = True
            self.decorators = {
                "sugar_decorator" : SugarDecorator,
                "milk_decoartor" : MilkDecorator,
                "caramel_decorator" : CarmelDecorator
            }
        
    def make_coffee(self, coffee, add_ons : List[Coffee]):
        for each in add_ons:
            coffee = self.decorators.get(each)(coffee)
        return coffee



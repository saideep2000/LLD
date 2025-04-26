from coffee import Coffee
from espresso import Espresso
from americano import Americano

class CoffeeMachine():
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CoffeeMachine, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, "initialized"):
            self.initialized = True

            self.base_coffee_type = {
                "espresso" : Espresso,
                "americano" : Americano
            }

            self.extra_decorators = {
                'milk': MilkDecorator,
                'sugar': SugarDecorator,
                'caramel': CaramelDecorator,
                'whipped_cream': WhippedCreamDecorator
            }


    def make_coffee(self, base_coffee : Coffee, extras = None):
        if base_coffee not in self.base_coffee_type:
            raise ValueError("Base Coffee is not provided")

        if extras:
            for extra in extras:
                if extra not in self.extra_decorators:
                    raise ValueError(f"Provided extra {extra} is not in our collection")
                base_coffee = self.extra_decorators[extra](base_coffee)
        
        return base_coffee
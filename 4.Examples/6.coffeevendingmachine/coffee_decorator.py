from coffee import Coffee

class CoffeeDecorator(Coffee):
    def __init__(self, coffee : Coffee):
        self.coffee = coffee
        super().__init__()

    
    def get_ingredients(self):
        return self.coffee.get_ingredients() + self.ingredients
    
    def get_cost(self):
        return self.coffee.get_cost() + self.cost
    
    def get_description(self):
        return f"{self.coffee.get_description()} with {self.description}"


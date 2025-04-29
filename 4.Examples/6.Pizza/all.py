class Pizza():
    def __init__(self):
        self.base = "Flour"
        self.size = None
        self.sauce = None
        self.protein = []
        self.toppings = []
        self.extra_cheese = False
    
    def get_cost(self):
        size = {"small" : 2, "large" : 4, "xl" : 5}
        sauce = {"tomato" : 3, "ranch" : 4}
        protein = {"chicken" : 4, "brocolli" : 2}
        toppings = {"olives" : 2, "onions" : 3, "capcicum" : 2}

        cost = 0

        if self.size is not None:
            cost = cost + size[self.size]
        if self.sauce is not None:
            cost = cost + sauce[self.sauce]
        for each in self.protein:
            cost = cost + protein[each]
        for each in self.toppings:
            cost = cost + toppings[each]
        if self.extra_cheese:
            cost = cost + 2
        
        return cost

class PizzaBuilder():
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.pizza = Pizza()
    
    def add_chicken(self):
        self.pizza.ingredients.append("chicken")

    def add_cheese(self):
        self.pizza.ingredients.append("cheese")
    
    def add_olives(self):
        self.pizza.ingredients.append("olives")

class pizza_demo():
    def __init__(self):
        pass


from pizza import Pizza

class PizzaBuilder():
    def __init__(self):
        self.rest()
    
    def reset(self):
        self.pizza = Pizza()
    
    def set_size(self, size):
        self.pizza.size = size
    
    def set_crust(self, crust):
        self.pizza.crust = crust
        return self
    
    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self
    
    def add_cheese(self, cheese):
        self.pizza.cheese.append(cheese)
        return self
    
    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self
    
    def add_extra(self, extra):
        self.pizza.extras.append(extra)
        return self
    
    def build(self):
        pizza = self.pizza
        self.reset()  # Reset for next build
        return pizza
    
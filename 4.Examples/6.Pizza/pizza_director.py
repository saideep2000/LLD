class PizzaDirector():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PizzaDirector, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, builder):
        if not hasattr(self, "initialised"):
            self.initialised = True
            self.builder = builder
    
    def make_margherita(self):
        """Create a classic Margherita pizza"""
        return (self.builder
                .set_size("Medium")
                .set_crust("Thin")
                .set_sauce("Tomato")
                .add_cheese("Mozzarella")
                .add_topping("Fresh Basil")
                .build())
    
    def make_pepperoni(self):
        """Create a pepperoni pizza"""
        return (self.builder
                .set_size("Large")
                .set_crust("Regular")
                .set_sauce("Tomato")
                .add_cheese("Mozzarella")
                .add_topping("Pepperoni")
                .build())
    
    def make_supreme(self):
        """Create a supreme pizza with many toppings"""
        return (self.builder
                .set_size("Large")
                .set_crust("Thick")
                .set_sauce("Tomato")
                .add_cheese("Mozzarella")
                .add_cheese("Cheddar")
                .add_topping("Pepperoni")
                .add_topping("Sausage")
                .add_topping("Bell Peppers")
                .add_topping("Onions")
                .add_topping("Black Olives")
                .add_topping("Mushrooms")
                .build())
    
    def make_vegetarian(self):
        """Create a vegetarian pizza"""
        return (self.builder
                .set_size("Medium")
                .set_crust("Regular")
                .set_sauce("Tomato")
                .add_cheese("Mozzarella")
                .add_topping("Bell Peppers")
                .add_topping("Onions")
                .add_topping("Mushrooms")
                .add_topping("Tomatoes")
                .add_topping("Spinach")
                .build())
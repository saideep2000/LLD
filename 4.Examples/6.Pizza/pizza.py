class Pizza():
    def __init__(self):
        self.size = None
        self.crust = None
        self.sauce = None
        self.cheese = []
        self.toppings = []
        self.extras = []

    def __str__(self):
        pizza_str = f"{self.size} {self.crust} crust pizza with {self.sauce} sauce"
        
        if self.cheese:
            cheese_str = ", ".join(self.cheese)
            pizza_str += f" and {cheese_str} cheese"
        
        if self.toppings:
            toppings_str = ", ".join(self.toppings)
            pizza_str += f"\nToppings: {toppings_str}"
        
        if self.extras:
            extras_str = ", ".join(self.extras)
            pizza_str += f"\nExtras: {extras_str}"
            
        return pizza_str

    def get_price(self):
        # Base prices
        size_prices = {"small": 8.99, "medium": 10.99, "large": 12.99, "extra large": 14.99}
        crust_prices = {"thin": 0, "regular": 0, "thick": 1.50, "stuffed": 2.50}
        
        # Start with base price
        total = size_prices.get(self.size.lower(), 0)
        total += crust_prices.get(self.crust.lower(), 0)
        
        # Add toppings ($1.25 each)
        total += len(self.toppings) * 1.25
        
        # Add extra cheese ($1.00 per type beyond the first)
        if len(self.cheese) > 1:
            total += (len(self.cheese) - 1) * 1.00
            
        # Add extras
        total += len(self.extras) * 0.75
        
        return total
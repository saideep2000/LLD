from pizza_director import PizzaDirector
from pizza_builder import PizzaBuilder

class PizzaDemo():
    @staticmethod
    def run():
        director = PizzaDirector()
        builder = PizzaBuilder()
        
        # Use the builder directly for custom pizza
        custom_pizza = (builder
                    .set_size("Extra Large")
                    .set_crust("Stuffed")
                    .set_sauce("BBQ")
                    .add_cheese("Mozzarella")
                    .add_cheese("Provolone")
                    .add_topping("Chicken")
                    .add_topping("Bacon")
                    .add_topping("Red Onions")
                    .add_extra("Ranch Dipping Sauce")
                    .build())
        
        print("=== Custom Pizza ===")
        print(custom_pizza)
        print(f"Price: ${custom_pizza.get_price():.2f}")
        print()
        
        
        director = PizzaDirector(builder)
        
        # Make some predefined pizzas
        margherita = director.make_margherita()
        print("=== Margherita Pizza ===")
        print(margherita)
        print(f"Price: ${margherita.get_price():.2f}")
        print()




if __name__ == "__main__":
    PizzaDemo.run()
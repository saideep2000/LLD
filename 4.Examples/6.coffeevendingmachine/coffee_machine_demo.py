from coffee_machine import CoffeeMachine

class CoffeeMachineDemo():
    @staticmethod
    def run():
        machine = CoffeeMachine()

        espresso = machine.make_coffee('espresso')
        print(f"Ordered: {espresso.get_description()}")
        print(f"Ingredients: {', '.join(espresso.get_ingredients())}")
        print(f"Cost: ${espresso.get_cost():.2f}")
        print()

        fancy_coffee = machine.make_coffee('americano', ['milk', 'sugar'])
        print(f"Ordered: {fancy_coffee.get_description()}")
        print(f"Ingredients: {', '.join(fancy_coffee.get_ingredients())}")
        print(f"Cost: ${fancy_coffee.get_cost():.2f}")
        print()

        super_fancy = machine.make_coffee('espresso', ['milk', 'caramel', 'whipped_cream'])
        print(f"Ordered: {super_fancy.get_description()}")
        print(f"Ingredients: {', '.join(super_fancy.get_ingredients())}")
        print(f"Cost: ${super_fancy.get_cost():.2f}")


if __name__ == "__main__":
    CoffeeMachineDemo.run()
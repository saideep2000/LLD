from coffee_machine import CoffeeMachine

class CoffeeMachineDemo():
    @staticmethod
    def run():
        machine = CoffeeMachine()

        espresso = machine.make_coffee('espresso')

        fancy_coffee = machine.make_coffee('americano', ['milk', 'sugar'])

        super_fancy = machine.make_coffee('espresso', ['milk', 'caramel', 'whipped_cream'])



if __name__ == "__main__":
    CoffeeMachineDemo.run()
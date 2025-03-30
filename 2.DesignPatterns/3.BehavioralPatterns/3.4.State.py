# Problem Statement:
# When an object’s behavior depends on its internal state, implementing all the 
# behavior within a monolithic class often results in complex 
# conditional logic (e.g., numerous if/else or switch-case statements). 
# This not only makes the code hard to read and maintain but also violates the 
# open-closed principle—making it difficult to introduce new behaviors without modifying 
# existing code. The State Design Pattern addresses this problem by encapsulating 
# state-specific behavior into separate state classes and delegating behavior to the 
# current state. This allows the context object to change its behavior at runtime simply 
# by switching its internal state, thereby "appearing" to change its class.

# Example: Vending Machine State Pattern
# Below is an example of a vending machine that changes its behavior based on its 
# internal state. The machine has four states:

# NoCoinState: Waiting for a coin to be inserted.
# HasCoinState: A coin has been inserted and the machine is waiting for an item selection.
# SoldState: An item has been selected and is being dispensed.
# SoldOutState: The machine is empty.

# Each state encapsulates behavior corresponding to actions like inserting a coin, ejecting a coin, selecting an item, and dispensing an item.


from abc import ABC, abstractmethod

# State interface that declares methods for all actions.
class State(ABC):
    @abstractmethod
    def insert_coin(self):
        pass

    @abstractmethod
    def eject_coin(self):
        pass

    @abstractmethod
    def select_item(self):
        pass

    @abstractmethod
    def dispense(self):
        pass

# Concrete State: NoCoinState
class NoCoinState(State):
    def __init__(self, machine):
        self.machine = machine

    def insert_coin(self):
        print("Coin inserted.")
        self.machine.set_state(self.machine.has_coin_state)

    def eject_coin(self):
        print("No coin to eject.")

    def select_item(self):
        print("Insert coin first.")

    def dispense(self):
        print("Payment required.")

# Concrete State: HasCoinState
class HasCoinState(State):
    def __init__(self, machine):
        self.machine = machine

    def insert_coin(self):
        print("Coin already inserted.")

    def eject_coin(self):
        print("Coin returned.")
        self.machine.set_state(self.machine.no_coin_state)

    def select_item(self):
        print("Item selected.")
        self.machine.set_state(self.machine.sold_state)

    def dispense(self):
        print("No item dispensed.")

# Concrete State: SoldState
class SoldState(State):
    def __init__(self, machine):
        self.machine = machine

    def insert_coin(self):
        print("Please wait, dispensing in progress.")

    def eject_coin(self):
        print("Cannot eject coin, item is being dispensed.")

    def select_item(self):
        print("Item already being dispensed.")

    def dispense(self):
        self.machine.release_item()
        if self.machine.count > 0:
            self.machine.set_state(self.machine.no_coin_state)
        else:
            print("Out of items!")
            self.machine.set_state(self.machine.sold_out_state)

# Concrete State: SoldOutState
class SoldOutState(State):
    def __init__(self, machine):
        self.machine = machine

    def insert_coin(self):
        print("Machine is sold out.")

    def eject_coin(self):
        print("No coin inserted.")

    def select_item(self):
        print("Machine is sold out.")

    def dispense(self):
        print("Machine is sold out.")

# Context: VendingMachine
class VendingMachine:
    def __init__(self, count):
        self.count = count
        self.sold_out_state = SoldOutState(self)
        self.no_coin_state = NoCoinState(self)
        self.has_coin_state = HasCoinState(self)
        self.sold_state = SoldState(self)

        # Initial state depends on inventory.
        self.state = self.no_coin_state if count > 0 else self.sold_out_state

    def set_state(self, state):
        self.state = state

    def insert_coin(self):
        self.state.insert_coin()

    def eject_coin(self):
        self.state.eject_coin()

    def select_item(self):
        self.state.select_item()
        self.state.dispense()

    def release_item(self):
        if self.count > 0:
            print("An item is dispensed...")
            self.count -= 1

# Client code demonstrating the State pattern.
if __name__ == '__main__':
    # Create a vending machine with 2 items.
    machine = VendingMachine(2)

    # Scenario 1: Normal operation.
    machine.insert_coin()   # Transition from NoCoinState to HasCoinState.
    machine.select_item()   # Dispense item, transition to SoldState then back to NoCoinState.

    # Scenario 2: Insert coin and then eject coin.
    machine.insert_coin()   # Transition to HasCoinState.
    machine.eject_coin()    # Coin returned, transition back to NoCoinState.

    # Scenario 3: Dispense the last item.
    machine.insert_coin()   # Transition to HasCoinState.
    machine.select_item()   # Dispense item, transition to SoldOutState.

    # Scenario 4: Attempt operations when sold out.
    machine.insert_coin()   # Should print "Machine is sold out."

# python3 2.DesignPatterns/3.BehavioralPatterns/3.4.State.py
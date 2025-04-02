# Problem Statement
# In complex systems, multiple components (or colleagues) often need to interact with 
# one another. Direct communication between every pair of components can lead to tightly 
# coupled code and a “spaghetti” network of dependencies that is hard to modify and maintain. 
# The Mediator Design Pattern solves this problem by centralizing communication: 
# instead of colleagues referring to each other directly, they communicate only through 
# a mediator. This decouples the colleagues from one another, simplifies interactions, 
# and makes it easier to change how they cooperate.

# Example: Air Traffic Control Tower
# In an airport, airplanes (the colleagues) need to coordinate with each other to take 
# off and land. Rather than each airplane communicating directly with every other 
# airplane—which would lead to chaos—the control tower (the mediator) manages the 
# communication and enforces rules. Airplanes report their status to the control tower 
# and request permission for takeoff or landing. The control tower then informs the 
# appropriate airplanes about the status of the runway or other relevant information.

from abc import ABC, abstractmethod

# Mediator Interface
class AirTrafficControl(ABC):
    @abstractmethod
    def register_airplane(self, airplane):
        pass

    @abstractmethod
    def request_landing(self, airplane):
        pass

    @abstractmethod
    def request_takeoff(self, airplane):
        pass

# Concrete Mediator: Control Tower
class ControlTower(AirTrafficControl):
    def __init__(self):
        self.airplanes = []
        self.runway_available = True

    def register_airplane(self, airplane):
        self.airplanes.append(airplane)
        airplane.control_tower = self

    def request_landing(self, airplane):
        print(f"{airplane.name} requesting landing.")
        if self.runway_available:
            print(f"ControlTower: Runway is available. {airplane.name} is cleared to land.")
            self.runway_available = False  # runway is now in use
            # Simulate landing...
            self._clear_runway(airplane, action="landed")
        else:
            print(f"ControlTower: Runway is busy. {airplane.name} please wait.")

    def request_takeoff(self, airplane):
        print(f"{airplane.name} requesting takeoff.")
        if self.runway_available:
            print(f"ControlTower: Runway is available. {airplane.name} is cleared for takeoff.")
            self.runway_available = False  # runway is now in use
            # Simulate takeoff...
            self._clear_runway(airplane, action="took off")
        else:
            print(f"ControlTower: Runway is busy. {airplane.name} please wait.")

    def _clear_runway(self, airplane, action):
        # Simulate the process of landing/takeoff and then clear the runway.
        print(f"{airplane.name} has {action}.")
        self.runway_available = True
        print("ControlTower: Runway is now available.\n")

# Colleague: Airplane
class Airplane:
    def __init__(self, name):
        self.name = name
        self.control_tower = None  # mediator will be set during registration

    def land(self):
        if self.control_tower:
            self.control_tower.request_landing(self)
        else:
            print(f"{self.name} has no control tower assigned!")

    def takeoff(self):
        if self.control_tower:
            self.control_tower.request_takeoff(self)
        else:
            print(f"{self.name} has no control tower assigned!")

# Client code to demonstrate the Mediator pattern.
if __name__ == "__main__":
    # Create a control tower (mediator).
    tower = ControlTower()

    # Create airplanes (colleagues).
    plane1 = Airplane("Flight A123")
    plane2 = Airplane("Flight B456")
    plane3 = Airplane("Flight C789")

    # Register airplanes with the control tower.
    tower.register_airplane(plane1)
    tower.register_airplane(plane2)
    tower.register_airplane(plane3)

    # Airplanes make landing and takeoff requests.
    plane1.land()
    plane2.land()
    plane1.takeoff()
    plane3.takeoff()

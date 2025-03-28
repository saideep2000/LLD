# Problem Statement:

# In many applications, different algorithms can be applied to solve a problem, 
# but the choice of algorithm may vary based on the context or user preferences. 
# Hardcoding a specific algorithm into the client leads to a design that is difficult 
# to extend or modify. The Strategy Design Pattern addresses this problem by defining a 
# family of interchangeable algorithms, encapsulating each one in its own class. 
# The client interacts only with an abstraction (interface) for the algorithm, 
# allowing the underlying implementation to change without affecting the client. 
# This approach promotes flexibility and adheres to the open-closed principle—systems 
# remain open for extension but closed for modification.

# Example: Transportation Strategy
# Consider the problem of choosing a mode of transportation to get to the airport. 
# Several strategies exist such as driving your own car, taking a taxi, or riding a 
# shuttle. Each of these strategies calculates travel time and cost differently. 
# By using the Strategy pattern, we can encapsulate each transportation method into its 
# own class and allow the client to choose the appropriate strategy at runtime.

from abc import ABC, abstractmethod

# Strategy interface: declares a common method for all transportation strategies.
class TransportationStrategy(ABC):
    @abstractmethod
    def travel_time(self, distance: float) -> float:
        """Calculate travel time given a distance."""
        pass

    @abstractmethod
    def travel_cost(self, distance: float) -> float:
        """Calculate travel cost given a distance."""
        pass

# Concrete Strategy: Driving your own car.
class CarStrategy(TransportationStrategy):
    def travel_time(self, distance: float) -> float:
        # Assume average speed of 60 mph.
        return distance / 60

    def travel_cost(self, distance: float) -> float:
        # Cost is calculated based on fuel consumption: $0.15 per mile.
        return distance * 0.15

# Concrete Strategy: Taking a taxi.
class TaxiStrategy(TransportationStrategy):
    def travel_time(self, distance: float) -> float:
        # Assume taxi speed is similar to car.
        return distance / 60

    def travel_cost(self, distance: float) -> float:
        # Taxi cost: flat fee plus per mile charge.
        flat_fee = 3.00
        per_mile = 2.00
        return flat_fee + (distance * per_mile)

# Concrete Strategy: Taking an airport shuttle.
class ShuttleStrategy(TransportationStrategy):
    def travel_time(self, distance: float) -> float:
        # Shuttle might be slower due to stops; assume average speed of 40 mph.
        return distance / 40

    def travel_cost(self, distance: float) -> float:
        # Shuttle cost is fixed regardless of distance.
        return 15.00

# Context: The traveler who uses a transportation strategy.
class Traveler:
    def __init__(self, strategy: TransportationStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: TransportationStrategy):
        self.strategy = strategy

    def get_travel_info(self, distance: float):
        time = self.strategy.travel_time(distance)
        cost = self.strategy.travel_cost(distance)
        print(f"For a distance of {distance} miles:")
        print(f"  Estimated travel time: {time:.2f} hours")
        print(f"  Estimated travel cost: ${cost:.2f}")

# Client code demonstrating the Strategy pattern.
if __name__ == "__main__":
    distance_to_airport = 120  # miles

    # Traveler choosing different transportation strategies.
    traveler = Traveler(CarStrategy())
    print("Traveling by Car:")
    traveler.get_travel_info(distance_to_airport)
    
    print("\nTraveling by Taxi:")
    traveler.set_strategy(TaxiStrategy())
    traveler.get_travel_info(distance_to_airport)
    
    print("\nTraveling by Shuttle:")
    traveler.set_strategy(ShuttleStrategy())
    traveler.get_travel_info(distance_to_airport)


# python3 2.DesignPatterns/3.BehavioralPatterns/3.2.Strategy.py
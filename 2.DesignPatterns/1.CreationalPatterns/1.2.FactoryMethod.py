# The Factory Method Pattern is a creational design pattern that provides an interface 
# for creating objects without specifying their exact class.

# Encapsulates Object Creation → Avoids new keyword everywhere.
# Increases Flexibility → Can create different objects dynamically.
# Follows Open-Closed Principle → Easy to extend without modifying existing code.
# Abstracts Complex Object Creation → Useful when initialization is complex.

# Let's implement a factory method for creating different types of vehicles.



from abc import ABC, abstractmethod

# Step 1: Define the Product Interface (Abstract Class)
class Vehicle(ABC):
    @abstractmethod
    def create(self):
        pass

# Step 2: Create Concrete Products
class Car(Vehicle):
    def create(self):
        return "Car is created"

class Bike(Vehicle):
    def create(self):
        return "Bike is created"

# Step 3: Define the Creator (Factory) Interface
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass

# Step 4: Implement Concrete Factories
class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()

class BikeFactory(VehicleFactory):
    def create_vehicle(self):
        return Bike()

# Step 5: Using the Factory Method
def client_code(factory: VehicleFactory):
    vehicle = factory.create_vehicle()
    print(vehicle.create())

# Test Factory Method
car_factory = CarFactory()
bike_factory = BikeFactory()

client_code(car_factory)  # Output: Car is created
client_code(bike_factory)  # Output: Bike is created

# Here the client doesn't know how exactly the object is created.


# When to use:
# When object creation logic is complex.
# When you need different types of objects based on conditions.
# When you want to follow SOLID principles (Open-Closed Principle).
# When the exact class of the object is unknown at compile-time.
# When you want to separate object creation from object usage.
# When creating objects involves some logic (e.g., parameter-based selection, caching, etc.).

# python3 2.DesignPatterns/1.CreationalPatterns/1.2.FactoryMethod.py
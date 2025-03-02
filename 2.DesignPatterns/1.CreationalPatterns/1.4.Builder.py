# The Builder Pattern is a creational design pattern used to construct complex objects 
# step-by-step. It allows us to create different representations of an object using 
# the same construction process.

# When an object has many optional parameters (e.g., a car with GPS, sunroof, autopilot, etc.).
# When object creation becomes complex due to multiple configurations.
# When you want to make the object immutable (constructed step by step but final after creation).
# When you need better code readability instead of long constructor calls.

# Builder Pattern - Question
# In a software system, customers need a way to build and configure cars dynamically based on their preferences.
# Each car has different configurable attributes, such as engine type, color, sunroof, and autopilot.

# To maintain scalability and flexibility, the system should use the Builder Pattern to allow step-by-step car construction while keeping the client code clean and avoiding long constructor parameter lists.


from abc import ABC, abstractmethod

# Step 1: Car Class (Product)
class Car:
    def __init__(self):
        self.type = None
        self.engine = None
        self.color = None
        self.sunroof = False
        self.autopilot = False

    def __str__(self):
        return (f"Car: {self.type}, Engine: {self.engine}, Color: {self.color}, "
                f"Sunroof: {self.sunroof}, Autopilot: {self.autopilot}")

# Step 2: Abstract Builder
class CarBuilder(ABC):
    @abstractmethod
    def set_type(self, car_type):
        pass

    @abstractmethod
    def set_engine(self, engine):
        pass

    @abstractmethod
    def set_color(self, color):
        pass

    @abstractmethod
    def set_sunroof(self, sunroof):
        pass

    @abstractmethod
    def set_autopilot(self, autopilot):
        pass

    @abstractmethod
    def build(self):
        pass

# Step 3: Concrete Builder
class CarBuilderBase(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_type(self, car_type):
        self.car.type = car_type
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def set_sunroof(self, sunroof):
        self.car.sunroof = sunroof
        return self

    def set_autopilot(self, autopilot):
        self.car.autopilot = autopilot
        return self

    def build(self):
        return self.car

# Step 4: Director Class
class CarDirector:
    def __init__(self, builder: CarBuilderBase):
        self.builder = builder

    def build_sports_car(self):
        return (self.builder
                .set_type("Sports Car")
                .set_engine("V8")
                .set_color("White")
                .set_sunroof(True)
                .set_autopilot(True)
                .build())

    def build_economy_car(self):
        return (self.builder
                .set_type("Economy Car")
                .set_engine("Electric")
                .set_color("Blue")
                .set_sunroof(False)
                .set_autopilot(False)
                .build())

# Step 5: Client Code
if __name__ == "__main__":
    # Building a Sports Car
    sports_car_builder = CarBuilderBase()
    sports_car_director = CarDirector(sports_car_builder)
    sports_car = sports_car_director.build_sports_car()
    
    # Building an Economy Car
    economy_car_builder = CarBuilderBase()
    economy_car_director = CarDirector(economy_car_builder)
    economy_car = economy_car_director.build_economy_car()

    print(sports_car)  # Display the Sports Car
    print(economy_car)  # Display the Economy Car



# Here if you want an optional features then you should remove the director.
# Instead you can make the things deafult False so that if the client calls for it 
# it will build with it included or else it's default not included.

# python3 2.DesignPatterns/1.CreationalPatterns/1.4.Builder.py
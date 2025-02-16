# The Builder Pattern is a creational design pattern used to construct complex objects 
# step-by-step. It allows us to create different representations of an object using 
# the same construction process.

# When an object has many optional parameters (e.g., a car with GPS, sunroof, autopilot, etc.).
# When object creation becomes complex due to multiple configurations.
# When you want to make the object immutable (constructed step by step but final after creation).
# When you need better code readability instead of long constructor calls.

# Step 1: Define the Product (Complex Object)
class Car:
    def __init__(self):
        self.model = None
        self.engine = None
        self.color = None
        self.sunroof = False
        self.autopilot = False

    def __str__(self):
        return f"Car: {self.model}, Engine: {self.engine}, Color: {self.color}, Sunroof: {self.sunroof}, Autopilot: {self.autopilot}"

# Step 2: Define the Abstract Builder Interface
class CarBuilder:
    def set_model(self, model):
        pass

    def set_engine(self, engine):
        pass

    def set_color(self, color):
        pass

    def add_sunroof(self):
        pass

    def add_autopilot(self):
        pass

    def build(self):
        pass

# Step 3: Implement the Concrete Builder
class ConcreteCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_model(self, model):
        self.car.model = model
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def add_sunroof(self):
        self.car.sunroof = True
        return self

    def add_autopilot(self):
        self.car.autopilot = True
        return self

    def build(self):
        return self.car  # Returns the final Car object

# Step 4: Director (Optional - Manages Construction)
class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_sports_car(self):
        return (self.builder
                .set_model("Sports Car")
                .set_engine("V8 Turbo")
                .set_color("Red")
                .add_sunroof()
                .add_autopilot()
                .build())

    def build_economy_car(self):
        return (self.builder
                .set_model("Economy Car")
                .set_engine("Electric")
                .set_color("Blue")
                .build())

# Step 5: Using the Builder Pattern
builder = ConcreteCarBuilder()
director = CarDirector(builder)

sports_car = director.build_sports_car()
economy_car = director.build_economy_car()

print(sports_car)  # Output: Car: Sports Car, Engine: V8 Turbo, Color: Red, Sunroof: True, Autopilot: True
print(economy_car)  # Output: Car: Economy Car, Engine: Electric, Color: Blue, Sunroof: False, Autopilot: False


# Here if you want an optional features then you should remove the director.
# Instead you can make the things deafult False so that if the client calls for it 
# it will build with it included or else it's default not included.

# python3 2.DesignPatterns/1.CreationalPatterns/1.4.Builder.py
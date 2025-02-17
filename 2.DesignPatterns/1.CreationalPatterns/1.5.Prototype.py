# The Prototype Pattern is a creational design pattern that lets you clone 
# existing objects instead of creating new instances from scratch. 

# This is useful when object creation is expensive or when we want to preserve 
# object state.

# Why?
# When object creation is costly, and you need to create multiple similar objects efficiently.
# When an object has complex initialization and you want to avoid redundant computations.
# When you need deep copies or shallow copies of an object.
# When objects have many configurations, and you want to reuse a base template.


import copy

# Step 1: Define the Prototype (Base Class)
class Car:
    def __init__(self, model, engine, color, features=None):
        self.model = model
        self.engine = engine
        self.color = color
        self.features = features if features else []

    def add_feature(self, feature):
        self.features.append(feature)

    def clone(self):
        return copy.deepcopy(self)  # Creates a deep copy of the object

    def __str__(self):
        return f"Car: {self.model}, Engine: {self.engine}, Color: {self.color}, Features: {self.features}"

# Step 2: Using the Prototype Pattern
original_car = Car("Sedan", "V6", "Black", ["Sunroof"])
print("Original Car:", original_car)

# Cloning the Car
cloned_car = original_car.clone()
cloned_car.add_feature("Autopilot")  # Modify cloned object

print("Cloned Car:", cloned_car)  # New feature added to cloned car
print("Original Car after cloning:", original_car)  # Original remains unchanged

# python3 2.DesignPatterns/1.CreationalPatterns/1.5.Prototype.py

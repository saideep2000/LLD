# Singleton is a creational design pattern that ensures only one instance of a class exists 
# and provides a global point of access to it.

# Key Features:
# Single Instance – Ensures that only one object of the class is created.
# Global Access – Provides a way to access that instance.
# Controlled Instantiation – Prevents multiple object creation.

# Singleton Pattern - Question
# In a software system, certain classes must have only one instance throughout the entire application.
# For example, classes like Database Connection, Configuration Manager, and Logging System should follow 
# the Singleton Pattern to prevent multiple instances from being created.

# To maintain global access and ensure only one instance exists, implement the Singleton Pattern where a 
# class restricts the instantiation of itself to a single object.

class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance

obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2) # Output: True (Both are same instance)



# cls is a class-level parameter that refers to the class itself when working with class methods or __new__()

# super(Singleton, cls).__new__(cls) calls object.__new__(cls), which allocates memory for a new instance.

# Here the parent for any class is object, so if you call super at an object you will get the object.
    
# _instance stores this single instance so that future calls return the same object.

# The check if cls._instance is None: ensures only one instance is created.

# Run:
# Be at root level and run this:
# python3 2.DesignPatterns/1.CreationalPatterns/1.1.Singleton.py
# Output: True (Both are same instance)
# The Abstract Factory Pattern is a creational design pattern that provides an 
# interface for creating families of related objects without specifying their 
# concrete classes.
    
# Why?
# When you need to create related objects together (e.g., a UI theme with matching buttons and checkboxes).
# When you want to avoid hard-coded class names and decouple object creation from usage.
# When different products share a common interface and belong to a family.

# from abc import ABC, abstractmethod

# # Step 1: Abstract Products
# class Button(ABC):
#     @abstractmethod
#     def click(self):
#         pass

# class Checkbox(ABC):
#     @abstractmethod
#     def check(self):
#         pass

# # Step 2: Concrete Products
# class WindowsButton(Button):
#     def click(self):
#         return "Windows button clicked"

# class MacButton(Button):
#     def click(self):
#         return "Mac button clicked"

# class WindowsCheckbox(Checkbox):
#     def check(self):
#         return "Windows checkbox checked"

# class MacCheckbox(Checkbox):
#     def check(self):
#         return "Mac checkbox checked"

# # Step 3: Abstract Factory
# class UIFactory(ABC):
#     @abstractmethod
#     def create_button(self):
#         pass

#     @abstractmethod
#     def create_checkbox(self):
#         pass

# # Step 4: Concrete Factories
# class WindowsFactory(UIFactory):
#     def create_button(self):
#         return WindowsButton()

#     def create_checkbox(self):
#         return WindowsCheckbox()

# class MacFactory(UIFactory):
#     def create_button(self):
#         return MacButton()

#     def create_checkbox(self):
#         return MacCheckbox()

# # Step 5: Client Code
# def create_ui(factory: UIFactory):
#     button = factory.create_button()
#     checkbox = factory.create_checkbox()

#     print(button.click())
#     print(checkbox.check())

# # Step 6: Usage
# print("Windows UI:")
# create_ui(WindowsFactory())  # Produces Windows-compatible UI elements

# print("\nMac UI:")
# create_ui(MacFactory())  # Produces Mac-compatible UI elements

# With the factory method we will only able to create one type of object.
# Here we can make family of related objects together.





# ### **Abstract Factory Pattern - Question**  

# In a software system, notifications need to be sent through multiple channels such as **Email, SMS, and Push Notifications**.  
# Each notification type has a different implementation for sending messages and storing logs, but the core operations remain the same.  

# To maintain **scalability** and **loose coupling**, the system should not depend on concrete implementations of notification types.  
# Instead, it should dynamically create the required notification object at runtime without modifying the existing client code.  

# #### **Requirements:**  
# 1. Define a common interface for all notification types to enforce the structure.  
# 2. Implement the **Abstract Factory Pattern** to create notification objects dynamically.  
# 3. Ensure that adding a new notification type does not require modifying the existing client code.  

# #### **Implement the Abstract Factory Pattern**  
# Provide the necessary **abstract classes, concrete implementations, and a client function** that utilizes the factories to 
# send notifications and store logs efficiently.



# from abc import ABC, abstractmethod

# # Step 1: Abstract Product Interface
# class System(ABC):
#     @abstractmethod
#     def SendNotification(self, message: str):
#         pass

#     @abstractmethod
#     def Store(self, message: str):
#         pass

# # Step 2: Concrete Product Implementations
# class EmailNotification(System):
#     def SendNotification(self, message: str):
#         print(f"I'm an Email. Please email me at {message}")

#     def Store(self, message: str):
#         print(f"This is getting stored in the log pages of email at {message}")

# class SmsNotification(System):
#     def SendNotification(self, message: str):
#         print(f"I'm an SMS. Please text me at {message}")

#     def Store(self, message: str):
#         print(f"This is getting stored in the log pages of SMS at {message}")

# class PushNotification(System):
#     def SendNotification(self, message: str):
#         print(f"I'm a Push Notification. Please check me at {message}")

#     def Store(self, message: str):
#         print(f"This is getting stored in the log pages of push notifications at {message}")

# # Step 3: Abstract Factory Interface
# class SystemFactory(ABC):
#     @abstractmethod
#     def MakeNotification(self) -> System:
#         pass

# # Step 4: Concrete Factories
# class EmailNotificationFactory(SystemFactory):
#     def MakeNotification(self):
#         return EmailNotification()
    
# class SmsNotificationFactory(SystemFactory):
#     def MakeNotification(self):
#         return SmsNotification()
    
# class PushNotificationFactory(SystemFactory):
#     def MakeNotification(self):
#         return PushNotification()

# # Step 5: Client Code
# def hit(factory: SystemFactory, message: str):
#     now = factory.MakeNotification()
#     now.SendNotification(message)
#     now.Store(message)

# # Step 6: Testing the Abstract Factory Pattern
# hit(EmailNotificationFactory(), "Hi, this is an email")
# hit(SmsNotificationFactory(), "Hi, this is an SMS")
# hit(PushNotificationFactory(), "Hi, this is a push notification")

# Example 2:

from abc import ABC, abstractmethod
from typing import Type

# let's create the abstract class of pet
class Pet(ABC):
    def __init__(self, name : str):
        self.name = name
    
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

# Dog class which will inhert the Pet
class Dog(Pet):
    def speak(self):
        print(f"Bow Bow...")
    
    def __str__(self):
        return f"Hi I'm a Dog and my name is {self.name}"

# Cat class which will inhert the Pet
class Cat(Pet):
    def speak(self):
        print(f"Muew Muew...")
    
    def __str__(self):
        return f"Hi I'm a Cat and my name is {self.name}"
        
class PetShop():
    def __init__(self, animal_factory : Type[Pet]):
        self.pet_factory = animal_factory
    def buy_pet(self, name) -> Pet:
        return self.pet_factory(name)

# client code

pet_shop = PetShop(Dog)
my_dog_pet_shop = pet_shop.buy_pet("Juli")
print(my_dog_pet_shop)
my_dog_pet_shop.speak()


# Use the Abstract Factory Pattern when: 
# You need to create groups of related objects (e.g., GUI elements for different OS).
# You want to ensure compatibility between created objects.
# You want to decouple the client from specific classes.
# You need a scalable, extensible solution that follows Open-Closed Principle.

# Here the concrete factory will provide the actually logic to create products.

# python3 2.DesignPatterns/1.CreationalPatterns/1.3.AbstractFactory.py
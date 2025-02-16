# The Abstract Factory Pattern is a creational design pattern that provides an 
# interface for creating families of related objects without specifying their 
# concrete classes.
    
# Why?
# When you need to create related objects together (e.g., a UI theme with matching buttons and checkboxes).
# When you want to avoid hard-coded class names and decouple object creation from usage.
# When different products share a common interface and belong to a family.

from abc import ABC, abstractmethod

# Step 1: Abstract Products
class Button(ABC):
    @abstractmethod
    def click(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass

# Step 2: Concrete Products
class WindowsButton(Button):
    def click(self):
        return "Windows button clicked"

class MacButton(Button):
    def click(self):
        return "Mac button clicked"

class WindowsCheckbox(Checkbox):
    def check(self):
        return "Windows checkbox checked"

class MacCheckbox(Checkbox):
    def check(self):
        return "Mac checkbox checked"

# Step 3: Abstract Factory
class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

# Step 4: Concrete Factories
class WindowsFactory(UIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacFactory(UIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

# Step 5: Client Code
def create_ui(factory: UIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(button.click())
    print(checkbox.check())

# Step 6: Usage
print("Windows UI:")
create_ui(WindowsFactory())  # Produces Windows-compatible UI elements

print("\nMac UI:")
create_ui(MacFactory())  # Produces Mac-compatible UI elements




# Use the Abstract Factory Pattern when: 
# You need to create groups of related objects (e.g., GUI elements for different OS).
# You want to ensure compatibility between created objects.
# You want to decouple the client from specific classes.
# You need a scalable, extensible solution that follows Open-Closed Principle.

# python3 2.DesignPatterns/1.CreationalPatterns/1.3.AbstractFactory.py
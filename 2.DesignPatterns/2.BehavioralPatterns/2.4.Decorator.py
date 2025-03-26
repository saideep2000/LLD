# Attach additional responsibilities to an object dynamically. 
# Decorators provide a flexible alternative to subclassing for extending functionality.
# Client-specified embellishment of a core object by recursively wrapping it.
# Wrapping a gift, putting it in a box, and wrapping the box.

# You want to add behavior or state to individual objects at run-time. 
# Inheritance is not feasible because it is static and applies to an entire class.

# Problem Statement:

# You have a core object that implements a specific functionality (e.g., a basic window or a data stream). 
# However, you want to add additional behavior (like borders, scrollbars, or compression) 
# dynamically, at runtime, without modifying the core object's code or creating a multitude of subclasses. '
# 'Inheritance alone isn't sufficient or flexible enough because it statically defines behavior for the whole class. 
# The Decorator pattern solves this by wrapping the core object with one or more decorator objects that add 
# the desired responsibilities while keeping the interface consistent for the client.

# Below is a Python example illustrating the Decorator Design Pattern using a window widget 
# that can be dynamically decorated with additional features like a border and a scrollbar.

from abc import ABC, abstractmethod

# The common interface for core objects and decorators.
class Widget(ABC):
    @abstractmethod
    def draw(self):
        pass

# The core object that provides basic functionality.
class Window(Widget):
    def draw(self):
        print("Drawing Window")

# The base Decorator that wraps a Widget.
class WidgetDecorator(Widget):
    def __init__(self, widget: Widget):
        self.widget = widget

    def draw(self):
        # Delegates the draw call to the wrapped widget.
        self.widget.draw()

# A concrete decorator that adds a border.
class BorderDecorator(WidgetDecorator):
    def draw(self):
        super().draw()          # Draw the original widget.
        self.draw_border()      # Add border-specific behavior.

    def draw_border(self):
        print("Drawing border around widget")

# A concrete decorator that adds a scrollbar.
class ScrollBarDecorator(WidgetDecorator):
    def draw(self):
        super().draw()             # Draw the original widget.
        self.draw_scrollbar()      # Add scrollbar-specific behavior.

    def draw_scrollbar(self):
        print("Drawing scrollbar for widget")

# Client code demonstrating dynamic decoration.
if __name__ == '__main__':
    # Create a basic window.
    simple_window = Window()
    
    # Wrap the window with decorators to add additional behavior.
    # For example, first add a scrollbar, then a border.
    decorated_window = BorderDecorator(ScrollBarDecorator(simple_window))
    
    # Client calls draw() on the decorated window.
    decorated_window.draw()


# python3 2.DesignPatterns/2.BehavioralPatterns/2.4.Decorator.py
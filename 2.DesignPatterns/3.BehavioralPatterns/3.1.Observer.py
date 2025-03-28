# Problem Statement:

# In many systems, data or state changes need to be communicated to multiple components—such 
# as different user interfaces, logging mechanisms, or analytics modules—without tightly 
# coupling these components to the data source. A monolithic design forces the data source 
# to have knowledge of all its dependents, making the system inflexible and hard to maintain.
# The Observer pattern solves this problem by defining a one-to-many relationship between a 
# subject (which holds the state) and its observers (which depend on that state). 
# When the subject’s state changes, it automatically notifies all registered observers, 
# which can then update themselves accordingly. This decouples the subject from its 
# dependents, making the system easier to extend and maintain.

# In this example, we model a stock price tracker where the stock (subject) notifies 
# registered observers whenever its price changes. Observers could represent different 
# components such as a GUI display, a logging system, or an alert mechanism.

from abc import ABC, abstractmethod

# Subject: Defines the interface for managing observers and notifying them of changes.
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self._price = price
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price != self._price:
            self._price = new_price
            print(f"\nStock: {self.symbol} price updated to {self._price}")
            self.notify_observers()


# Observer: Defines the interface for objects that should be notified of subject changes.
class StockObserver(ABC):
    @abstractmethod
    def update(self, stock: Stock):
        pass


# Concrete Observer 1: Displays the stock price.
class PriceDisplay(StockObserver):
    def update(self, stock: Stock):
        print(f"PriceDisplay: The current price of {stock.symbol} is {stock.price}")


# Concrete Observer 2: Logs the stock price change.
class PriceLogger(StockObserver):
    def update(self, stock: Stock):
        print(f"PriceLogger: Logged new price for {stock.symbol}: {stock.price}")


# Client code demonstrating the Observer pattern.
if __name__ == "__main__":
    # Create a stock subject.
    apple_stock = Stock("AAPL", 150)

    # Create observers.
    display = PriceDisplay()
    logger = PriceLogger()

    # Register observers with the stock.
    apple_stock.add_observer(display)
    apple_stock.add_observer(logger)

    # Simulate price changes.
    apple_stock.price = 155  # Notifies display and logger.
    apple_stock.price = 160  # Notifies display and logger.


# python3 2.DesignPatterns/3.BehavioralPatterns/3.1.Observer.py


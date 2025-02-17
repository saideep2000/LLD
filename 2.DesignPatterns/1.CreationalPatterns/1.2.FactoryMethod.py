# The Factory Method Pattern is a creational design pattern that provides an interface 
# for creating objects without specifying their exact class.

# Encapsulates Object Creation → Avoids new keyword everywhere.
# Increases Flexibility → Can create different objects dynamically.
# Follows Open-Closed Principle → Easy to extend without modifying existing code.
# Abstracts Complex Object Creation → Useful when initialization is complex.

from abc import ABC, abstractmethod

# This is abstract class and other will extends this.
class NotificationSystem(ABC):
    @abstractmethod
    def send(self, message):
        pass


class email(NotificationSystem):
    def send(self, message):
        print(f"Sending {message} through the email notification")
    
class sms(NotificationSystem):
    def send(self, message):
        print(f"Sending {message} through the sms notification")

class push(NotificationSystem):
    def send(self, message):
        print(f"Sending {message} through the push notification")

class NotificationFactory(ABC):
    @abstractmethod
    def MakeNotification(self):
        pass

class EmailFactory(NotificationFactory):
    def MakeNotification(self):
        return email()

class SmsFactory(NotificationFactory):
    def MakeNotification(self):
        return sms()

class PushFactory(NotificationFactory):
    def MakeNotification(self):
        return push()


# client
def send_notification(factory : NotificationFactory, message : str):
    now = factory.MakeNotification()
    now.send(message)

send_notification(EmailFactory(), "hi email")
send_notification(SmsFactory(), "hi sms")
send_notification(PushFactory(), "hi push")

# Here the client doesn't know how exactly the object is created.

# even if the new notification type comes, client will just have to use the new factory but other than that nothing will change.

# When to use:
# When object creation logic is complex.
# When you need different types of objects based on conditions.
# When you want to follow SOLID principles (Open-Closed Principle).
# When the exact class of the object is unknown at compile-time.
# When you want to separate object creation from object usage.
# When creating objects involves some logic (e.g., parameter-based selection, caching, etc.).

# python3 2.DesignPatterns/1.CreationalPatterns/1.2.FactoryMethod.py
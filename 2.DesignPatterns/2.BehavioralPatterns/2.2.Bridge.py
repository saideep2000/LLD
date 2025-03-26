# The Bridge Pattern is a structural design pattern that helps decouple abstraction from 
# implementation so they can evolve independently.

# It is useful when we have multiple variations of an abstraction that can be 
# implemented in different ways.

# When you have multiple dimensions of change (e.g., a shape can have different rendering styles).
# When you want to decouple high-level logic (abstraction) from low-level implementation.
# When you need better maintainability and scalability of code.
# When you want to avoid inheritance explosion (too many subclasses).

# Bridge makes them work before they are designed.
# Bridge is designed up-front to let the abstraction and the implementation vary idependently.


# Problem Statement :


# BEFORE: Coupled Inheritance, class explosion, tight coupling

# class RoundRobinWindowsScheduler:
#     def schedule(self):
#         print("Round Robin Scheduler on Windows")

# class RoundRobinLinuxScheduler:
#     def schedule(self):
#         print("Round Robin Scheduler on Linux")

# class PriorityWindowsScheduler:
#     def schedule(self):
#         print("Priority Scheduler on Windows")

# class PriorityLinuxScheduler:
#     def schedule(self):
#         print("Priority Scheduler on Linux")

# # Client code:
# def before_example():
#     # Creating a list of schedulers for demonstration.
#     schedulers = [
#         RoundRobinWindowsScheduler(),
#         RoundRobinLinuxScheduler(),
#         PriorityWindowsScheduler(),
#         PriorityLinuxScheduler(),
#     ]
#     for scheduler in schedulers:
#         scheduler.schedule()

# if __name__ == '__main__':
#     print("Before Bridge Pattern:")
#     before_example()

# using bridge pattern:

from abc import ABC, abstractmethod

# Implementation Interface and Concrete Platform Classes
class Platform(ABC):
    @abstractmethod
    def schedule_task(self, scheduler_type: str):
        pass

class WindowsPlatform(Platform):
    def schedule_task(self, scheduler_type: str):
        print(f"{scheduler_type} Scheduler on Windows")

class LinuxPlatform(Platform):
    def schedule_task(self, scheduler_type: str):
        print(f"{scheduler_type} Scheduler on Linux")

# Abstraction and its Derived Classes (Scheduler Hierarchy)
class Scheduler(ABC):
    def __init__(self, platform: Platform):
        self.platform = platform

    @abstractmethod
    def schedule(self):
        pass

class RoundRobinScheduler(Scheduler):
    def schedule(self):
        # Delegates scheduling to the platform implementation.
        self.platform.schedule_task("Round Robin")

class PriorityScheduler(Scheduler):
    def schedule(self):
        # Delegates scheduling to the platform implementation.
        self.platform.schedule_task("Priority")

# Client code:
def after_example():
    # Create platform instances.
    windows = WindowsPlatform()
    linux = LinuxPlatform()
    
    # Create scheduler objects by combining scheduler type with a platform.
    schedulers = [
        RoundRobinScheduler(windows),
        RoundRobinScheduler(linux),
        PriorityScheduler(windows),
        PriorityScheduler(linux),
    ]
    for scheduler in schedulers:
        scheduler.schedule()

if __name__ == '__main__':
    print("\nAfter Bridge Pattern:")
    after_example()

# Benefits:

# Decoupling: The scheduler abstraction and platform implementation vary independently.

# Extensibility: Adding a new scheduler type or platform requires only one additional 
# class in the respective hierarchy rather than redefining every combination.

# Maintainability: Changes in platform-specific behavior affect only the platform classes, 
# and scheduler strategies remain independent.

# The Bridge pattern splits the problem into two orthogonal hierarchies—one for 
# scheduling strategies (e.g., RoundRobinScheduler, PriorityScheduler) and one for 
# platforms (e.g., WindowsPlatform, LinuxPlatform). The Scheduler abstraction holds a 
# reference to a Platform instance and delegates platform-specific scheduling, which 
# significantly reduces class explosion and improves flexibility.


# python3 2.DesignPatterns/2.BehavioralPatterns/2.2.Bridge.py
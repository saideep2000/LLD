# Problem Statement
# In many applications, a request for an operation needs to be decoupled from the 
# object that performs the operation. This is especially useful when you want to 
# parameterize clients with different actions, queue or log requests, or support 
# undoable operations. Instead of invoking a method directly on a receiver, 
# the request is encapsulated as an object. This allows the system to treat all 
# requests uniformly, store them, and execute them at a later time without the sender 
# needing to know the details of the operation or the receiver. The Command Design Pattern 
# provides this level of indirection by encapsulating a request as an object.

# Example: Remote Control for a Light
# In this example, we simulate a remote control system for a light. 
# The light (receiver) can be turned on or off, but the remote control (invoker) 
# doesn't call these methods directly. Instead, it works with command objects that 
# encapsulate the request details. Each command implements a common interface, so the 
# remote control can execute them without needing to know the specifics of what each 
# command does.'


from abc import ABC, abstractmethod

# The Command interface, which declares the execute method.
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Receiver: the Light that can be turned on or off.
class Light:
    def on(self):
        print("Light is ON.")

    def off(self):
        print("Light is OFF.")

# Concrete Command to turn the light on.
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

# Concrete Command to turn the light off.
class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

# Invoker: the RemoteControl that holds and executes commands.
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()
        else:
            print("No command set.")

# Client code demonstrating the Command pattern.
if __name__ == "__main__":
    # Create the receiver.
    living_room_light = Light()
    
    # Create command objects for turning the light on and off.
    light_on_command = LightOnCommand(living_room_light)
    light_off_command = LightOffCommand(living_room_light)

    # Create the invoker.
    remote_control = RemoteControl()

    # Set the command to turn the light on and execute it.
    remote_control.set_command(light_on_command)
    remote_control.press_button()  # Output: Light is ON.

    # Set the command to turn the light off and execute it.
    remote_control.set_command(light_off_command)
    remote_control.press_button()  # Output: Light is OFF.


# The Command pattern is flexible because it transforms method calls into objects. 
# This transformation enables you to manage, extend, and manipulate operations in ways 
# that wouldn’t be possible if the client directly invoked methods on the receiver. 
# The benefits of queuing, undo/redo, macro commands, logging, and dynamic behavior 
# adjustment all stem from this fundamental encapsulation of a request as an object.


# python3 2.DesignPatterns/3.BehavioralPatterns/3.3.Command.py
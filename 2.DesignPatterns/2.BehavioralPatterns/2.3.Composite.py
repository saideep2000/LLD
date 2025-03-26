# The Composite Pattern is a structural design pattern that treats 
# individual objects and compositions uniformly.

# Problem Statement:

# In a file system, you have files (which are individual elements) and 
# directories (which can contain files or other directories). 
# Without a uniform approach, the client would have to check if an item is a 
# file or a directory before processing it, making the code more complex and less scalable.

# The Composite pattern solves this problem by defining a common interface for both primitive and composite objects, so that clients can treat them uniformly.

from abc import ABC, abstractmethod

# Component: Defines the common interface for both leaf and composite.
class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent: int = 0):
        pass

# Leaf: Represents a primitive element in the composition.
class File(FileSystemComponent):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def display(self, indent: int = 0):
        print(" " * indent + f"File: {self.name} (Size: {self.size} bytes)")

# Composite: Represents a complex element that may have children.
class Directory(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def display(self, indent: int = 0):
        print(" " * indent + f"Directory: {self.name}")
        for child in self.children:
            child.display(indent + 2)

# Client code to demonstrate the composite structure
if __name__ == '__main__':
    # Create files
    file1 = File("file1.txt", 100)
    file2 = File("file2.txt", 200)
    file3 = File("file3.txt", 300)

    # Create directories and compose them
    root_directory = Directory("root")
    sub_directory = Directory("subdir")

    sub_directory.add(file3)
    root_directory.add(file1)
    root_directory.add(file2)
    root_directory.add(sub_directory)

    # Display the whole file system structure
    root_directory.display()


# Composite and Decorator have similar structure diagrams, reflecting the fact 
# that both rely on recursive composition to organize an open-ended number of objects.
# Composite can be traversed with Iterator. Visitor can apply an operation over a Composite. Composite could use Chain of Responsibility to let components access global properties through their parent. It could also use Decorator to override these properties on parts of the composition. It could use Observer to tie one object structure to another and State to let a component change its behavior as its state changes.
# Composite can let you compose a Mediator out of smaller pieces through recursive composition.
# Decorator is designed to let you add responsibilities to objects without subclassing. 
# Composite's focus is not on embellishment but on representation. 
# These intents are distinct but complementary. 
# Consequently, Composite and Decorator are often used in concert.


# python3 2.DesignPatterns/2.BehavioralPatterns/2.3.Composite.py
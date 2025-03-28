
# Problem Statement:

# In many systems, certain objects are expensive to create, either due to heavy resource 
# usage, complex initialization, or because they reside remotely. Instantiating these objects
# upfront can lead to performance degradation and unnecessary memory usage, especially when 
# the object might not be needed immediately—or even at all. The Proxy Design Pattern 
# addresses this by providing a surrogate (or placeholder) that controls access to the real 
# object. The proxy defers the creation of the expensive object until it is actually 
# required (virtual proxy), and then delegates client requests to it.


# onsider a scenario where you have an object that is costly to initialize 
# (e.g., a high-resolution image or a resource-intensive computation module).The proxy delays 
# the instantiation of this expensive object until the client actually needs to call its methods.


import time

# The RealSubject: An expensive object to create.
class ExpensiveObject:
    def __init__(self):
        print("ExpensiveObject: Initializing... (this may take some time)")
        time.sleep(2)  # Simulate expensive initialization.
        print("ExpensiveObject: Initialization complete.")

    def process(self):
        print("ExpensiveObject: Processing request.")

# The Proxy: Controls access to the ExpensiveObject.
class ExpensiveObjectProxy:
    def __init__(self):
        self._real_object = None

    def process(self):
        # Instantiate the real object on first use.
        if self._real_object is None:
            print("ExpensiveObjectProxy: Creating the expensive object now...")
            self._real_object = ExpensiveObject()
        # Delegate the call to the real object.
        self._real_object.process()

# Client code using the proxy.
if __name__ == '__main__':
    print("Proxy Pattern Demo")
    proxy = ExpensiveObjectProxy()

    print("\nFirst call to process()")
    proxy.process()  # Triggers creation of ExpensiveObject, then processes the request.

    print("\nSecond call to process()")
    proxy.process()  # Uses the already created ExpensiveObject to process the request.



# python3 2.DesignPatterns/2.StructuralPatterns/2.1.Adapter.py
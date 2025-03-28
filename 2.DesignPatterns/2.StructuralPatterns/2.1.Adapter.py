# The Adapter Pattern is a structural design pattern that allows two 
# incompatible interfaces to work together. It acts as a bridge between existing 
# and new code, enabling interoperability without modifying the original classes.

# Why?
# When you have legacy code that doesn’t match a new interface.
# When two systems must work together but have different method names or structures.
# When you want to reuse existing functionality without modifying the source code.
# When you're integrating third-party libraries that don’t match your expected interface.

# Adapter makes things work after they're designed.
# Adapter provides a different interface to it's subjects.
# Adapter is meant to change the interface of an existing object.
# Adapter reuses an old interface, it makes two existing interfaces work together.

# Note:
# Here as we know in Python, we typically implement interfaces implicitly 
# via method signatures and duck typing rather than declaring explicit interfaces like in Java
# In the provided code, the two classes represent different interfaces conceptually

# Problem Statement: 
# we have a legacy component—a rectangle whose display method expects parameters as 
# (x, y, width, height)—but the client wants to work with rectangles defined by the 
# coordinates of the upper-left and lower-right corners. The adapter converts the 
# client's (x1, y1, x2, y2) into the parameters expected by the legacy component.

class LegacyRectangle:
    def display(self, x, y, width, height):
        print(f"LegacyRectangle: Drawing rectangle at ({x}, {y}) with width {width} and height {height}")

class RectangleAdapter:
    def __init__(self, legacy_rectangle):
        self.legacy_rectangle = legacy_rectangle

    def display(self, x1, y1, x2, y2):
        x = x1
        y = y1
        width = x2 - x1
        height = y2 - y1
        self.legacy_rectangle.display(x, y, width, height)

# Client code:
if __name__ == "__main__":
    legacy = LegacyRectangle()
    adapter = RectangleAdapter(legacy)
    
    # The client wants to draw a rectangle using two corners:
    # (10, 20) as the upper-left and (110, 220) as the lower-right.
    adapter.display(10, 20, 110, 220)


# Example 2:

# # Step 1: Adaptee (Old Logging System - File Logger)
# class FileLogger:
#     def log_message(self, message):
#         return f"Log written to file: {message}"

# # Step 2: Target Interface (New Logging System - Cloud Logger)
# class CloudLogger:
#     def write_log(self, message):
#         return f"Log sent to cloud: {message}"

# # Step 3: Adapter (Allows Old Code to Use the New Cloud Logger)
# class LoggingAdapter(FileLogger):
#     def __init__(self, cloud_logger):
#         self.cloud_logger = cloud_logger  # Takes an instance of CloudLogger

#     def log_message(self, message):
#         # Instead of writing to file, it redirects to the cloud logger
#         return self.cloud_logger.write_log(message)

# # Step 4: Client Code
# file_logger = FileLogger()
# cloud_logger = CloudLogger()
# adapter = LoggingAdapter(cloud_logger)

# # Using the old system
# print(file_logger.log_message("System started."))  # Output: Log written to file: System started.

# # Using the new system through the adapter (old method, new behavior)
# print(adapter.log_message("User logged in."))  # Output: Log sent to cloud: User logged in.


# Adapter enables new technology to work alongside old systems.
# Both the old and new systems remain usable, allowing gradual migration.
# No need to rewrite legacy code, making integration smooth.


# python3 2.DesignPatterns/2.StructuralPatterns/2.1.Adapter.py
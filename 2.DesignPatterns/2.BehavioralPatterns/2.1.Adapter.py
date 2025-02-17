# The Adapter Pattern is a structural design pattern that allows two 
# incompatible interfaces to work together. It acts as a bridge between existing 
# and new code, enabling interoperability without modifying the original classes.

# Why?
# When you have legacy code that doesn’t match a new interface.
# When two systems must work together but have different method names or structures.
# When you want to reuse existing functionality without modifying the source code.
# When you're integrating third-party libraries that don’t match your expected interface.


# Step 1: Adaptee (Old Logging System - File Logger)
class FileLogger:
    def log_message(self, message):
        return f"Log written to file: {message}"

# Step 2: Target Interface (New Logging System - Cloud Logger)
class CloudLogger:
    def write_log(self, message):
        return f"Log sent to cloud: {message}"

# Step 3: Adapter (Allows Old Code to Use the New Cloud Logger)
class LoggingAdapter(FileLogger):
    def __init__(self, cloud_logger):
        self.cloud_logger = cloud_logger  # Takes an instance of CloudLogger

    def log_message(self, message):
        # Instead of writing to file, it redirects to the cloud logger
        return self.cloud_logger.write_log(message)

# Step 4: Client Code
file_logger = FileLogger()
cloud_logger = CloudLogger()
adapter = LoggingAdapter(cloud_logger)

# Using the old system
print(file_logger.log_message("System started."))  # Output: Log written to file: System started.

# Using the new system through the adapter (old method, new behavior)
print(adapter.log_message("User logged in."))  # Output: Log sent to cloud: User logged in.


# Adapter enables new technology to work alongside old systems.
# Both the old and new systems remain usable, allowing gradual migration.
# No need to rewrite legacy code, making integration smooth.


# python3 2.DesignPatterns/2.BehavioralPatterns/2.1.Adapter.py
Designing a Parking Lot System

Requirements:
The parking lot should have multiple levels, each level with a certain number of parking spots.
The parking lot should support different types of vehicles, such as cars, motorcycles, and trucks.
Each parking spot should be able to accommodate a specific type of vehicle.
The system should assign a parking spot to a vehicle upon entry and release it when the vehicle exits.
The system should track the availability of parking spots and provide real-time information to customers.
The system should handle multiple entry and exit points and support concurrent access.



After implementing the singleton (making sure you have only 1 instance) and factory pattern (clean way to instantiate different types of same thing(like Car, Motorcycle, Truck) without repeating boilerplate)

Now we can implement strategy pattern (for using of different patterns):
closest first
first available
priority based (vip spots)
level-based(eg; park on level 1 first)

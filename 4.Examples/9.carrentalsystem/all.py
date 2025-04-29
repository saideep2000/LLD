# Factory Car:

from abc import ABC
class Factorycar(ABC):
    @staticmethod
    def add_car(id, make, model, year, price, availability):
        return Car(id, make, model, year, price, availability)

class Car:
    def __init__(self, id, make, model, year, price, availability):
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.availability = availability
    
    def change_availability(self, availability):
        self.availability = availability


# ---------------------------------------------------------------

# Customer : 

class Customer():
    def __init__(self, name, age, driving_license):
        self.name = name
        self.age = age
        self.driving_license = driving_license

# ---------------------------------------------------------------

# Reservation

import uuid
class Reservation():
    def __init__(self, expected_pick_up_date_time, expected_drop_off_date_time, car, customer):
        self.receipt_id = uuid.uuid4()
        self.expected_pick_up_date_time = expected_pick_up_date_time
        self.expected_drop_off_date_time = expected_drop_off_date_time
        self.pick_up_date_time = None
        self.drop_off_date_time = None
        self.car = car
        self.customer = customer
    
    def update_pick_up_date_time(self, pick_up_date_time):
        self.pick_up_date_time = pick_up_date_time
    
    def update_drop_off_date_time(self, drop_off_date_time):
        self.drop_off_date_time = drop_off_date_time

# ---------------------------------------------------------------

# PaymentProcessor:

class PaymentProcessor():
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PaymentProcessor, cls).__new__(cls)
            # Initialize the singleton instance
            cls._instance.initialize()
        return cls._instance
    
    def initialize(self):
        # Initialize any payment processor properties here
        self.payment_methods = ["credit_card", "debit_card", "cash"]
    
    def process_payment(self, reservation, payment_method, amount):
        if payment_method not in self.payment_methods:
            return False, "Invalid payment method"
        
        # In a real implementation, this would connect to a payment gateway
        print(f"Processing payment of ${amount} for reservation {reservation.receipt_id} using {payment_method}")
        return True, "Payment processed successfully"


# ---------------------------------------------------------------
# Command Pattern:

from abc import ABC, abstractmethod

class RentalCommand(ABC):
    @abstractmethod
    def execute(self):
        pass


class AddCarCommand(RentalCommand):
    def __init__(self, rental_system, id, make, model, year, price, availability):
        self.rental_system = rental_system
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.availability = availability
    
    def execute(self):
        # Check if car already exists
        if self.id in self.rental_system.cars:
            return False, "Car with this ID already exists"
        
        # Create the car using factory
        car = Factorycar.add_car(self.id, self.make, self.model, self.year, self.price, self.availability)
        
        # Add to the system's inventory
        self.rental_system.cars[self.id] = car
        return True, car


class RemoveCarCommand(RentalCommand):
    def __init__(self, rental_system, car_id):
        self.rental_system = rental_system
        self.car_id = car_id
    
    def execute(self):
        # Check if car exists
        if self.car_id not in self.rental_system.cars:
            return False, "Car does not exist"
        
        # Check if car is part of any active reservation
        for reservation in self.rental_system.reservations.values():
            if reservation.car.id == self.car_id and reservation.drop_off_date_time is None:
                return False, "Car is currently reserved"
        
        # Remove car from inventory
        del self.rental_system.cars[self.car_id]
        return True, "Car removed successfully"


class SearchCommand(RentalCommand):
    def __init__(self, rental_system, criteria):
        self.rental_system = rental_system
        self.criteria = criteria
    
    def execute(self):
        result = []
        # Search through all cars
        for car in self.rental_system.cars.values():
            if not car.availability:
                continue
                
            matches = True
            for key, value in self.criteria.items():
                if key == 'price_max' and car.price > value:
                    matches = False
                    break
                elif key == 'price_min' and car.price < value:
                    matches = False
                    break
                elif key == 'make' and car.make != value:
                    matches = False
                    break
                elif key == 'model' and car.model != value:
                    matches = False
                    break
                elif key == 'year' and car.year != value:
                    matches = False
                    break
            
            if matches:
                result.append(car)
                
        return result


class MakeReservationCommand(RentalCommand):
    def __init__(self, rental_system, car_id, customer, pick_up_date, drop_off_date):
        self.rental_system = rental_system
        self.car_id = car_id
        self.customer = customer
        self.pick_up_date = pick_up_date
        self.drop_off_date = drop_off_date
    
    def execute(self):
        # Check if car exists
        if self.car_id not in self.rental_system.cars:
            return False, "Car does not exist"
        
        car = self.rental_system.cars[self.car_id]
        
        # Check if car is available
        if not car.availability:
            return False, "Car is not available"
        
        # Create reservation
        reservation = Reservation(self.pick_up_date, self.drop_off_date, car, self.customer)
        
        # Update car availability
        car.change_availability(False)
        
        # Store reservation
        self.rental_system.reservations[str(reservation.receipt_id)] = reservation
        
        return True, reservation


class CancelReservationCommand(RentalCommand):
    def __init__(self, rental_system, reservation_id):
        self.rental_system = rental_system
        self.reservation_id = reservation_id
    
    def execute(self):
        # Check if reservation exists
        if self.reservation_id not in self.rental_system.reservations:
            return False, "Reservation does not exist"
        
        reservation = self.rental_system.reservations[self.reservation_id]
        
        # Make car available again
        reservation.car.change_availability(True)
        
        # Remove reservation
        del self.rental_system.reservations[self.reservation_id]
        
        return True, "Reservation canceled successfully"


class ProcessPaymentCommand(RentalCommand):
    def __init__(self, rental_system, reservation_id, payment_method, amount):
        self.rental_system = rental_system
        self.reservation_id = reservation_id
        self.payment_method = payment_method
        self.amount = amount
    
    def execute(self):
        # Check if reservation exists
        if self.reservation_id not in self.rental_system.reservations:
            return False, "Reservation does not exist"
        
        reservation = self.rental_system.reservations[self.reservation_id]
        return self.rental_system.payment_processor.process_payment(
            reservation, self.payment_method, self.amount
        )


# ---------------------------------------------------------------

# Rental System : 

class RentalSystem():
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RentalSystem, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance
    
    def initialize(self):
        self.cars = {}  # car_id -> Car
        self.reservations = {}  # reservation_id -> Reservation
        self.payment_processor = PaymentProcessor()
        self.command_history = []  # For tracking executed commands
    
    def execute(self, command):
        result = command.execute()
        self.command_history.append(command)  # Store command for history/undo
        return result


# ---------------------------------------------------------------

# Rental System Demo :

class CarRentalSystemDemo():
    @staticmethod
    def run():
        # Get rental system instance
        rental_system = RentalSystem()
        
        # Add cars
        print("Adding cars to the system...")
        add_car1 = AddCarCommand(rental_system, "C001", "Toyota", "Camry", 2022, 50, True)
        add_car2 = AddCarCommand(rental_system, "C002", "Honda", "Accord", 2023, 60, True)
        add_car3 = AddCarCommand(rental_system, "C003", "Ford", "Mustang", 2022, 100, True)
        
        rental_system.execute(add_car1)
        rental_system.execute(add_car2)
        rental_system.execute(add_car3)
        
        # Search for available Toyota cars
        print("\nSearching for available Toyota cars...")
        search_command = SearchCommand(rental_system, {"make": "Toyota"})
        toyota_cars = rental_system.execute(search_command)
        for car in toyota_cars:
            print(f"Found: {car.make} {car.model} ({car.year}) - ${car.price}/day")
        
        # Create a customer
        customer = Customer("John Doe", 30, "DL12345")
        
        # Make a reservation
        print("\nMaking a reservation...")
        import datetime
        pickup_date = datetime.datetime.now()
        dropoff_date = pickup_date + datetime.timedelta(days=3)
        
        make_reservation = MakeReservationCommand(
            rental_system, "C001", customer, pickup_date, dropoff_date
        )
        success, reservation = rental_system.execute(make_reservation)
        
        if success:
            print(f"Reservation created with ID: {reservation.receipt_id}")
            
            # Process payment
            print("\nProcessing payment...")
            payment_command = ProcessPaymentCommand(
                rental_system, str(reservation.receipt_id), "credit_card", 150
            )
            rental_system.execute(payment_command)
            
            # Cancel reservation
            print("\nCanceling reservation...")
            cancel_command = CancelReservationCommand(rental_system, str(reservation.receipt_id))
            rental_system.execute(cancel_command)
            
            # Show command history
            print("\nCommand History:")
            for i, cmd in enumerate(rental_system.command_history):
                print(f"{i+1}. {cmd.__class__.__name__}")
        else:
            print(f"Failed to create reservation: {reservation}")


if __name__ == "__main__":
    CarRentalSystemDemo.run()
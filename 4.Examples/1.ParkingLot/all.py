# vehicle_type
from enum import Enum
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from abc import ABC, abstractmethod

class VehicleType(Enum):
    CAR = 1
    BIKE = 2
    TRUCK = 3

# Payment class
class Payment:
    def __init__(self, amount: float, payment_date: datetime = None):
        self.amount = amount
        self.payment_date = payment_date or datetime.now()
        self.is_completed = False
    
    def complete_payment(self):
        self.is_completed = True
        return True
    
    def get_amount(self):
        return self.amount
    
    def is_payment_completed(self):
        return self.is_completed

# Payment strategy - different vehicles might have different payment calculations
class PaymentStrategy(ABC):
    @abstractmethod
    def calculate_payment(self, vehicle_type: VehicleType, duration_hours: float) -> float:
        pass

# Standard payment strategy
class StandardPaymentStrategy(PaymentStrategy):
    def calculate_payment(self, vehicle_type: VehicleType, duration_hours: float) -> float:
        rates = {
            VehicleType.BIKE: 1.0,  # $1 per hour
            VehicleType.CAR: 2.0,   # $2 per hour
            VehicleType.TRUCK: 3.0  # $3 per hour
        }
        
        hourly_rate = rates.get(vehicle_type, 2.0)  # Default to car rate if type not found
        return hourly_rate * duration_hours

# factory vehicle
class FactoryVehicle():
    @staticmethod
    def create_vehicle(type: VehicleType, license: str):
        if type == VehicleType.CAR:
            return Car(license, type)
        elif type == VehicleType.BIKE:
            return Bike(license, type)
        elif type == VehicleType.TRUCK:
            return Truck(license, type)
        else:
            raise Exception(f"Invalid vehicle type given: {type}")

# vehicle
class Vehicle(ABC):
    def __init__(self, license, vehicle_type):
        self.license = license
        self.vehicle_type = vehicle_type
    
    def get_license_number(self):
        return self.license

    def get_vehicle_type(self):
        return self.vehicle_type

# car
class Car(Vehicle):
    def __init__(self, license, vehicle_type):
        super().__init__(license, vehicle_type)
    
# bike
class Bike(Vehicle):
    def __init__(self, license, vehicle_type):
        super().__init__(license, vehicle_type)

# truck
class Truck(Vehicle):
    def __init__(self, license, vehicle_type):
        super().__init__(license, vehicle_type)

# parking record - to track parking duration for payment calculation
class ParkingRecord:
    def __init__(self, vehicle: Vehicle, spot: 'ParkingSpot'):
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.now()
        self.exit_time = None
        self.payment = None
    
    def exit(self):
        self.exit_time = datetime.now()
    
    def get_duration_hours(self) -> float:
        if self.exit_time is None:
            # Still parked, calculate duration until now
            duration = datetime.now() - self.entry_time
        else:
            duration = self.exit_time - self.entry_time
            
        # Convert timedelta to hours
        hours = duration.total_seconds() / 3600
        return hours
    
    def set_payment(self, payment: Payment):
        self.payment = payment
    
    def is_payment_completed(self) -> bool:
        return self.payment is not None and self.payment.is_payment_completed()

# parking spot
class ParkingSpot:
    def __init__(self, level_id, spot_id):
        self.level_id = level_id
        self.id = spot_id
        self.availability = True
        self.vehicle = None
        self.parking_record = None

    def get_availability(self):
        return self.availability

    def park(self, vehicle: Vehicle) -> Optional[ParkingRecord]:
        if self.availability:
            self.vehicle = vehicle
            self.availability = False
            # Create parking record
            self.parking_record = ParkingRecord(vehicle, self)
            return self.parking_record
        return None
    
    def unpark(self) -> Optional[ParkingRecord]:
        if not self.availability and self.vehicle is not None and self.parking_record is not None:
            # Record exit time
            self.parking_record.exit()
            record = self.parking_record
            
            # Reset spot
            self.vehicle = None
            self.parking_record = None
            self.availability = True
            
            return record
        return None
    
    def get_parking_record(self) -> Optional[ParkingRecord]:
        return self.parking_record

# levels
class Level:
    def __init__(self, id, num_of_spots):
        self.id = id
        self.spots: List[ParkingSpot] = [ParkingSpot(id, i) for i in range(num_of_spots)]

    def get_spot_count(self):
        return len(self.spots)

    def get_spots(self):
        return self.spots
    
    # Find a spot by ID
    def find_spot_by_id(self, spot_id: int) -> Optional[ParkingSpot]:
        for spot in self.spots:
            if spot.id == spot_id:
                return spot
        return None

# strategy to park
class StrategyPark(ABC):
    @abstractmethod
    def park(self, vehicle, levels):
        pass

# This strategy is to park floor wise from first available spot
class StrategyParkFirst(StrategyPark):
    def park(self, vehicle, levels: List[Level]):
        for level in levels:
            for spot in level.get_spots():
                if spot.get_availability():
                    record = spot.park(vehicle)
                    if record:
                        return record
        return None

# parking system
class ParkingSystem:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ParkingSystem, cls).__new__(cls)
        return cls._instance

    def __init__(self, 
                 strategy_to_park=None, 
                 payment_strategy=None):
        # Only initialize if not already initialized
        if not hasattr(self, 'initialized'):
            self.levels: List[Level] = []
            self.strategy_to_park = strategy_to_park if strategy_to_park else StrategyParkFirst()
            self.payment_strategy = payment_strategy if payment_strategy else StandardPaymentStrategy()
            self.parking_records: Dict[str, List[ParkingRecord]] = {}  # License -> records
            self.initialized = True
    
    def add_level(self, num_of_spots):
        self.levels.append(Level(len(self.levels), num_of_spots))
        return len(self.levels) - 1  # Return the level ID
    
    def set_strategy_for_parking(self, strategy):
        self.strategy_to_park = strategy
    
    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy
    
    def park(self, vehicle: Vehicle) -> Optional[ParkingRecord]:
        # Attempt to park the vehicle
        record = self.strategy_to_park.park(vehicle, self.levels)
        
        # If parked successfully, store the record
        if record:
            license = vehicle.get_license_number()
            if license not in self.parking_records:
                self.parking_records[license] = []
            self.parking_records[license].append(record)
            
        return record
    
    def unpark(self, level_id: int, spot_id: int) -> Optional[ParkingRecord]:
        # Find the level
        if level_id < 0 or level_id >= len(self.levels):
            return None
        
        level = self.levels[level_id]
        spot = level.find_spot_by_id(spot_id)
        
        if spot and not spot.get_availability():
            return spot.unpark()
        
        return None
    
    def unpark_by_license(self, license: str) -> Optional[ParkingRecord]:
        # Find all records for this license
        if license not in self.parking_records:
            return None
        
        records = self.parking_records[license]
        # Find the active record (without exit time)
        active_records = [r for r in records if r.exit_time is None]
        
        if not active_records:
            return None
        
        # Get the spot from the record and unpark
        record = active_records[0]
        return record.spot.unpark()
    
    def calculate_payment(self, record: ParkingRecord) -> float:
        if not record:
            return 0.0
        
        duration = record.get_duration_hours()
        vehicle_type = record.vehicle.get_vehicle_type()
        
        return self.payment_strategy.calculate_payment(vehicle_type, duration)
    
    def process_payment(self, record: ParkingRecord) -> Optional[Payment]:
        if not record:
            return None
        
        # Check if already paid
        if record.is_payment_completed():
            return record.payment
        
        # Calculate amount
        amount = self.calculate_payment(record)
        
        # Create payment
        payment = Payment(amount)
        
        # Complete payment (in a real system, this would involve payment processing)
        payment.complete_payment()
        
        # Update record
        record.set_payment(payment)
        
        return payment
        
    def get_parking_history(self, license: str) -> List[ParkingRecord]:
        return self.parking_records.get(license, [])

# Parking system Demo:
class ParkingSystemDemo:
    @staticmethod
    def run():
        ps = ParkingSystem()

        # Add levels
        ps.add_level(12)
        ps.add_level(15)

        # Create vehicles
        car = FactoryVehicle.create_vehicle(VehicleType.CAR, "1234QWER")
        bike = FactoryVehicle.create_vehicle(VehicleType.BIKE, "5987QWER")
        truck = FactoryVehicle.create_vehicle(VehicleType.TRUCK, "34565QWER")
        
        # Park vehicles
        print("Parking vehicles...")
        car_record = ps.park(car)
        print(f"Car parked at Level {car_record.spot.level_id}, Spot {car_record.spot.id}")
        
        bike_record = ps.park(bike)
        print(f"Bike parked at Level {bike_record.spot.level_id}, Spot {bike_record.spot.id}")
        
        truck_record = ps.park(truck)
        print(f"Truck parked at Level {truck_record.spot.level_id}, Spot {truck_record.spot.id}")
        
        # Simulate some time passing (for demo purposes)
        print("\nSimulating passage of time (3 hours)...")
        # In a real implementation, time would pass naturally
        car_record.entry_time = datetime.now() - timedelta(hours=3)
        
        # Unpark car and process payment
        print("\nUnparking car...")
        car_record = ps.unpark(car_record.spot.level_id, car_record.spot.id)
        if car_record:
            payment = ps.process_payment(car_record)
            print(f"Car unparked. Duration: {car_record.get_duration_hours():.2f} hours")
            print(f"Payment amount: ${payment.get_amount():.2f}, Completed: {payment.is_payment_completed()}")
        
        # Unpark bike by license
        print("\nUnparking bike by license...")
        bike_record = ps.unpark_by_license(bike.get_license_number())
        if bike_record:
            payment = ps.process_payment(bike_record)
            print(f"Bike unparked. Duration: {bike_record.get_duration_hours():.2f} hours")
            print(f"Payment amount: ${payment.get_amount():.2f}, Completed: {payment.is_payment_completed()}")
        
        # Check parking history
        print("\nParking history for car license:", car.get_license_number())
        car_history = ps.get_parking_history(car.get_license_number())
        for i, record in enumerate(car_history):
            print(f"Record {i+1}:")
            print(f" - Entry time: {record.entry_time}")
            print(f" - Exit time: {record.exit_time}")
            if record.payment:
                print(f" - Payment: ${record.payment.amount:.2f}")

if __name__ == "__main__":
    ParkingSystemDemo.run()
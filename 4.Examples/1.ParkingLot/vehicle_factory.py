from vehicle_type import VehicleType
from car import Car
from motorcycle import Motorcycle
from truck import Truck

class Vehiclefactory:
    @staticmethod
    def create_vehicle(vehicle_kind : VehicleType, license_plate : str) -> VehicleType:
        if vehicle_kind == VehicleType.CAR:
            return Car(license_plate)
        elif vehicle_kind == VehicleType.TRUCK:
            return Truck(license_plate)
        elif vehicle_kind == VehicleType.MOTORCYCLE:
            return Motorcycle(license_plate)
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_kind}")

from vehicle_type import VehicleType
from abc import ABC

class Vehicle(ABC):
    def __init__(self, license_plate : str, vehicle_type : VehicleType):
        self.license_plate = license_plate
        self.type = vehicle_type
    
    def get_type(self) -> VehicleType:
        return self.type

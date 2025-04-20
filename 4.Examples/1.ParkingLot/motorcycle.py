from vehicle import Vehicle
from vehicle_type import VehicleType
class Motorcycle(Vehicle):
    def __init__(self, license_plate : str):
        super().__init__(license_plate, VehicleType.MOTORCYCLE)
from vehicle_type import VehicleType
from vehicle import Vehicle
class ParkingSpot():
    def __init__(self, spot_number : int):
        self.spot_number = spot_number
        self.parked_vehicle = None
        self.vehicle_type = VehicleType.CAR

    def is_availabile(self) -> bool:
        return self.parked_vehicle is None
    
    def park_vehicle(self,vehicle : Vehicle) -> None:
        if self.is_availabile() and vehicle.get_type() == self.vehicle_type:
            self.parked_vehicle = vehicle
        else:
            raise ValueError("Invalid vehicle type or spot already occupied.")
    
    def unpark_vehicle(self) -> None:
        self.parked_vehicle = None
    
    def get_spot_number(self) -> int:
        return self.spot_number
    
    def get_vehicle_type(self) -> VehicleType:
        return self.vehicle_type

    def get_parked_vehicle(self) -> Vehicle:
        return self.parked_vehicle
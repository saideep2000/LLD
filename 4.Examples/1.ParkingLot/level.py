from typing import List
from parking_spot import ParkingSpot
from vehicle import Vehicle
class Level():
    def __init__(self, floor : int, num_spots : int):
        self.floor = floor
        self.parking_spots : List[ParkingSpot] = [ParkingSpot(i) for i in range(num_spots)]

    def park_vehicle(self, vehicle : Vehicle) -> bool:
        for parking_spot in self.parking_spots:
            if parking_spot.is_availabile() and parking_spot.get_vehicle_type() == vehicle.get_type():
                parking_spot.park_vehicle(vehicle)
                return True
        return False
    
    def unpark_vehicle(self, vehicle : Vehicle) -> bool:
        for parking_spot in self.parking_spots:
            if not parking_spot.is_availabile() and parking_spot.get_parked_vehicle() == vehicle:
                parking_spot.unpark_vehicle(vehicle)
                return True
        return False
    
    def display_availability(self) -> None:
        print(f"Level : {self.floor} Availability:")
        for spot in self.parking_spots:
            print(f"Spot {spot.get_spot_number()} : {'Available' if spot.is_availabile() else 'Occupied'}")

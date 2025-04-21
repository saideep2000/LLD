from parking_lot import ParkingLot
from vehicle_type import VehicleType
# from vehicle import Vehicle
# from car import Car
# from truck import Truck
# from motorcycle import Motorcycle
from level import Level
from vehicle_factory import Vehiclefactory

class ParkingLotDemo:
    def run():
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_level(Level(1,3))
        parking_lot.add_level(Level(2,3))


        # before the factory design pattern
        # car = Car("ABC123")
        # truck = Truck("XYZ789")
        # motorcycle = Motorcycle("M1234")

        # after factory design pattern
        car = Vehiclefactory.create_vehicle(VehicleType.CAR, "ABC123")
        truck = Vehiclefactory.create_vehicle(VehicleType.TRUCK, "XYZ789")
        motorcycle = Vehiclefactory.create_vehicle(VehicleType.MOTORCYCLE, "M1234")


        # Park vehicles
        print(parking_lot.park_vehicle(car))
        print(parking_lot.park_vehicle(truck))
        print(parking_lot.park_vehicle(motorcycle))

        # Display availability
        parking_lot.display_availability()

        # Unpark vehicle
        parking_lot.unpark_vehicle(motorcycle)

        # Display updated availability
        parking_lot.display_availability()
if __name__ == "__main__":
    ParkingLotDemo.run()


# python3 4.Examples/1.ParkingLot/parking_lot_demo.py
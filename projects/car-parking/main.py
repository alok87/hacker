from parkinglot import ParkingLot
from parkingspace import ParkingSpace


if __name__ == '__main__':

    print("Creating Parking lot")
    parking_lot = ParkingLot()
    parking_levels = int(raw_input("No of parking levels: "))
    parking_lot.set_levels(parking_levels)
    ids = 1
    for level in range(1, parking_levels + 1):
        spaces = int(raw_input("No of spaces in level %d: " % level))
        entrance = str(raw_input("Entrance of level %d: " % level))
        level_parking_spaces = []
        for space in range(1, spaces + 1):
            space_id = ids
            parking_space = ParkingSpace()
            parking_space.set_level_id(level)
            parking_space.set_space_id(space_id)
            parking_space.set_entrance(entrance)
            level_parking_spaces.append(parking_space)
            ids += 1
    print("Parking lot created")





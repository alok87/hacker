from constants import FULL, EMPTY, FILLING
from parkingspace import ParkingSpace


class ParkingLot:
    def __init__(self):
        self.__sign = EMPTY
        self.__levels = 0
        self.parking_spaces = []
        self.vacant_parking_spaces = []

    def get_sign(self):
        return self__sign

    def set_sign(self, sign):
        if sign not in [FULL, EMPTY, FILLING]:
            raise Exception('Invalid parking sign %s' % sign)
        self.__sign = sign

    def get_levels(self):
        return self.__levels

    def set_levels(self, levels):
        self.__levels = levels

    def set_parking_spaces(self, parking_space):
        self.parking_spaces.append(parking_space)

    def get_parking_spaces(self):
        return self.parking_spaces

    def set_vacant_parking_spaces(self, parking_space):
        self.vacant_parking_spaces.append(parking_space)

    def get_vacant_parking_spaces(self):
        self.vacant_parking_spaces


class ParkingSpace:
    def __init__(self):
        self.__level_id = None
        self.__space_id = None
        self.__entrance = None

    def get_level_id(self):
        return self.__level_id

    def set_level_id(self, id):
        return self.__level_id

    def get_space_id(self):
        return self.__space_id

    def set_space_id(self, id):
        self.__space_id = id

    def get_entrance(self):
        return self.__entrance

    def set_entrance(self, entrance):
        self.__entrance = entrance

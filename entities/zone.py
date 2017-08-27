class Zone(object):

    def __init__(self):
        self.__id = -1
        self.__name = ""
        self.__description = ""
        self.__rooms = []

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, val):
        self.__id = val

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, val):
        self.__description = val

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, val):
        self.__rooms = val

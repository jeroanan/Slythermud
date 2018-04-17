import inspect

import entities.room as room

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

    def room_by_id(self, room_id):
        pass

    @classmethod
    def from_dict(cls, the_dict):
        z = Zone()

        propnames = [name for (name,value) in inspect.getmembers(Zone, lambda x: isinstance(x, property))]

        for p in propnames:
            if p!="rooms": setattr(z, p, the_dict.get(p, ""))
            
        for r in the_dict["rooms"]:
            z.rooms.append(room.Room.from_dict(r))
    
        return z

import inspect

import world.direction as direction

class Room(object):

    def __init__(self):
        self.__id = "-1"
        self.__name = ""
        self.__description = ""
        self.__exit_north = ""
        self.__exit_east = ""
        self.__exit_south = ""
        self.__exit_west = ""
        self.__exit_up = ""
        self.__exit_down = ""

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,val):
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
    def exit_north(self):
        return self.__exit_north

    @exit_north.setter
    def exit_north(self, val):
        self.__exit_north = val

    @property
    def exit_east(self):
        return self.__exit_east

    @exit_east.setter
    def exit_east(self, val):
        self.__exit_east = val

    @property
    def exit_south(self):
        return self.__exit_south

    @exit_south.setter
    def exit_south(self, val):
        self.__exit_south = val

    @property
    def exit_west(self):
        return self.__exit_west

    @exit_west.setter
    def exit_west(self, val):
        self.__exit_west = val

    @property
    def exit_up(self):
        return self.__exit_up

    @exit_up.setter
    def exit_up(self, val):
        self.__exit_up = val

    @property
    def exit_down(self):
        return self.__exit_down

    @exit_down.setter
    def exit_down(self, val):
        self.__exit_down = val

    def can_exit_dir(self, d):
        return self.get_exit(d) is not None

    def get_exit(self, d):
        if d=="": return None

        exits = {"north": self.exit_north,
                "east": self.exit_east,
                "south": self.exit_south,
                "west": self.exit_west}
        
        ed = direction.get_direction(d)

        exit_string = exits.get(ed, None)

        if exit_string is None: return exit_string
        exit_split = exit_string.split(',')

        return (exit_split[0], exit_split[1])

    @classmethod
    def from_dict(cls, the_dict):

        r = Room()
        
        propnames = [name for (name,value) in inspect.getmembers(Room, lambda x: isinstance(x, property))]

        for p in propnames:
            setattr(r, p, the_dict.get(p, ""))
            
        return r


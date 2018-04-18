import database.dbcommand as dbcommand

class PlayerStatus(object):

    def __init__(self):
        self.__name__ = ""
        self.__zone__ = ""
        self.__room__ = ""

    @property
    def name(self):
        return self.__name__
    
    @name.setter
    def name(self, val):
        self.__name__ = val

    @property
    def zone(self):
        return self.__zone__

    @zone.setter
    def zone(self, val):
        self.__zone__ = val

    @property
    def room(self):
        return self.__room__

    @room.setter
    def room(self, val):
        self.__room__ = val

    def save(self, config):

        sql = ""
        params = ()

        if PlayerStatus.load_by_name(config, self.name, False) is not None:
            sql = "UPDATE PlayerStatus SET Zone=?, Room=? WHERE Name=?"
            params = (self.zone, self.room, self.name,)
        else:
            sql = "INSERT INTO PlayerStatus (Name, Zone, Room) VALUES (?, ?, ?)"
            params = (self.name, self.room, self.zone,)

        dbcommand.param_exec(config, sql, params)

    @classmethod
    def load_by_name(cls, config, name, create_not_exist=True):
        """
        Load the given player's current status.
        """
        ps = PlayerStatus()

        sql = "SELECT Name, Zone, Room FROM PlayerStatus WHERE Name=?"
        result = dbcommand.param_fetch_one(config, sql, (name,))

        if result is None:
            ps.name = name
            ps.zone = config.start_zone
            ps.room = config.start_room

            if create_not_exist:
                ps.save(config)
            else:
                return None

        if result is not None: ps.name, ps.zone, ps.room = result
        return ps

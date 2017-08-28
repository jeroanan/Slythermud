import bcrypt

import database.dbcommand as dbcommand
import entities.playerstatus as playerstatus

class Player(object):
    
    def __init__(self):
        self.__name = ""
        self.__password = ""
        self.__gender = ""
        self.__status = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, val):
        try:
            self.__password = bcrypt.hashpw(val.encode(), bcrypt.gensalt())
        except AttributeError:
            self.__password = val

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, val):
        self.__gender = val

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, val):
        self.__status = val

    def verify_password(self, password):
        return bcrypt.hashpw(password.encode(), self.password)==self.password

    def save(self, config):
        """
        Create a new player record if it doesn't exist. Otherwise update
        an existing one.
        """
        if Player.load_by_name(config, self.name):
            pass # TODO: Update existing player
        else:
            sql = "INSERT INTO Player (Name, Password, Gender) VALUES (?, ?, ?)"
            params = (self.name, self.password, self.gender)
            dbcommand.param_exec(config, sql, params)

        if self.status is not None: self.status.save(config)

    @classmethod
    def load_by_name(cls, config, name):
        """
        Load a player record given the player's name. Also load the player's
        current status.
        """

        the_player = None

        sql = "SELECT Name, Password, Gender FROM Player WHERE Name=?"

        result = dbcommand.param_fetch_one(config, sql, (name,))

        if result is not None:
            the_player = Player()
            the_player.name, the_player.password, the_player.gender = result
            the_player.status = playerstatus.PlayerStatus.load_by_name(config, name)

        return the_player

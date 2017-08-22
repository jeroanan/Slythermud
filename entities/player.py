import bcrypt
import sqlite3

class Player(object):
    
    def __init__(self):
        self.__name = ""
        self.__password = ""
        self.__gender = ""

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
            Player.param_exec(config, sql, params)

    @classmethod
    def load_by_name(cls, config, name):

        the_player = None

        conn = sqlite3.connect(config.database_file)
        cur = conn.cursor()

        sql = "SELECT Name, Password, Gender FROM Player WHERE Name=?"

        cur.execute(sql, (name,))

        result = cur.fetchone()

        if result is not None:
            the_player = Player()
            the_player.name, the_player.password, the_player.gender = result

        cur.close()
        conn.close()

        return the_player

    @classmethod
    def param_exec(cls, config, sql, params):
        conn = sqlite3.connect(config.database_file)
        cur = conn.cursor()

        cur.execute(sql, params)

        conn.commit()

        cur.close()
        conn.close()

import bcrypt
import sqlite3

class Player(object):
    
    def __init__(self):
        self.__name = ""
        self.__password = ""

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
        self.__password = bcrypt.hashpw(val.encode(), bcrypt.gensalt())

    def verify_password(self, password):
        return bcrypt.hashpw(password.encode(), self.password)==self.password

    @classmethod
    def load_by_name(self, config, name):

        player = None

        conn = sqlite3.connect(config.database_file)
        cur = conn.cursor()

        sql = "SELECT Name, Password FROM Player WHERE Name=?"

        cur.execute(sql, (name,))

        result = cur.fetchone()

        if result is not None:
            print(result)
        cur.close()
        conn.close()

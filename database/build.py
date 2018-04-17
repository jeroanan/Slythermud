import logging
import sqlite3

class Build(object):

    def __init__(self, config):
        self.__config = config
        self.__conn = None
        self.__logger = logging.getLogger('database.Build')

    def build(self):
        self.__logger.info("Building database at {df}".format(df=self.__config.database_file))
        self.__conn = sqlite3.connect(self.__config.database_file)

        def table_exists(table_name):
            return self.__table_exists(conn, table_name)

        self.__create_player_table()
        self.__create_player_status_table()

        self.__conn.commit()
        self.__conn.close()

        self.__logger.info("Done building database")

    def __create_player_table(self):
        sql = """CREATE TABLE Player (Name TEXT PRIMARY KEY, 
                                      Password TEXT, 
                                      Gender TEXT)"""
        self.__create_table("Player", sql)

    def __create_player_status_table(self):
        sql = """CREATE TABLE PlayerStatus (Name TEXT PRIMARY KEY REFERENCES Player(Name),
                                            Zone INT,
                                            Room INT)"""
        self.__create_table("PlayerStatus", sql)

    def __create_table(self, table_name, creation_sql):
        if self.__table_exists(table_name): return

        _logger.info("Creating new table {tn}".format(tn=table_name))

        cur = self.__conn.cursor()
        cur.execute(creation_sql)
        cur.close()

    def __table_exists(self, table_name):
        sql = "SELECT * FROM sqlite_master WHERE name=? AND type='table'"

        cur = self.__conn.cursor()
        cur.execute(sql, (table_name,))
        result = cur.fetchone()
        cur.close()

        return result is not None



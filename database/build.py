import sqlite3

class Build(object):

    def __init__(self, config):
        self.__config = config

    def build(self):
        conn = sqlite3.connect(self.__config.database_file)

        def table_exists(table_name):
            return self.__table_exists(conn, table_name)

        self.__create_player_table(conn)

        conn.close()

    def __create_player_table(self, conn):
        if self.__table_exists(conn, "Player"): return

        sql = "CREATE TABLE Player (Name TEXT PRIMARY KEY, Password TEXT, Gender TEXT)"
        cur = conn.cursor()
        cur.execute(sql)
        cur.close()

    def __table_exists(self, conn, table_name):
        sql = "SELECT * FROM sqlite_master WHERE name=? AND type='table'"

        cur = conn.cursor()
        cur.execute(sql, (table_name,))
        result = cur.fetchone()
        cur.close()

        return result is not None



import sqlite3

def param_fetch_one(config, sql, params):

    def action(conn, cur):
        cur.execute(sql, params)
        return cur.fetchone()

    return __do_something(config, action)

def param_exec(config, sql, params):

    def action(conn, cur):
        cur.execute(sql, params)
        conn.commit()

    __do_something(config, action)

def __do_something(config, something):
    conn = sqlite3.connect(config.database_file)
    cur = conn.cursor()

    result = something(conn, cur)

    cur.close()
    conn.close()

    return result


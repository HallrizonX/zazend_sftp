import sqlite3


class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()

        print("Choose connector by ID")
        self.sql_get_all()
        self.conn.commit()

    def sql_get_all(self):
        sql = "SELECT * FROM account"
        for items in self.cursor.execute(sql):
            print(items)

    def sql_insert(self, hostname: str, password: str, username: str):
        sql = "INSERT INTO account VALUES (?,?,?,?)"
        self.cursor.execute(sql, (None, hostname, password, username))

    def sql_get(self, id):
        sql = "SELECT * FROM account WHERE id={}".format(id)
        query = self.cursor.execute(sql)
        return query.fetchone()
    def __del__(self):
        self.conn.commit()

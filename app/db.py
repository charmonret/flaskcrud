import os
import pymysql

pymysql.install_as_MySQLdb()

class MySQLConnectionWrapper:
    def __init__(self):
        self.conn = pymysql.connect(
            host=os.getenv('MYSQL_HOST', 'mysql_db'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', 'rootpassword'),
            database=os.getenv('MYSQL_DB', 'flaskcontacts'),
            cursorclass=pymysql.cursors.DictCursor
        )

    def cursor(self):
        try:
            if not self.conn.open:
                self.conn.ping(reconnect=True)
        except Exception:
            self.conn = pymysql.connect(
                host=os.getenv('MYSQL_HOST', 'mysql_db'),
                user=os.getenv('MYSQL_USER', 'root'),
                password=os.getenv('MYSQL_PASSWORD', 'rootpassword'),
                database=os.getenv('MYSQL_DB', 'flaskcontacts'),
                cursorclass=pymysql.cursors.DictCursor
            )
        return self.conn.cursor()

    def commit(self):
        self.conn.commit()

class MySQL:
    def __init__(self):
        self._connection = None

    @property
    def connection(self):
        if self._connection is None:
            self._connection = MySQLConnectionWrapper()
        return self._connection

mysql = MySQL()
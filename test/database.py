import pymysql

class DBConnector:
    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db

    def connect(self):
        return pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )

    def fetch_data(self, query, params=None):
        with self.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()

    def insert_data(self, query, params=None):
        with self.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                connection.commit()

    def close(self):
        pass
import pymysql

class DBConnector:
    def __init__(self, host, port, user, password, db):
        self.config = {
            'host': host,
            'port': port,
            'user': user,
            'password': password,
            'db': db
        }

    def execute_query(self, query, params=None):
        try:
            conn = pymysql.connect(**self.config)
            with conn.cursor() as cur:
                cur.execute(query, params)
                results = cur.fetchall()
            conn.close()
            return results
        except Exception as e:
            print(f"Ошибка выполнения запроса: {e}")
            return []

    def fetch_data(self, query, params=None):
        return self.execute_query(query, params)

    def insert_data(self, query, params=None):
        conn = pymysql.connect(**self.config)
        with conn.cursor() as cur:
            cur.execute(query, params)
        conn.commit()
        conn.close()
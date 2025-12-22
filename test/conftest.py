import pytest
from .utils.database import DBConnector

@pytest.fixture(autouse=True)
def clear_database():
    conn = DBConnector(host='localhost', port=3306, user='app', password='pass', db='app')
    # Чистка всей таблицы платежей
    conn.execute_query("DELETE FROM payment_entity;")
    yield
    # Чистка после завершения теста
    conn.execute_query("DELETE FROM payment_entity;")
import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="trocadisco_db",
        user="postgres",
        password="120721",
        options="-c client_encoding=UTF8"
    )
    return conn

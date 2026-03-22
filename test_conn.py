import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="trocadisco_db",
        user="postgres",
        password="12345678"
    )
    print("Conexão OK")
    conn.close()
except Exception as e:
    print("Erro:", e)
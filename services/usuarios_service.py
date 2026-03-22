from database.db import get_db_connection

def cadastrar_usuario(login, senha, nome, cidade):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO usuarios (login, senha, nome, cidade) VALUES (%s, %s, %s, %s)',
        (login, senha, nome, cidade)
    )
    conn.commit()
    cur.close()
    conn.close()

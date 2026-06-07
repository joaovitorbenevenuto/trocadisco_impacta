from database.db import get_db_connection

def cadastrar_usuario(login, senha, nome, cidade):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO usuarios (login, senha, nome, city) VALUES (%s, %s, %s, %s)',
        (login, senha, nome, cidade)
    )
    conn.commit()
    cur.close()
    conn.close()

def verificar_usuario(login, senha):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id FROM usuarios WHERE login = %s AND senha = %s', (login, senha))
    usuario = cur.fetchone()
    cur.close()
    conn.close()
    if usuario:
        return usuario[0]
    return None
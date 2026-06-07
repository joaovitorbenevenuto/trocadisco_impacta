from database.db import get_db_connection

def cadastrar_disco(titulo, artista, ano, genero, preco, usuario_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = """
        INSERT INTO discos (titulo, artista, ano, genero, preco, usuario_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    
    cursor.execute(query, (titulo, artista, ano, genero, preco, usuario_id))
    conn.commit()
    
    cursor.close()
    conn.close()

def listar_discos_com_filtro(genero, artista, usuario):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = """
        SELECT d.id, d.titulo, d.artista, d.ano, d.genero, d.preco, u.nome, d.status 
        FROM discos d
        JOIN usuarios u ON d.usuario_id = u.id
        WHERE 1=1
    """
    params = []
    
    if genero:
        query += " AND d.genero ILIKE %s"
        params.append(f"%{genero}%")
    if artista:
        query += " AND d.artista ILIKE %s"
        params.append(f"%{artista}%")
    if usuario:
        query += " AND u.nome ILIKE %s"
        params.append(f"%{usuario}%")
        
    query += " ORDER BY d.id DESC"
    
    cursor.execute(query, params)
    discos_fetched = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return discos_fetched

def registrar_venda(disco_id, comprador_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT status, usuario_id FROM discos WHERE id = %s", (disco_id,))
    disco = cursor.fetchone()

    if disco and disco[0] == 'disponivel' and disco[1] != comprador_id:
        cursor.execute("UPDATE discos SET status = 'vendido' WHERE id = %s", (disco_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    cursor.close()
    conn.close()
    return False
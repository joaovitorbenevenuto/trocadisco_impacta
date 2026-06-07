from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from database.db import get_db_connection

discos_bp = Blueprint('discos', __name__)

@discos_bp.route('/cadastro-disco', methods=['GET', 'POST'])
def cadastro_disco():
    usuario_id = session.get('usuario_id')
    if not usuario_id:
        return redirect(url_for('usuarios.index'))
    if request.method == 'POST':
        titulo = request.form['titulo']
        artista = request.form['artista']
        ano = request.form['ano']
        genero = request.form['genero']
        preco = request.form['preco']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO discos (titulo, artista, ano, genero, preco, usuario_id) VALUES (%s, %s, %s, %s, %s, %s)',
            (titulo, artista, ano, genero, preco, usuario_id)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('discos.lista_discos'))
    return render_template('cadastro_disco.html')

@discos_bp.route('/discos')
def lista_discos():
    usuario_id = session.get('usuario_id')
    if not usuario_id:
        return redirect(url_for('usuarios.index'))
    termo_busca = request.args.get('busca', '')
    conn = get_db_connection()
    cur = conn.cursor()
    query_base = """
        SELECT d.id, d.titulo, d.artista, d.ano, d.genero, d.preco, d.status, d.usuario_id, u.login 
        FROM discos d
        JOIN usuarios u ON d.usuario_id = u.id
    """
    if termo_busca:
        cur.execute(
            query_base + " WHERE (d.titulo ILIKE %s OR d.artista ILIKE %s) ORDER BY d.id DESC",
            (f'%{termo_busca}%', f'%{termo_busca}%')
        )
    else:
        cur.execute(query_base + " ORDER BY d.id DESC")
    discos_banco = cur.fetchall()
    cur.close()
    conn.close()
    lista_de_discos = []
    for d in discos_banco:
        lista_de_discos.append({
            'id': d[0],
            'titulo': d[1],
            'artista': d[2],
            'ano': d[3],
            'genero': d[4],
            'preco': d[5],
            'status': d[6],
            'dono_id': d[7],
            'dono_login': d[8]
        })
    return render_template('listagem_discos.html', discos=lista_de_discos, usuario_atual=usuario_id)

@discos_bp.route('/comprar-disco/<int:disco_id>', methods=['POST'])
def comprar_disco(disco_id):
    usuario_id = session.get('usuario_id')
    if not usuario_id:
        return redirect(url_for('usuarios.index'))
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT u.login FROM discos d JOIN usuarios u ON d.usuario_id = u.id WHERE d.id = %s", (disco_id,))
    vendedor = cur.fetchone()
    cur.execute(
        "UPDATE discos SET status = 'em negociação' WHERE id = %s AND status = 'disponivel'",
        (disco_id,)
    )
    conn.commit()
    cur.close()
    conn.close()
    if vendedor:
        flash(f'O vendedor {vendedor[0]} foi informado e entrará em contato! Aguarde o envio do produto.', 'success')
    return redirect(url_for('discos.lista_discos'))
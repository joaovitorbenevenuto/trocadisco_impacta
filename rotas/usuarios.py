from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from services.usuarios_service import cadastrar_usuario, verificar_usuario

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/')
def index():
    return render_template('login.html')

@usuarios_bp.route('/login', methods=['POST'])
def login():
    login_usuario = request.form['login']
    senha_usuario = request.form['senha']
    usuario_id = verificar_usuario(login_usuario, senha_usuario)
    if usuario_id:
        session['usuario_id'] = usuario_id
        return redirect(url_for('usuarios.dashboard'))
    flash('Usuário ou senha incorretos!', 'error')
    return redirect(url_for('usuarios.index'))

@usuarios_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        login = request.form['login']
        senha = request.form['senha']
        nome = request.form['nome']
        cidade = request.form['cidade']
        cadastrar_usuario(login, senha, nome, cidade)
        return redirect(url_for('usuarios.index'))
    return render_template('cadastro.html')

@usuarios_bp.route('/dashboard')
def dashboard():
    usuario_id = session.get('usuario_id')
    if not usuario_id:
        return redirect(url_for('usuarios.index'))
    return render_template('dashboard.html')
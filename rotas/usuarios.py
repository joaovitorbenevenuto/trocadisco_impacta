from flask import Blueprint, render_template, request, redirect, url_for
from services.usuarios_service import cadastrar_usuario

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/')
def index():
    return render_template('login.html')

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

from flask import Flask
from rotas.usuarios import usuarios_bp
from rotas.discos import discos_bp

app = Flask(__name__)

app.secret_key = '12345678'

app.register_blueprint(usuarios_bp)
app.register_blueprint(discos_bp)

if __name__ == '__main__':
    app.run(debug=True)
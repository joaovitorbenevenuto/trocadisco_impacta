from flask import Flask
from rotas.usuarios import usuarios_bp

app = Flask(__name__)

# Registrando blueprint de usuários
app.register_blueprint(usuarios_bp)

if __name__ == '__main__':
    app.run(debug=True)
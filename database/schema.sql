CREATE DATABASE trocadisco_db;

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    login VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR(100) NOT NULL,
    nome VARCHAR(100),
    cidade VARCHAR(100)
);

CREATE TABLE discos (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    artista VARCHAR(150) NOT NULL,
    ano INT NOT NULL,
    genero VARCHAR(100),
    preco DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) DEFAULT 'disponivel',
    usuario_id INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);
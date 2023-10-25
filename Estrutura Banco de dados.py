from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Criar uma API Flask
app = Flask(__name__)

# Configurar a chave secreta e a URI do banco de dados
app.config['SECRET_KEY'] = 'FSD2323f#$!SAH'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

# Criar uma instância do SQLAlchemy
db = SQLAlchemy(app)

# Definir a estrutura da tabela Postagem
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))

# Definir a estrutura da tabela Autor
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')

# Executar o comando para criar o banco de dados
with app.app_context():
    db.create_all()

    # Criar usuários administradores
    autor = Autor(nome='jhonatan', email='jhonatan@email.com', senha='123456', admin=True)
    db.session.add(autor)
    db.session.commit()

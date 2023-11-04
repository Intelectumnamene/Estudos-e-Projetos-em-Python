from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Criar um API flask
app = Flask(__name__)
# Criar um instância de SQLAlchemy
app.config['SECRET_KEY'] = 'FSD2323f#$!SAH'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'


db = SQLAlchemy(app)
db: SQLAlchemy
# Definir a estrutra da tabela Postagem
# id_postagem, titulo, autor


class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))
# Definir a estrutra da tabela Autor
# id_autor, nome, email, senha, admin, postagens


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

    db.drop_all()#Apaga qualquer estrutura prévia que possas existir
    db.create_all()#Permite criar todas as tabela que estão anexadas ao db
    # Criar usuários adminstradores
    autor = Autor(nome='jhonatan', email='jhonatan@email.com',
                senha='123456', admin=True)
    db.session.add(autor)#adiciona o novo autor ao banco de dados
    db.session.commit()

'''

'''
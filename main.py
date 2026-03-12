from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi import FastAPI

db = create_engine("sqlite:///dtbank.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

# criando tabelas
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Jogo(Base):
    __tablename__ = "jogos"

    id = Column("idg", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    genero = Column("genero", String)
    preco = Column("preco", Float)
    dono = Column("dono", ForeignKey("usuarios.id"))
    
    def __init__(self,titulo,genero,preco,dono):
        self.titulo = titulo
        self.genero = genero
        self.preco = preco
        self.dono = dono

Base.metadata.create_all(bind=db)

#Criando Usuário
#user1 = Usuario(nome="Timbronus",email="gordo@gmail.com",senha="ola@1232")
#session.add(user1)
#session.commit()

# Lendo dados especificos do DB
user_find = session.query(Usuario).filter_by(id=8).first()
print(user_find.nome)
print(user_find.email)
print(user_find.senha)
jogo_find = session.query(Jogo).filter_by(id=2).first()

#Criando Jogo
#jogo1 = Jogo(titulo="HouseFighter3",genero="Luta",preco=9.20,dono=user_find.id)
#session.add(jogo1)
#session.commit()
#jogo2 = Jogo(titulo="Lavador de Cortinas 2",genero="Simulação",preco=30.10,dono=user_find.id)
#session.add(jogo2)
#session.commit()

# Update em dados
#user_find.nome = 
#session.add(user_find)
#session.commit()
jogo_find.dono = "Nenhum"
session.add(jogo_find)
session.commit()

# Deletando Dados
#del_gam = session.query(Jogo).filter_by(id=12).first()
#session.delete(del_gam)
#session.commit()

#list_user = session.query(Usuario).all()
#for i in list_user:
#    print(i.nome)

# - - - - - 

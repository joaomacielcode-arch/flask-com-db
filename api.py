from main import *
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hp():
    return "/usuarios ou /jogos + index"

@app.get("/usuarios/{id_user}")
def userspec(id_user: int):
    spec_user = session.query(Usuario).filter_by(id=id_user).first()
    return spec_user.nome, spec_user.email, spec_user.senha

@app.get("/jogos/{id_jogo}")
def gamespec(id_jogo: int):
    spec_game = session.query(Jogo).filter_by(id=id_jogo).first()
    return spec_game.titulo,spec_game.genero,spec_game.preco,spec_game.dono
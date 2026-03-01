from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    email: str
    password: str


@app.post("/register")
def register(user: User):

    for u in users:
        if u.email == user.email:
            return "Usuário já existe"

    users.append(user)

    return "Usuário cadastrado com sucesso"


@app.post("/login")
def login(user: User):

    for u in users:

        if u.email == user.email and u.password == user.password:
            return "Login realizado com sucesso"

    return "Credenciais inválidas"

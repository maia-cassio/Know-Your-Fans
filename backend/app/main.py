from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, database

# Cria as tabelas no banco se não existirem (opcional, pois já criamos via pgAdmin)
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependência para injeção de sessão do banco
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "API Know Your Fan funcionando!"}

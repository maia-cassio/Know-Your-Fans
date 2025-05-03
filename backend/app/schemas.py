from pydantic import BaseModel

class FanBase(BaseModel):
    nome: str
    endereco: str
    cpf: str
    interesses: str
    eventos: str
    compras: str
    rede_social: str
    perfil_esports: str

class FanCreate(FanBase):
    pass

class Fan(FanBase):
    id: int
    documento: str

    class Config:
        orm_mode = True

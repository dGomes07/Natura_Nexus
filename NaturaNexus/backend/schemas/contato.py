from pydantic import BaseModel

class ContatoBase(BaseModel):
    nome: str
    mensagem: str

class ContatoCreate(ContatoBase):
    pass

class Contato(ContatoBase):
    id: int

    class Config:
        orm_mode = True

from sqlalchemy import Column, Integer, String
from backend.database import Base

class Contato(Base):
    __tablename__ = "contatos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    mensagem = Column(String)

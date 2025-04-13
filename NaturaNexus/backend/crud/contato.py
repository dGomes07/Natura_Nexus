from sqlalchemy.orm import Session
from backend import models, schemas

def get_contatos(db: Session):
    return db.query(models.Contato).all()

def get_contato(db: Session, contato_id: int):
    return db.query(models.Contato).filter(models.Contato.id == contato_id).first()

def create_contato(db: Session, contato: schemas.ContatoCreate):
    db_contato = models.Contato(**contato.dict())
    db.add(db_contato)
    db.commit()
    db.refresh(db_contato)
    return db_contato

def delete_contato(db: Session, contato_id: int):
    contato = get_contato(db, contato_id)
    if contato:
        db.delete(contato)
        db.commit()

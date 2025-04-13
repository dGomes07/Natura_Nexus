from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import SessionLocal, engine, Base
from backend import schemas, models, crud

Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/contatos", tags=["Contatos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Contato])
def listar_contatos(db: Session = Depends(get_db)):
    return crud.get_contatos(db)

@router.get("/{contato_id}", response_model=schemas.Contato)
def pegar_contato(contato_id: int, db: Session = Depends(get_db)):
    contato = crud.get_contato(db, contato_id)
    if not contato:
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    return contato

@router.post("/", response_model=schemas.Contato)
def criar_contato(contato: schemas.ContatoCreate, db: Session = Depends(get_db)):
    return crud.create_contato(db, contato)

@router.delete("/{contato_id}")
def deletar_contato(contato_id: int, db: Session = Depends(get_db)):
    crud.delete_contato(db, contato_id)
    return {"mensagem": "Contato deletado com sucesso"}

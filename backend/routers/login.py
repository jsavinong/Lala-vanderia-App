# Importaciones necesarias
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from backend import models, schemas, database
from backend.auth import crear_token_acceso

router = APIRouter()

# End Point de inicio de sesión
@router.post("/login")
def login(usuario: schemas.UsuarioLogin, db: Session = Depends(database.get_db)):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.correo_electronico == usuario.correo_electronico).first()
    if not db_usuario or not db_usuario.verificar_contraseña(usuario.contraseña):
        raise HTTPException(status_code=400, detail="Correo electrónico o contraseña incorrectos")
    access_token = crear_token_acceso(data={"sub": usuario.correo_electronico})
    return {"access_token": access_token, "token_type": "bearer"}

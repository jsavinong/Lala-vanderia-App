from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import models, schemas, database

router = APIRouter()

@router.put("/users/{correo_electronico}/preferences")
def update_user_preferences(correo_electronico: str, preferences: schemas.UsuarioCreate, db: Session = Depends(database.get_db)):
    db_user = models.Usuario.buscar_por_correo(db, correo_electronico)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    db_user.lenguaje_preferido = preferences.lenguaje_preferido
    db_user.suscrito_boletin = preferences.suscrito_boletin
    db.commit()
    return {"msg": "Preferencias actualizadas correctamente"}

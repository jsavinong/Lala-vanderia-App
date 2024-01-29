from datetime import datetime, timedelta
from jose import JWTError, jwt
from backend import schemas
from fastapi import HTTPException, status
from config.config import SECRET_KEY, ALGORITHM


credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="No se pudieron validar las credenciales",
    headers={"WWW-Authenticate": "Bearer"},
)


def crear_token_acceso(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=60)  # Token expira en 1 hora
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verificar_token_acceso(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        correo_electronico: str = payload.get("sub")
        if correo_electronico is None:
            raise credentials_exception
        return correo_electronico
    except JWTError:
        raise credentials_exception

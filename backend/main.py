from fastapi import FastAPI
from sqlalchemy import create_engine
from .database import Base, engine, get_db
from .routers import usuarios, servicios, pedidos, suscripciones, planes_suscripcion, pagos, horarios

# Crear las tablas en la base de datos (esto es opcional dependiendo de cómo manejes las migraciones de la base de datos)
Base.metadata.create_all(bind=engine)

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Incluir los routers de cada módulo
app.include_router(usuarios.router)
app.include_router(servicios.router)
app.include_router(pedidos.router)
app.include_router(suscripciones.router)
app.include_router(planes_suscripcion.router)
app.include_router(pagos.router)
app.include_router(horarios.router)

# Puedes agregar también middlewares, manejadores de eventos, etc.

from fastapi import FastAPI
# from sqlalchemy import create_engine
from .database import Base, engine
from .routers import verify_email, sign_up, login, servicios, pedidos, suscripciones, planes_suscripcion, pagos, horarios, estado_pedidos, estado_suscripcion, metodos_de_pago
from fastapi.middleware.cors import CORSMiddleware
from config.config import origins


# Crear las tablas en la base de datos (esto es opcional dependiendo de cómo manejes las migraciones de la base de datos)
Base.metadata.create_all(bind=engine)

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Configura el middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Los dominios/origins que serán aceptados
    allow_credentials=True,
    allow_methods=["*"],  # Métodos permitidos, por ejemplo: ["GET", "POST"]
    allow_headers=["*"],  # Headers permitidos
)

# Incluir los routers de cada módulo
app.include_router(verify_email.router)
app.include_router(sign_up.router)
app.include_router(login.router)
app.include_router(servicios.router)
app.include_router(pedidos.router)
app.include_router(suscripciones.router)
app.include_router(planes_suscripcion.router)
app.include_router(pagos.router)
app.include_router(horarios.router)
app.include_router(estado_suscripcion.router)
app.include_router(estado_pedidos.router)
app.include_router(metodos_de_pago.router)



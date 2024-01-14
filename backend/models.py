from sqlalchemy import Column, Integer, String, Float, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Modelo para tabla usuarios
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    correo_electronico = Column(String, unique=True, index=True)
    contraseña = Column(String)
    direccion = Column(String)
    telefono = Column(String)

# Modelo para tabla planes_suscripcion
class PlanSuscripcion(Base):
    __tablename__ = "planes_suscripcion"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String)
    precio = Column(Float)
    duracion = Column(Integer)

# Modelo para tabla suscripciones_usuarios
class SuscripcionUsuario(Base):
    __tablename__ = "suscripciones_usuarios"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    plan_id = Column(Integer, ForeignKey('planes_suscripcion.id'))
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    estado = Column(String)

# Modelo para tabla servicios
class Servicio(Base):
    __tablename__ = "servicios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String)
    precio = Column(Float)

    
# Modelo para tabla pedidos
class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    servicio_id = Column(Integer, ForeignKey('servicios.id'))
    fecha_pedido = Column(Date)
    fecha_entrega = Column(Date)
    estado = Column(String)
    cantidad = Column(Integer)
    precio_total = Column(Float)

# Modelo para tabla pagos
class Pago(Base):
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey('pedidos.id'))
    fecha_pago = Column(Date)
    monto = Column(Float)
    metodo_pago = Column(String)

# Modelo para tabla horarios
class Horario(Base):
    __tablename__ = "horarios"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey('pedidos.id'))
    fecha_recogida = Column(Date)
    hora_recogida = Column(Time)
    fecha_entrega = Column(Date)
    hora_entrega = Column(Time)

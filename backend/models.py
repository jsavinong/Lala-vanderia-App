from sqlalchemy import Column, Integer, String, Float, Date, Time, ForeignKey
from sqlalchemy.orm import relationship, Session
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

    def registrarUsuario(self, db: Session, usuario_data):
        """
        Método para registrar un nuevo usuario.
        :param db: Sesión de la base de datos
        :param usuario_data: Datos del usuario para el registro
        """
        # Aquí, usuario_data será un objeto o diccionario con los datos del usuario.
        # Crear una nueva instancia de Usuario
        nuevo_usuario = Usuario(**usuario_data)
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)
        return nuevo_usuario

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
    estado_suscripcion_id = Column(Integer, ForeignKey('estado_suscripciones.id'))

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
    estado_pedido_id = Column(Integer, ForeignKey('estado_pedidos.id'))
    cantidad = Column(Integer)
    precio_total = Column(Float)

# Modelo para tabla pagos
class Pago(Base):
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey('pedidos.id'))
    fecha_pago = Column(Date)
    monto = Column(Float)
    metodo_de_pago_id = Column(Integer, ForeignKey('metodos_de_pago.id'))

# Modelo para tabla horarios
class Horario(Base):
    __tablename__ = "horarios"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey('pedidos.id'))
    fecha_recogida = Column(Date)
    hora_recogida = Column(Time)
    fecha_entrega = Column(Date)
    hora_entrega = Column(Time)

# Modelo para tabla estado_suscripciones
class EstadoSuscripcion(Base):
    __tablename__ = 'estado_suscripciones'
    id = Column(Integer, primary_key=True, index=True)
    nombre_estado = Column(String, unique=True, nullable=False)

# Modelo para tabla estado_pedidos
class EstadoPedidos(Base):
    __tablename__ = 'estado_pedidos'
    id = Column(Integer, primary_key=True, index=True)
    nombre_estado = Column(String, unique=True, nullable=False)

# Modelo para tabla metodos_de_pago
class MetodosDePago(Base):
    __tablename__ = 'metodos_de_pago'
    id = Column(Integer, primary_key=True, index=True)
    metodo = Column(String, unique=True, nullable=False)
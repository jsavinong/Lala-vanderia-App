from sqlalchemy import Column, Integer, String, Float, Date, Time, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
import re
from validate_email import validate_email # ! librería "validate_email" no valida los correos correctamente, buscar otra opción
import bcrypt
from .database import Base
from datetime import datetime, date, timedelta


# Modelo para tabla usuarios
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    correo_electronico = Column(String, unique=True, index=True)
    contraseña = Column(String)
    direccion = Column(String)
    telefono = Column(String)
    plan_suscripcion_id = Column(Integer, ForeignKey('planes_suscripcion.id'))
    #lenguaje_preferido = Column(String, default='en')
    #suscrito_boletin = Column(String, default=None)
    # fecha_inicio_suscripcion = Column(Date)
    # fecha_fin_suscripcion = Column(Date)

    # Relaciones (si son necesarias)
    # plan_suscripcion = relationship("PlanSuscripcion")

    @classmethod
    def buscar_por_correo(cls, db: Session, correo_electronico: str):
        return db.query(cls).filter(cls.correo_electronico == correo_electronico).first()
    
    @classmethod
    def registrar_usuario(cls, db: Session, usuario_data):
        """
        Método para registrar un nuevo usuario.
        :param db: Sesión de la base de datos
        :param usuario_data: Datos del usuario para el registro
        """
        # Validar el correo electrónico
        if not validate_email(usuario_data["correo_electronico"]):
            raise HTTPException(status_code=400, detail="Correo electrónico inválido.")

        # Validar la contraseña
        if not cls.es_contraseña_valida(usuario_data["contraseña"]):
            raise HTTPException(
                status_code=400,
                detail="La contraseña no cumple con los criterios de seguridad.",
            )

        # Hashear la contraseña y actualizar usuario_data
        contraseña_hash = cls.hashear_contraseña(usuario_data["contraseña"])
        usuario_data["contraseña"] = contraseña_hash

        try:
            # Intenta crear una nueva instancia de Usuario y guardarla en la base de datos
            nuevo_usuario = Usuario(**usuario_data)
            db.add(nuevo_usuario)
            db.commit()
            db.refresh(nuevo_usuario)
            return nuevo_usuario

        except IntegrityError:
            db.rollback()  # Importante para cerrar la transacción fallida
            raise HTTPException(status_code=400, detail="El usuario ya existe o los datos son inválidos.")

        except Exception as e:
            # Manejo de otros errores inesperados
            raise HTTPException(status_code=500, detail="Error interno del servidor.")

    @staticmethod
    def es_contraseña_valida(contraseña):
        """
        Verifica si la contraseña cumple con los criterios de seguridad.
        """
        caracteres_especiales = r"[\W_]"
        longitud_minima = 8
        if len(contraseña) < longitud_minima:
            return False
        if not re.search("[a-z]", contraseña):
            return False
        if not re.search("[A-Z]", contraseña):
            return False
        if not re.search("[0-9]", contraseña):
            return False
        if not re.search(caracteres_especiales, contraseña):
            return False
        return True

    @staticmethod
    def hashear_contraseña(contraseña: str) -> str:
        """
        Hashea una contraseña usando bcrypt.
        """
        return bcrypt.hashpw(contraseña.encode(), bcrypt.gensalt()).decode()

    def verificar_contraseña(self, contraseña_plana: str) -> bool:
        return bcrypt.checkpw(contraseña_plana.encode(), self.contraseña.encode())

    def solicitar_servicio(self, db: Session, servicio_id: int, cantidad: int):
        """
        Método para que un usuario registrado solicite un servicio.
        :param db: Sesión de la base de datos
        :param servicio_id: ID del servicio solicitado
        :param cantidad: Cantidad del servicio solicitado
        """
        # Crear y guardar el pedido en la base de datos
        nuevo_pedido = Pedido(
            usuario_id=self.id,
            servicio_id=servicio_id,
            fecha_pedido=datetime.now(),
            cantidad=cantidad
        )
        db.add(nuevo_pedido)
        db.commit()
        db.refresh(nuevo_pedido)
        return nuevo_pedido

    def suscribirse_a_plan(self, db: Session, plan_id: int):
        """
        Método para suscribir a un usuario a un plan.
        :param db: Sesión de la base de datos
        :param plan_id: ID del plan al que suscribirse
        """
        # Verificar si el usuario ya está suscrito a un plan y si aún está activo
        if self.plan_suscripcion_id and self.fecha_fin_suscripcion >= date.today():
            raise Exception("El usuario ya tiene un plan activo.")

        # Actualizar el plan de suscripción del usuario
        self.plan_suscripcion_id = plan_id
        self.fecha_inicio_suscripcion = date.today()
        self.fecha_fin_suscripcion = date.today() + timedelta(days=30)  # Ejemplo para una duración de 30 días

        db.add(self)
        db.commit()
        db.refresh(self)
        return self

    def ver_detalles_pedido(self, db: Session, pedido_id: int):
        """
        Método para ver los detalles de un pedido.
        :param db: Sesión de la base de datos
        :param pedido_id: ID del pedido a consultar
        """
        # Obtener y retornar los detalles del pedido específico
        pedido = db.query(Pedido).filter(Pedido.id == pedido_id, Pedido.usuario_id == self.id).first()
        if not pedido:
            raise HTTPException(status_code=404, detail="Pedido no encontrado o no pertenece al usuario")
        return pedido

    def realizar_pago(self, db: Session, pedido_id: int, monto: float, metodo_pago_id: int):
        # Verificar que el pedido existe y pertenece al usuario
        pedido = db.query(Pedido).filter(Pedido.id == pedido_id, Pedido.usuario_id == self.id).first()
        if not pedido:
            raise HTTPException(status_code=404, detail="Pedido no encontrado o no pertenece al usuario.")
        
        # Verificar que el monto del pago coincide con el precio del pedido
        if pedido.precio_total != monto:
            raise HTTPException(status_code=400, detail="El monto del pago no coincide con el precio del pedido.")
        
        # Verificar que el pedido no ha sido pagado previamente
        pago_existente = db.query(Pago).filter(Pago.pedido_id == pedido_id).first()
        if pago_existente:
            raise HTTPException(status_code=400, detail="El pedido ya ha sido pagado.")
        
        # Verificar que el método de pago existe
        metodo_pago = db.query(MetodosDePago).filter(MetodosDePago.id == metodo_pago_id).first()
        if not metodo_pago:
            raise HTTPException(status_code=404, detail="Método de pago no encontrado.")
        
        # Actualizar el estado del pedido al pagar
        pedido.estado_pedido_id = 3  # Asumiendo que 3 representa "Pagado"
        
        # Crear un nuevo registro de pago
        nuevo_pago = Pago(pedido_id=pedido_id, monto=monto, metodo_de_pago_id=metodo_pago_id)
        db.add(nuevo_pago)
        db.commit()
        db.refresh(nuevo_pago)
        return nuevo_pago




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
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    plan_id = Column(Integer, ForeignKey("planes_suscripcion.id"))
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    estado_suscripcion_id = Column(Integer, ForeignKey("estado_suscripciones.id"))


# Modelo para tabla servicios
class Servicio(Base): # TODO: Por definir cuáles serán los tipos de servicios y cómo se medirán. Mientras tanto se medirá por lote. 1 Servicio = 1 lote
    __tablename__ = "servicios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String)
    precio = Column(Float)


# Modelo para tabla pedidos
class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    servicio_id = Column(Integer, ForeignKey("servicios.id"))
    fecha_pedido = Column(Date)
    fecha_entrega = Column(Date)
    estado_pedido_id = Column(Integer, ForeignKey("estado_pedidos.id"))
    cantidad = Column(Integer)
    precio_total = Column(Float)


# Modelo para tabla pagos
class Pago(Base):
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    fecha_pago = Column(Date)
    monto = Column(Float)
    metodo_de_pago_id = Column(Integer, ForeignKey("metodos_de_pago.id"))


# Modelo para tabla horarios
class Horario(Base):
    __tablename__ = "horarios"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    fecha_recogida = Column(Date)
    hora_recogida = Column(Time)
    fecha_entrega = Column(Date)
    hora_entrega = Column(Time)


# Modelo para tabla estado_suscripciones
class EstadoSuscripcion(Base):
    __tablename__ = "estado_suscripciones"
    id = Column(Integer, primary_key=True, index=True)
    nombre_estado = Column(String, unique=True, nullable=False)


# Modelo para tabla estado_pedidos
class EstadoPedidos(Base):
    __tablename__ = "estado_pedidos"
    id = Column(Integer, primary_key=True, index=True)
    nombre_estado = Column(String, unique=True, nullable=False)


# Modelo para tabla metodos_de_pago
class MetodosDePago(Base):
    __tablename__ = "metodos_de_pago"
    id = Column(Integer, primary_key=True, index=True)
    metodo = Column(String, unique=True, nullable=False)

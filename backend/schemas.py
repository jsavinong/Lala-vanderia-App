from pydantic import BaseModel
from datetime import date, time
from typing import Optional

# Esquema base para Usuario
class UsuarioBase(BaseModel):
    nombre: str
    correo_electronico: str

# Esquema para crear un Usuario
class UsuarioCreate(UsuarioBase):
    contraseña: str
    direccion: str
    telefono: str

# Esquema para leer un Usuario
class Usuario(UsuarioBase):
    id: int

    class Config:
        orm_mode = True

# Esquema base para Plan de Suscripción
class PlanSuscripcionBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    duracion: int

# Esquema para crear un Plan de Suscripción
class PlanSuscripcionCreate(PlanSuscripcionBase):
    pass

# Esquema para leer un Plan de Suscripción
class PlanSuscripcion(PlanSuscripcionBase):
    id: int

    class Config:
        orm_mode = True

# Esquema base para Suscripción de Usuario
class SuscripcionUsuarioBase(BaseModel):
    usuario_id: int
    plan_id: int
    fecha_inicio: date
    fecha_fin: date
    estado: str

# Esquema para crear una Suscripción de Usuario
class SuscripcionUsuarioCreate(SuscripcionUsuarioBase):
    pass

# Esquema para leer una Suscripción de Usuario
class SuscripcionUsuario(SuscripcionUsuarioBase):
    id: int

    class Config:
        orm_mode = True

# Esquema base para Servicio
class ServicioBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

# Esquema para crear un Servicio
class ServicioCreate(ServicioBase):
    precio: float

# Esquema para leer un Servicio
class Servicio(ServicioBase):
    id: int
    precio: float

    class Config:
        orm_mode = True

# Esquema base para Pedido
class PedidoBase(BaseModel):
    usuario_id: int
    servicio_id: int
    fecha_pedido: date
    cantidad: int

# Esquema para crear un Pedido
class PedidoCreate(PedidoBase):
    pass

# Esquema para leer un Pedido
class Pedido(PedidoBase):
    id: int
    fecha_entrega: Optional[date] = None
    estado: Optional[str] = None
    precio_total: Optional[float] = None

    class Config:
        orm_mode = True

# Esquema base para Pago
class PagoBase(BaseModel):
    pedido_id: int
    fecha_pago: date
    monto: float
    metodo_pago: str

# Esquema para crear un Pago
class PagoCreate(PagoBase):
    pass

# Esquema para leer un Pago
class Pago(PagoBase):
    id: int

    class Config:
        orm_mode = True

# Esquema base para Horario
class HorarioBase(BaseModel):
    pedido_id: int
    fecha_recogida: date
    hora_recogida: time
    fecha_entrega: date
    hora_entrega: time

# Esquema para crear un Horario
class HorarioCreate(HorarioBase):
    pass

# Esquema para leer un Horario
class Horario(HorarioBase):
    id: int

    class Config:
        orm_mode = True

# Aquí puedes agregar más esquemas según sea necesario.

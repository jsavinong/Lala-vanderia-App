from fastapi import HTTPException
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from validate_email import validate_email # ! librería "validate_email" no valida los correos correctamente, buscar otra opción
from backend.database import Base
from backend.models import Usuario, Servicio, PlanSuscripcion, Pedido, MetodosDePago
import bcrypt


# Configura una base de datos de prueba en memoria
DATABASE_URL_MEM = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL_MEM)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


@pytest.fixture
def db_session():
    """
    Crea una sesión de base de datos para la prueba.
    """
    db = TestingSessionLocal()
    yield db
    db.close()

def test_es_valido_correo_electronico():
    correo_valido = "j.savinong@gmail.com"
    correo_no_valido = "testexample.com@"
    assert validate_email(correo_valido)
    assert not validate_email(correo_no_valido)

def test_es_contraseña_valida():
    """
    Prueba la función es_contraseña_valida.
    """
    assert Usuario.es_contraseña_valida("Password01&") == True # Prueba con contraseña válida
    assert Usuario.es_contraseña_valida("Pss0m2!") == False # Prueba con contraseña inválida

def test_hashear_contraseña():
    contraseña = "unaContraseñaSegura123!"
    hash_contraseña = Usuario.hashear_contraseña(contraseña)
    assert contraseña != hash_contraseña
    assert bcrypt.checkpw(contraseña.encode(), hash_contraseña.encode())

def test_registrar_usuario(db_session):
    """
    Prueba el registro de un usuario.
    """
    usuario_data = {
        "nombre": "Test User",
        "correo_electronico": "test@example.com",
        "contraseña": "Password01&",
        "direccion": "123 Calle Falsa",
        "telefono": "1234567890",
    }
    usuario = Usuario.registrar_usuario(db=db_session, usuario_data=usuario_data)
    assert usuario.correo_electronico == "test@example.com"
    assert usuario.id is not None

def test_error_registro_usuario_existente(db_session):
    usuario_data_1 = {
        "nombre": "Usuario",
        "correo_electronico": "usuario@example.com",
        "contraseña": "Password123!",
        "direccion": "123 Calle Falsa",
        "telefono": "1234567890"
    }
    usuario_data_2 = {
        "nombre": "Otro Usuario",
        "correo_electronico": "usuario@example.com",  # Mismo correo electrónico
        "contraseña": "Password123!",
        "direccion": "456 Otra Calle",
        "telefono": "0987654321"
    }
    Usuario.registrar_usuario(db=db_session, usuario_data=usuario_data_1)
    with pytest.raises(HTTPException):
        Usuario.registrar_usuario(db=db_session, usuario_data=usuario_data_2)

def test_solicitar_servicio(db_session):
    # Crear un usuario de prueba
    usuario = Usuario(nombre="Test", correo_electronico="usuariotest@example.com", contraseña="secure123")
    db_session.add(usuario)
    db_session.commit()

    # Crear un servicio de prueba (asumiendo que tienes un modelo de Servicio)
    servicio = Servicio(nombre="Lavado")
    db_session.add(servicio)
    db_session.commit()

    # Llamar a solicitar_servicio
    pedido = usuario.solicitar_servicio(db=db_session, servicio_id=servicio.id, cantidad=1)

    # Asegurarse de que el pedido se creó correctamente
    assert pedido is not None
    assert pedido.usuario_id == usuario.id
    assert pedido.servicio_id == servicio.id
    assert pedido.cantidad == 1

def test_suscribirse_a_plan_usuario_con_plan_activo(db_session):
    # Crear usuario de prueba
    usuario = Usuario(nombre="Test User", correo_electronico="test11@example.com", contraseña="secure123")
    db_session.add(usuario)

    # Crear dos planes de suscripción de prueba
    plan1 = PlanSuscripcion(nombre="Plan A", descripcion="Plan A Descripcion", precio=100.0, duracion=30)
    plan2 = PlanSuscripcion(nombre="Plan B", descripcion="Plan B Descripcion", precio=200.0, duracion=30)
    db_session.add(plan1)
    db_session.add(plan2)
    db_session.commit()

    # Suscribir al usuario al primer plan
    usuario.suscribirse_a_plan(db=db_session, plan_id=plan1.id)

    # Intentar suscribir al usuario al segundo plan
    with pytest.raises(Exception):
        usuario.suscribirse_a_plan(db=db_session, plan_id=plan2.id)


def test_suscribirse_a_plan_usuario_sin_plan_activo(db_session):
    # Crear usuario de prueba
    usuario = Usuario(nombre="Test User", correo_electronico="test22@example.com", contraseña="secure123")
    db_session.add(usuario)

    # Crear un plan de suscripción de prueba
    plan = PlanSuscripcion(nombre="Plan Test", descripcion="Plan Test Descripcion", precio=150.0, duracion=30)
    db_session.add(plan)
    db_session.commit()

    # Suscribir al usuario al plan
    usuario_suscrito = usuario.suscribirse_a_plan(db=db_session, plan_id=plan.id)

    # Verificar que el usuario se haya suscrito correctamente al plan
    assert usuario_suscrito.plan_suscripcion_id == plan.id
    assert usuario_suscrito.fecha_inicio_suscripcion is not None
    assert usuario_suscrito.fecha_fin_suscripcion is not None

def test_ver_detalles_pedido_existente_usuario(db_session):
    # Configuración: Crear un usuario, un servicio, y un pedido que le pertenezca
    usuario = Usuario(nombre="Test User", correo_electronico="user@example.com", contraseña="test")
    db_session.add(usuario)
    servicio = Servicio(nombre="Servicio de prueba", descripcion="Descripción del servicio", precio=100.0)
    db_session.add(servicio)
    db_session.commit()

    pedido = Pedido(usuario_id=usuario.id, servicio_id=servicio.id, estado_pedido_id=1, precio_total=servicio.precio)
    db_session.add(pedido)
    db_session.commit()

    # Acción: Intentar ver los detalles del pedido
    detalles_pedido = usuario.ver_detalles_pedido(db=db_session, pedido_id=pedido.id)

    # Verificación: El pedido retornado debe coincidir con el pedido creado
    assert detalles_pedido.id == pedido.id
    assert detalles_pedido.estado_pedido_id == 1
    assert detalles_pedido.precio_total == 100.0
    assert detalles_pedido.servicio_id == servicio.id

def test_ver_detalles_pedido_no_existente(db_session):
    # Configuración: Crear un usuario sin pedidos
    usuario = Usuario(nombre="Test User", correo_electronico="userprueba@example.com", contraseña="test")
    db_session.add(usuario)
    db_session.commit()

    # Acción y Verificación: Intentar ver los detalles de un pedido no existente debería lanzar una excepción
    with pytest.raises(HTTPException) as exc_info:
        usuario.ver_detalles_pedido(db=db_session, pedido_id=999)

    # Verificar que se lanzó la excepción correcta
    assert exc_info.value.status_code == 404
    assert "Pedido no encontrado" in str(exc_info.value.detail)

def test_ver_detalles_pedido_no_pertenece_usuario(db_session):
    # Configuración: Crear dos usuarios y un pedido que pertenezca al primero
    usuario1 = Usuario(nombre="Usuario 1", correo_electronico="user1@example.com", contraseña="test1")
    usuario2 = Usuario(nombre="Usuario 2", correo_electronico="user2@example.com", contraseña="test2")
    db_session.add(usuario1)
    db_session.add(usuario2)
    db_session.commit()

    servicio = Servicio(nombre="Servicio de prueba", descripcion="Descripción del servicio", precio=100.0)
    db_session.add(servicio)
    db_session.commit()

    pedido = Pedido(usuario_id=usuario1.id, servicio_id=servicio.id, estado_pedido_id=1, precio_total=servicio.precio)
    db_session.add(pedido)
    db_session.commit()

    # Acción y Verificación: Intentar que el segundo usuario vea los detalles del pedido debería lanzar una excepción
    with pytest.raises(HTTPException) as exc_info:
        usuario2.ver_detalles_pedido(db=db_session, pedido_id=pedido.id)

    # Verificar que se lanzó la excepción correcta
    assert exc_info.value.status_code == 404
    assert "Pedido no encontrado o no pertenece al usuario" in str(exc_info.value.detail)

def test_realizar_pago_correcto(db_session):
    # Configuración inicial: Crear usuario, pedido, y método de pago
    usuario = Usuario(nombre="Test User", correo_electronico="userpago@example.com", contraseña="test")
    db_session.add(usuario)
    metodo_pago = MetodosDePago(metodo="Tarjeta")
    db_session.add(metodo_pago)
    servicio = Servicio(nombre="Servicio de prueba", precio=100.0)
    db_session.add(servicio)
    db_session.commit()

    pedido = Pedido(usuario_id=usuario.id, servicio_id=servicio.id, estado_pedido_id =2, precio_total=servicio.precio) # ! estado_pedido_id igual 2 equivalente a "Pendiente de pago"
    db_session.add(pedido)
    db_session.commit()

    # Acción: Realizar un pago
    pago_realizado = usuario.realizar_pago(db=db_session, pedido_id=pedido.id, monto=100.0, metodo_pago_id=metodo_pago.id)

    # Verificación
    assert pago_realizado.pedido_id == pedido.id
    assert pago_realizado.monto == 100.0
    assert pago_realizado.metodo_de_pago_id == metodo_pago.id

def test_realizar_pago_pedido_inexistente(db_session):
    # Configuración inicial: Crear usuario y método de pago, pero sin pedido
    usuario = Usuario(nombre="Test User", correo_electronico="userpago2@example.com", contraseña="test")
    db_session.add(usuario)
    metodo_pago = MetodosDePago(metodo="Paypal")
    db_session.add(metodo_pago)
    db_session.commit()

    # Acción y Verificación: Intentar realizar un pago para un pedido inexistente
    with pytest.raises(HTTPException):
        usuario.realizar_pago(db=db_session, pedido_id=997, monto=100.0, metodo_pago_id=metodo_pago.id)

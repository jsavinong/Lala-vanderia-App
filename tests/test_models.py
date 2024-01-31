from fastapi import HTTPException
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from validate_email import validate_email # ! librería "validate_email" no valida los correos correctamente, buscar otra opción
from backend.database import Base
from backend.models import Usuario, Servicio, PlanSuscripcion
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


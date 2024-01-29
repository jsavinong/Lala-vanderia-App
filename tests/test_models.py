from fastapi import HTTPException
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from validate_email import validate_email # ! No valida los correos correctamente, buscar otra opción
from backend.database import Base
from backend.models import Usuario, Servicio
import bcrypt


# Configura una base de datos de prueba en memoria
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL)
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


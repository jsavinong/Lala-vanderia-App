import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.database import Base
from backend.models import Usuario

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


def test_es_contraseña_valida():
    """
    Prueba la función es_contraseña_valida.
    """
    assert Usuario.es_contraseña_valida("Password123*") == True
    assert Usuario.es_contraseña_valida("pass") == False


def test_registrar_usuario(db_session):
    """
    Prueba el registro de un usuario.
    """
    usuario_data = {
        "nombre": "Test User",
        "correo_electronico": "test@example.com",
        "contraseña": "Password123!",
        "direccion": "123 Calle Falsa",
        "telefono": "1234567890",
    }
    usuario = Usuario.registrar_usuario(db=db_session, usuario_data=usuario_data)
    assert usuario.correo_electronico == "test@example.com"
    assert usuario.id is not None

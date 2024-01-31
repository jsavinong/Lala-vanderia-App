from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

# SECRET_KEY para la firma de JWT
SECRET_KEY = os.getenv("SECRET_KEY")

# Algoritmo para la codificación del JWT
ALGORITHM = os.getenv("ALGORITHM")

# URL de conexión a la base de datos
DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

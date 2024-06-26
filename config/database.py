from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # Asegúrate de importar Base desde el archivo correcto
import atexit
import signal

# Configuración de la base de datos
DATABASE_URL = 'sqlite:///databases/productos.db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Lista de sesiones abiertas
open_sessions = []

# Función para cerrar todas las sesiones abiertas
def close_sessions():
    for session in open_sessions:
        session.close()
    print("Todas las sesiones de la base de datos se han cerrado correctamente.")

# Registrar la función de cierre para cuando el script termine
atexit.register(close_sessions)

# Capturar la señal SIGINT para cerrar las sesiones correctamente
def signal_handler(sig, frame):
    close_sessions()
    print("Interrupción del script detectada. Sesiones cerradas.")
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

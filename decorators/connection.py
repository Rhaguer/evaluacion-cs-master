from config.database import SessionLocal,open_sessions

# Decorador para manejar sesiones y excepciones
def with_session(func):
    def wrapper(*args, **kwargs):
        db_session = SessionLocal()
        open_sessions.append(db_session)  # Añadir la sesión a la lista de sesiones abiertas
        try:
            result = func(db_session, *args, **kwargs)
            db_session.commit()
            return result
        except Exception as e:
            db_session.rollback()
            print(f"Error: {e}")
            return None
        finally:
            if db_session in open_sessions:
                open_sessions.remove(db_session)  # Eliminar la sesión de la lista de sesiones abiertas
            db_session.close()
    return wrapper
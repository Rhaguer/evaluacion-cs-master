from functools import wraps
from contexto import Contexto

def require_permiso(required_permiso):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            usuario = Contexto.get_usuario()
            if not usuario:
                print(f"Permiso denegado: se requiere el permiso {required_permiso}")
                return None

            # Reasociar el usuario a la sesión para evitar problemas de lazy loading
            session = Contexto.get_session()
            usuario = session.merge(usuario)
            
            if not any(permiso.nombre == required_permiso for rol in usuario.roles for permiso in rol.permisos):
                print(f"Permiso denegado: se requiere el permiso {required_permiso}")
                return None

            return func(*args, **kwargs)
        return wrapper
    return decorator

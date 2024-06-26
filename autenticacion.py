from models.Usuario import Usuario
from models.Rol import Rol
from decorators.connection import with_session
from contexto import Contexto
from sqlalchemy.orm import joinedload

class Autenticacion:
    
    @staticmethod
    @with_session
    def autenticar_usuario(db_session, username: str):
        usuario = db_session.query(Usuario).options(
            joinedload(Usuario.roles).joinedload(Rol.permisos)
        ).filter(Usuario.username == username).filter(Usuario.estado == 'activo').first()
        if usuario:
            Contexto.set_usuario(usuario, db_session)
            return usuario
        else:
            print("Usuario no encontrado")
            return None

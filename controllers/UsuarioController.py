from models.Usuario import Usuario
from models.Rol import Rol
from decorators.connection import with_session
from decorators.permissions import require_permiso
from sqlalchemy.orm import joinedload

class UsuarioController:

    @staticmethod
    def assign_single_role_to_user(db_session, usuario, rol_nombre):
        rol_obj = db_session.query(Rol).filter(Rol.nombre == rol_nombre).first()
        if rol_obj:
            usuario.roles = [rol_obj]  # Asigna un solo rol

    @staticmethod
    @with_session
    @require_permiso('crear_usuario')
    def create_usuario(db_session, nombre, username, rol):
        usuario = Usuario(
            nombre=nombre,
            username=username
        )
        UsuarioController.assign_single_role_to_user(db_session, usuario, rol)
        db_session.add(usuario)
        db_session.flush()
        return usuario.get()

    @staticmethod
    @with_session
    @require_permiso('leer_usuario')
    def get_usuario(db_session, usuario_id):
        usuario = db_session.query(Usuario).options(joinedload(Usuario.roles)).filter(Usuario.id == usuario_id).first()
        return usuario.get() if usuario else None

    @staticmethod
    @with_session
    @require_permiso('actualizar_usuario')
    def update_usuario(db_session, usuario_id, data, rol):
        usuario = db_session.query(Usuario).options(joinedload(Usuario.roles)).filter(Usuario.id == usuario_id).first()
        if usuario:
            for key, value in data.items():
                setattr(usuario, key, value)
            UsuarioController.assign_single_role_to_user(db_session, usuario, rol)
        return usuario.get() if usuario else None

    @staticmethod
    @with_session
    @require_permiso('eliminar_usuario')
    def toggle_usuario_estado(db_session, usuario_id):
        usuario = db_session.query(Usuario).options(joinedload(Usuario.roles)).filter(Usuario.id == usuario_id).first()
        if usuario:
            nuevo_estado = 'inactivo' if usuario.estado == 'activo' else 'activo'
            setattr(usuario, 'estado', nuevo_estado)
        return usuario.get() if usuario else None

    @staticmethod
    @with_session
    @require_permiso('listar_usuarios')
    def list_usuarios(db_session):
        usuarios = db_session.query(Usuario).options(joinedload(Usuario.roles)).all()
        return [usuario.get() for usuario in usuarios]

    @staticmethod
    @with_session
    def get_roles(db_session):
        roles = db_session.query(Rol).all()
        return [rol.get() for rol in roles]

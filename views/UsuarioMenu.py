from controllers.UsuarioController import UsuarioController
from decorators.menu import menu_action
from validators.Validation import Validation
from validators.validators import StringValidator, NotEmptyValidator, RolesValidator
from views.BaseMenu import BaseMenu

class UsuarioMenu(BaseMenu):

    @menu_action("Crear Usuario", order=1, permiso='crear_usuario')
    def crear_usuario(cls):
        valid_roles = cls.get_valid_roles()
        data = {
            "nombre": Validation([StringValidator(), NotEmptyValidator()]).validate("Nombre: "),
            "username": Validation([StringValidator(), NotEmptyValidator()]).validate("Username: "),
            "rol": Validation([RolesValidator(valid_roles)]).validate(f"Rol ({', '.join(valid_roles)}): ")
        }
        usuario = UsuarioController.create_usuario(nombre=data['nombre'], username=data['username'], rol=data['rol'])
        if usuario:
            print("Usuario creado con éxito.")

    @menu_action("Ver Usuario", order=2, permiso='leer_usuario')
    def ver_usuario(cls):
        usuario = cls.obtener_usuario()
        if usuario:
            cls.display_table(usuario)

    @menu_action("Actualizar Usuario", order=3, permiso='actualizar_usuario')
    def actualizar_usuario(cls):
        valid_roles = cls.get_valid_roles()
        usuario = cls.obtener_usuario()
        if usuario:
            rol_actual = usuario.roles[0].nombre if usuario.roles else 'Ninguno'
            data = {
                "nombre": Validation([]).validate(f"Nuevo Nombre (actual: {usuario.nombre}): ", default=usuario.nombre),
                "username": Validation([]).validate(f"Nuevo Username (actual: {usuario.username}): ", default=usuario.username),
                "rol": Validation([RolesValidator(valid_roles)]).validate(f"Nuevo Rol (actual: {rol_actual} - disponibles: {', '.join(valid_roles)}): ")
            }
            usuario = UsuarioController.update_usuario(usuario.id, data, rol=data['rol'])
            print("Usuario actualizado con éxito.")

    @menu_action("Activar/Desactivar Usuario", order=4, permiso='eliminar_usuario')
    def toggle_usuario_estado(cls):
        usuario = cls.obtener_usuario()
        if usuario:
            usuario = UsuarioController.toggle_usuario_estado(usuario.id)
            nuevo_estado = 'activo' if usuario.estado == 'activo' else 'inactivo'
            print(f"Usuario {'activado' if nuevo_estado == 'activo' else 'desactivado'} con éxito.")

    @menu_action("Listar Usuarios", order=5, permiso='listar_usuarios')
    def listar_usuarios(cls):
        usuarios = UsuarioController.list_usuarios()
        cls.display_table(usuarios)

    @staticmethod
    def obtener_usuario():
        usuario_id = input("ID del Usuario: ")
        if not usuario_id:
            print("Debe ingresar un ID de usuario.")
            return None
        try:
            usuario_id = int(usuario_id)
        except ValueError:
            print("ID de usuario inválido.")
            return None
        usuario = UsuarioController.get_usuario(usuario_id)
        if not usuario:
            print("Usuario no encontrado.")
            return None
        return usuario
    
    @classmethod
    def get_headers(cls):
        return ["ID", "Nombre", "Username", "Estado", "Roles"]

    @classmethod
    def extract_data(cls, usuario):
        return [usuario.id, usuario.nombre, usuario.username, usuario.estado, ', '.join([rol.nombre for rol in usuario.roles])]
    
    @staticmethod
    def get_valid_roles():
        return [rol.nombre for rol in UsuarioController.get_roles()]
import unittest
from controllers.UsuarioController import UsuarioController
from autenticacion import Autenticacion
from contexto import Contexto
from config.database import SessionLocal
from models.Usuario import Usuario

class TestUsuarioController(unittest.TestCase):

    def setUp(self):
        # Crear una nueva sesión
        self.db_session = SessionLocal()

        # Autenticar el usuario administrador y establecerlo en el contexto
        self.admin_user = Autenticacion.autenticar_usuario(username="admin")
        self.admin_user = self.db_session.merge(self.admin_user)
        Contexto.set_usuario(self.admin_user, self.db_session)

        # Crear un usuario único para todas las pruebas
        self.usuario = UsuarioController.create_usuario(
            nombre="Usuario Test Unico",
            username="usuario_test_unico",
            rol="Administrador"
        )

        if not self.usuario:
            self.fail("Error: La creación del usuario de prueba falló.")

    def tearDown(self):
        # Eliminar el usuario de prueba creado en cada prueba
        usuario = self.db_session.query(Usuario).filter(Usuario.id == self.usuario.id).first()
        if usuario:
            self.db_session.delete(usuario)
            self.db_session.commit()

        # Limpiar el contexto y cerrar la sesión
        Contexto.clear()
        self.db_session.close()

    def test_create_usuario(self):
        # Comprobar que el usuario se ha creado correctamente
        self.assertIsNotNone(self.usuario, "Error: El usuario debería haber sido añadido")
        self.assertEqual(self.usuario.nombre, "Usuario Test Unico", "Error: El nombre del usuario no coincide")
        self.assertEqual(self.usuario.username, "usuario_test_unico", "Error: El username del usuario no coincide")
        self.assertEqual(self.usuario.roles[0].nombre, "Administrador", "Error: El rol del usuario no coincide")
        
        print("Prueba de creación de usuario completada exitosamente.")
    
    def test_get_usuario(self):
        # Obtener el usuario creado en setUp
        usuario = UsuarioController.get_usuario(self.usuario.id)

        # Comprobar que el usuario se ha obtenido correctamente
        self.assertIsNotNone(usuario, "Error: El usuario debería existir")
        self.assertEqual(usuario.nombre, "Usuario Test Unico", "Error: El nombre del usuario no coincide")
        self.assertEqual(usuario.username, "usuario_test_unico", "Error: El username del usuario no coincide")
        self.assertEqual(usuario.roles[0].nombre, "Administrador", "Error: El rol del usuario no coincide")

        print("Prueba de obtención de usuario completada exitosamente.")

    def test_update_usuario(self):
        # Datos actualizados
        data = {
            "nombre": "Usuario Test Actualizado",
            "username": "usuario_test_actualizado"
        }

        # Actualizar el usuario
        usuario_actualizado = UsuarioController.update_usuario(self.usuario.id, data, rol="Vendedor")

        # Comprobar que el usuario se ha actualizado correctamente
        self.assertIsNotNone(usuario_actualizado, "Error: El usuario debería haber sido actualizado")
        self.assertEqual(usuario_actualizado.nombre, "Usuario Test Actualizado", "Error: El nombre del usuario no coincide")
        self.assertEqual(usuario_actualizado.username, "usuario_test_actualizado", "Error: El username del usuario no coincide")
        self.assertEqual(usuario_actualizado.roles[0].nombre, "Vendedor", "Error: El rol del usuario no coincide")

        print("Prueba de actualización de usuario completada exitosamente.")

    def test_toggle_usuario_estado(self):
        # Cambiar el estado del usuario a inactivo
        usuario_inactivo = UsuarioController.toggle_usuario_estado(self.usuario.id)

        # Comprobar que el estado del usuario se ha cambiado correctamente
        self.assertIsNotNone(usuario_inactivo, "Error: El usuario debería existir después de cambiar el estado")
        self.assertEqual(usuario_inactivo.estado, 'inactivo', "Error: El estado del usuario debería ser inactivo")

        # Cambiar el estado del usuario de nuevo a activo
        usuario_activo = UsuarioController.toggle_usuario_estado(self.usuario.id)

        # Comprobar que el estado del usuario se ha cambiado correctamente
        self.assertIsNotNone(usuario_activo, "Error: El usuario debería existir después de cambiar el estado")
        self.assertEqual(usuario_activo.estado, 'activo', "Error: El estado del usuario debería ser activo")

        print("Prueba de cambio de estado de usuario completada exitosamente.")

    def test_list_usuarios(self):
        # Listar todos los usuarios
        usuarios = UsuarioController.list_usuarios()
        
        # Comprobar que la lista de usuarios no está vacía
        self.assertIsInstance(usuarios, list, "Error: La lista de usuarios debería ser una lista")
        self.assertGreater(len(usuarios), 0, "Error: La lista de usuarios no debería estar vacía")

        # Comprobar que el usuario creado está en la lista comparando por ID
        usuario_ids = [usuario.id for usuario in usuarios]
        self.assertIn(self.usuario.id, usuario_ids, "Error: El usuario creado debería estar en la lista de usuarios")

        print("Prueba de listado de usuarios completada exitosamente.")

if __name__ == '__main__':
    unittest.main()

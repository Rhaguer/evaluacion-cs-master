import unittest
from controllers.VentaController import VentaController
from controllers.ProductoController import ProductoController
from controllers.UsuarioController import UsuarioController
from autenticacion import Autenticacion
from contexto import Contexto
from config.database import SessionLocal
from models.Venta import Venta
from models.Producto import Producto
from models.Usuario import Usuario

class TestVentaController(unittest.TestCase):

    def setUp(self):
        # Crear una nueva sesión
        self.db_session = SessionLocal()

        # Autenticar el usuario administrador y establecerlo en el contexto
        self.admin_user = Autenticacion.autenticar_usuario(username="admin")
        self.admin_user = self.db_session.merge(self.admin_user)
        Contexto.set_usuario(self.admin_user, self.db_session)

        # Crear un producto único para todas las pruebas
        self.producto = ProductoController.create_producto(
            nombre="Producto Test Unico",
            descripcion="Descripción Test",
            precio=10.0,
            cantidad=100,
            categoria="Categoría Test"
        )

        if not self.producto:
            self.fail("Error: La creación del producto de prueba falló.")


    def tearDown(self):
        # Eliminar el producto de prueba creado en cada prueba
        producto = self.db_session.query(Producto).filter(Producto.id == self.producto.id).first()
        if producto:
            self.db_session.delete(producto)

        # Eliminar las ventas creadas en cada prueba
        ventas = self.db_session.query(Venta).filter(Venta.producto_id == self.producto.id).all()
        for venta in ventas:
            self.db_session.delete(venta)

        self.db_session.commit()

        # Limpiar el contexto y cerrar la sesión
        Contexto.clear()
        self.db_session.close()

    def test_create_venta(self):
        # Crear una nueva venta
        venta = VentaController.create_venta(
            producto_id=self.producto.id,
            cantidad=1
        )

        # Comprobar que la venta se ha creado correctamente
        self.assertIsNotNone(venta, "Error: La venta debería haber sido añadida")
        self.assertEqual(venta.producto_id, self.producto.id, "Error: El ID del producto en la venta no coincide")
        self.assertEqual(venta.cantidad, 1, "Error: La cantidad en la venta no coincide")
        self.assertEqual(venta.vendedor_id, self.admin_user.id, "Error: El ID del vendedor en la venta no coincide")
        
        print("Prueba de creación de venta completada exitosamente.")

    def test_list_ventas(self):
        # Crear una nueva venta
        venta = VentaController.create_venta(
            producto_id=self.producto.id,
            cantidad=1
        )

        # Listar todas las ventas
        ventas = VentaController.list_ventas()

        # Comprobar que la lista de ventas no está vacía
        self.assertIsInstance(ventas, list, "Error: La lista de ventas debería ser una lista")
        self.assertGreater(len(ventas), 0, "Error: La lista de ventas no debería estar vacía")

        # Comprobar que la venta creada está en la lista comparando por ID
        venta_ids = [v.id for v in ventas]
        self.assertIn(venta.id, venta_ids, "Error: La venta creada debería estar en la lista de ventas")

        print("Prueba de listado de ventas completada exitosamente.")

if __name__ == '__main__':
    unittest.main()

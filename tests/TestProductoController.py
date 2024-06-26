import unittest
from controllers.ProductoController import ProductoController
from autenticacion import Autenticacion
from contexto import Contexto
from config.database import SessionLocal
from models.Producto import Producto

class TestProductoController(unittest.TestCase):

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
            self.db_session.commit()

        # Limpiar el contexto y cerrar la sesión
        Contexto.clear()
        self.db_session.close()

    def test_create_producto(self):
        # Comprobar que el producto se ha creado correctamente
        self.assertIsNotNone(self.producto, "Error: El producto debería haber sido añadido")
        self.assertEqual(self.producto.nombre, "Producto Test Unico", "Error: El nombre del producto no coincide")
        self.assertEqual(self.producto.descripcion, "Descripción Test", "Error: La descripción del producto no coincide")
        self.assertEqual(self.producto.precio, 10.0, "Error: El precio del producto no coincide")
        self.assertEqual(self.producto.cantidad, 100, "Error: La cantidad del producto no coincide")
        self.assertEqual(self.producto.categoria, "Categoría Test", "Error: La categoría del producto no coincide")
        
        print("Prueba de creación de producto completada exitosamente.")
    
    def test_get_producto(self):
        # Obtener el producto creado en setUp
        producto = ProductoController.get_producto(self.producto.id)

        # Comprobar que el producto se ha obtenido correctamente
        self.assertIsNotNone(producto, "Error: El producto debería existir")
        self.assertEqual(producto.nombre, "Producto Test Unico", "Error: El nombre del producto no coincide")
        self.assertEqual(producto.descripcion, "Descripción Test", "Error: La descripción del producto no coincide")
        self.assertEqual(producto.precio, 10.0, "Error: El precio del producto no coincide")
        self.assertEqual(producto.cantidad, 100, "Error: La cantidad del producto no coincide")
        self.assertEqual(producto.categoria, "Categoría Test", "Error: La categoría del producto no coincide")

        print("Prueba de obtención de producto completada exitosamente.")

    def test_update_producto(self):
        # Datos actualizados
        data = {
            "nombre": "Producto Test Actualizado",
            "descripcion": "Descripción Actualizada",
            "precio": 15.0,
            "cantidad": 150,
            "categoria": "Categoría Actualizada"
        }

        # Actualizar el producto
        producto_actualizado = ProductoController.update_producto(self.producto.id, data)

        # Comprobar que el producto se ha actualizado correctamente
        self.assertIsNotNone(producto_actualizado, "Error: El producto debería haber sido actualizado")
        self.assertEqual(producto_actualizado.nombre, "Producto Test Actualizado", "Error: El nombre del producto no coincide")
        self.assertEqual(producto_actualizado.descripcion, "Descripción Actualizada", "Error: La descripción del producto no coincide")
        self.assertEqual(producto_actualizado.precio, 15.0, "Error: El precio del producto no coincide")
        self.assertEqual(producto_actualizado.cantidad, 150, "Error: La cantidad del producto no coincide")
        self.assertEqual(producto_actualizado.categoria, "Categoría Actualizada", "Error: La categoría del producto no coincide")

        print("Prueba de actualización de producto completada exitosamente.")

    def test_toggle_producto_estado(self):
        # Cambiar el estado del producto a inactivo
        producto_inactivo = ProductoController.toggle_producto_estado(self.producto.id)

        # Comprobar que el estado del producto se ha cambiado correctamente
        self.assertIsNotNone(producto_inactivo, "Error: El producto debería existir después de cambiar el estado")
        self.assertEqual(producto_inactivo.estado, 'inactivo', "Error: El estado del producto debería ser inactivo")

        # Cambiar el estado del producto de nuevo a activo
        producto_activo = ProductoController.toggle_producto_estado(self.producto.id)

        # Comprobar que el estado del producto se ha cambiado correctamente
        self.assertIsNotNone(producto_activo, "Error: El producto debería existir después de cambiar el estado")
        self.assertEqual(producto_activo.estado, 'activo', "Error: El estado del producto debería ser activo")

        print("Prueba de cambio de estado de producto completada exitosamente.")

    def test_list_productos(self):
        # Listar todos los productos
        productos = ProductoController.list_productos()
        # Comprobar que la lista de productos no está vacía
        self.assertIsInstance(productos, list, "Error: La lista de productos debería ser una lista")
        self.assertGreater(len(productos), 0, "Error: La lista de productos no debería estar vacía")

        # Comprobar que el producto creado está en la lista comparando por ID
        producto_ids = [producto.id for producto in productos]
        self.assertIn(self.producto.id, producto_ids, "Error: El producto creado debería estar en la lista de productos")


        print("Prueba de listado de productos completada exitosamente.")

if __name__ == '__main__':
    unittest.main()

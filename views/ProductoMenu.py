from controllers.ProductoController import ProductoController
from decorators.menu import menu_action
from validators.Validation import Validation
from validators.validators import (StringValidator, NotEmptyValidator, IntValidator, FloatValidator, PositiveFloatValidator, NonNegativeIntValidator)
from views.BaseMenu import BaseMenu

class ProductoMenu(BaseMenu):

    @menu_action("Crear Producto", order=1, permiso='crear_producto')
    def crear_producto(cls):
        data = {
            "nombre": Validation([StringValidator(), NotEmptyValidator()]).validate("Nombre: "),
            "descripcion": Validation([StringValidator(), NotEmptyValidator()]).validate("Descripción: "),
            "precio": Validation([FloatValidator(),  PositiveFloatValidator()]).validate("Precio: "),
            "cantidad": Validation([IntValidator(),  NonNegativeIntValidator()]).validate("Cantidad: "),
            "categoria": Validation([StringValidator(), NotEmptyValidator()]).validate("Categoría: ")
        }
        producto = ProductoController.create_producto(**data)
        if producto:
            print("Producto creado con éxito.")

    @menu_action("Ver Producto", order=2, permiso='ver_producto')
    def ver_producto(cls):
        producto = cls.obtener_producto()
        if producto:
            cls.display_table(producto)

    @menu_action("Actualizar Producto", order=3, permiso='actualizar_producto')
    def actualizar_producto(cls):
        producto = cls.obtener_producto()
        if producto:
            data = {
                "nombre": Validation([]).validate(f"Nuevo Nombre (actual: {producto.nombre}): ", default=producto.nombre),
                "descripcion": Validation([]).validate(f"Nueva Descripción (actual: {producto.descripcion}): ", default=producto.descripcion),
                "precio": Validation([]).validate(f"Nuevo Precio (actual: {producto.precio}): ", default=producto.precio),
                "cantidad": Validation([]).validate(f"Nueva Cantidad (actual: {producto.cantidad}): ", default=producto.cantidad),
                "categoria": Validation([]).validate(f"Nueva Categoría (actual: {producto.categoria}): ", default=producto.categoria)
            }
            ProductoController.update_producto(producto.id, data)
            print("Producto actualizado con éxito.")

    @menu_action("Activar/Desactivar Producto", order=4, permiso='eliminar_producto')
    def toggle_producto_estado(cls):
        producto = cls.obtener_producto()
        if producto:
            producto = ProductoController.toggle_producto_estado(producto.id)
            nuevo_estado = 'activo' if producto.estado == 'activo' else 'inactivo'
            print(f"Producto {'activado' if nuevo_estado == 'activo' else 'desactivado'} con éxito.")

    @menu_action("Listar Productos", order=5, permiso='listar_productos')
    def listar_productos(cls):
        productos = ProductoController.list_productos()
        cls.display_table(productos)


    @staticmethod
    def obtener_producto():
        producto_id = input("ID del Producto: ")
        if not producto_id:
            print("Debe ingresar un ID de producto.")
            return None
        try:
            producto_id = int(producto_id)
        except ValueError:
            print("ID de producto inválido.")
            return None
        producto = ProductoController.get_producto(producto_id)
        if not producto:
            print("Producto no encontrado.")
            return None
        return producto

    @classmethod
    def get_headers(cls):
        return ["ID", "Nombre", "Descripción", "Precio", "Cantidad", "Categoría", "Estado"]

    @classmethod
    def extract_data(cls, producto):
        return [producto.id, producto.nombre, producto.descripcion, producto.precio, producto.cantidad, producto.categoria, producto.estado]
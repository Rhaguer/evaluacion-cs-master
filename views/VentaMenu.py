from controllers.VentaController import VentaController
from controllers.ProductoController import ProductoController
from decorators.menu import menu_action
from validators.Validation import Validation
from validators.validators import IntValidator, NotEmptyValidator, StringValidator, DateValidator, NonNegativeIntValidator
from views.BaseMenu import BaseMenu

class VentaMenu(BaseMenu):

    @menu_action("Registrar Venta", order=1, permiso='registrar_venta')
    def registrar_venta(cls):
        producto = cls.obtener_producto()
        if not producto:
            return

        data = {
            "producto_id": producto.id,
            "cantidad": Validation([IntValidator(), NonNegativeIntValidator()]).validate("Cantidad: ")
        }
        
        venta = VentaController.create_venta(**data)
        if venta:
            print("Venta registrada con éxito.")

    @menu_action("Listar Ventas", order=2, permiso='listar_ventas')
    def listar_ventas(cls):
        ventas = VentaController.list_ventas()
        cls.display_table(ventas)

    @classmethod
    def get_headers(cls):
        return ["ID", "Producto", "Cantidad", "Fecha", "Vendedor"]

    @classmethod
    def extract_data(cls, venta):
        return [venta.id, venta.producto.nombre, venta.cantidad, venta.fecha, venta.vendedor.nombre]


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
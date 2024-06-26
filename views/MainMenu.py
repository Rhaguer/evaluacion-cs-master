from router import Router
from views.ProductoMenu import ProductoMenu
from views.UsuarioMenu import UsuarioMenu
from decorators.menu import menu_action
from views.VentaMenu import VentaMenu

class MainMenu:

    @menu_action("Menú Productos", order=1)
    def menu_productos(self):
        menu_productos = Router(title="Menú de Productos")
        producto_menu = ProductoMenu()
        menu_productos.register(producto_menu)
        menu_productos.run()

    @menu_action("Menú Usuarios", order=2)
    def menu_usuarios(self):
        menu_usuarios = Router(title="Menú de Usuarios")
        usuario_menu = UsuarioMenu()
        menu_usuarios.register(usuario_menu)
        menu_usuarios.run()

    @menu_action("Menú Ventas", order=3)
    def menu_ventas(self):
        menu_ventas = Router(title="Menú de Ventas")
        venta_menu = VentaMenu()
        menu_ventas.register(venta_menu)
        menu_ventas.run()

    def run(self):
        main_menu = Router(title="Menú Principal")
        main_menu.register(self)
        main_menu.run()

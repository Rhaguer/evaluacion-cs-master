from models.Producto import Producto
from decorators.connection import with_session
from decorators.permissions import require_permiso

class ProductoController:
    
    @staticmethod
    @with_session
    @require_permiso('crear_producto')
    def create_producto(db_session, nombre, descripcion, precio, cantidad, categoria):
        producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            cantidad=cantidad,
            categoria=categoria
        )
        db_session.add(producto)
        db_session.flush()
        return producto.get()

    @staticmethod
    @with_session
    @require_permiso('ver_producto')
    def get_producto(db_session, producto_id):
        producto = db_session.query(Producto).filter(Producto.id == producto_id).first()
        return producto.get() if producto else None

    @staticmethod
    @with_session
    @require_permiso('actualizar_producto')
    def update_producto(db_session, producto_id, data):
        producto = db_session.query(Producto).filter(Producto.id == producto_id).first()
        if producto:
            for key, value in data.items():
                setattr(producto, key, value)
        return producto.get() if producto else None


    @staticmethod
    @with_session
    @require_permiso('eliminar_producto')
    def toggle_producto_estado(db_session, producto_id):
        producto = db_session.query(Producto).filter(Producto.id == producto_id).first()
        if producto:
            nuevo_estado = 'inactivo' if producto.estado == 'activo' else 'activo'
            setattr(producto, 'estado', nuevo_estado)
        return producto.get() if producto else None
    
    @staticmethod
    @with_session
    @require_permiso('listar_productos')
    def list_productos(db_session):
        productos = db_session.query(Producto).all()
        return [producto.get() for producto in productos]

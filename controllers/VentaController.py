from models.Venta import Venta
from models.Producto import Producto
from decorators.connection import with_session
from decorators.permissions import require_permiso
from sqlalchemy.orm import joinedload
from contexto import Contexto  
from datetime import datetime, date

class VentaController:

    @staticmethod
    @with_session
    @require_permiso('registrar_venta')
    def create_venta(db_session, producto_id, cantidad):
        producto = db_session.query(Producto).filter(Producto.id == producto_id).first()
        if not producto:
            print("Producto no encontrado.")
            return None

        if producto.cantidad < cantidad:
            print("Stock insuficiente.")
            return None

        producto.cantidad -= cantidad  # Actualizar el stock del producto
        
        fecha = date.today() 
        usuario_logueado = db_session.merge(Contexto.get_usuario())  
        venta = Venta(
            producto_id=producto_id,
            cantidad=cantidad,
            fecha=fecha,
            vendedor_id=usuario_logueado.id
        )
        db_session.add(venta)
        db_session.flush()
        return venta.get()

    @staticmethod
    @with_session
    @require_permiso('listar_ventas')
    def list_ventas(db_session):
        ventas = db_session.query(Venta).options(joinedload(Venta.producto), joinedload(Venta.vendedor)).all()
        return [venta.get() for venta in ventas]

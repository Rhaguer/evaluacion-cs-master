from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from .Model import Model

class Venta(Model):
    __tablename__ = 'ventas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    producto_id = Column(Integer, ForeignKey('productos.id'), nullable=False)
    cantidad = Column(Integer, nullable=False)
    fecha = Column(Date, nullable=False)
    vendedor_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

    producto = relationship("Producto")
    vendedor = relationship("Usuario")

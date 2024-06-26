from .Model import Model
from sqlalchemy import Column, String, Float, Integer, CheckConstraint

class Producto(Model):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True, index=True)

    nombre = Column(String, unique=True, nullable=False)

    descripcion = Column(String, nullable=True)

    precio = Column(Float, nullable=False)

    cantidad = Column(Integer, nullable=False)
    
    categoria = Column(String, nullable=False)

    estado = Column(String, nullable=False, default='activo')

    __table_args__ = (
        CheckConstraint('precio > 0', name='check_precio_positive'),
        CheckConstraint('cantidad >= 0', name='check_cantidad_non_negative'),
        CheckConstraint("estado IN ('activo', 'inactivo')")
    )

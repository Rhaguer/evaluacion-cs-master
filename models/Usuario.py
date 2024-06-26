from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship
from .Model import Model
from .Rol import usuario_rol

class Usuario(Model):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False, unique=True)
    estado = Column(String(50), nullable=False, default='activo') 
    roles = relationship('Rol', secondary=usuario_rol, back_populates='usuarios')

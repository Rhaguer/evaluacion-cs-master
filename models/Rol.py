from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship
from .Model import Model
from .Permiso import rol_permiso

usuario_rol = Table('usuario_rol', Model.metadata,
    Column('usuario_id', Integer, ForeignKey('usuarios.id'), primary_key=True),
    Column('rol_id', Integer, ForeignKey('roles.id'), primary_key=True)
)

class Rol(Model):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False, unique=True)
    permisos = relationship('Permiso', secondary=rol_permiso, back_populates='roles')
    usuarios = relationship('Usuario', secondary=usuario_rol, back_populates='roles')

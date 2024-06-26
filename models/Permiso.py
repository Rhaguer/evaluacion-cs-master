from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship
from .Model import Model

rol_permiso = Table('rol_permiso', Model.metadata,
    Column('rol_id', Integer, ForeignKey('roles.id'), primary_key=True),
    Column('permiso_id', Integer, ForeignKey('permisos.id'), primary_key=True)
)

class Permiso(Model):
    __tablename__ = 'permisos'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False, unique=True)
    roles = relationship('Rol', secondary=rol_permiso, back_populates='permisos')

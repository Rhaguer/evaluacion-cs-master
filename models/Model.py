from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import RelationshipProperty
from typing import Any, Dict

Base = declarative_base()

class Model(Base):
    __abstract__ = True  # No se crea una tabla para esta clase

    def get(self, seen=None) -> Any:
        """
        Convierte la instancia del modelo a un objeto, incluyendo relaciones.

        :param seen: Conjunto de objetos ya vistos para evitar recursión infinita.
        :return: Objeto con los datos de la instancia del modelo.
        """
        if seen is None:
            seen = set()

        if self in seen:
            return f"Cyclic reference to {self.__class__.__name__}"

        seen.add(self)

        data = {c.name: getattr(self, c.name) for c in self.__table__.columns}

        # Incluir relaciones
        for rel in self.__mapper__.relationships:
            rel_data = getattr(self, rel.key)
            if rel_data is not None:
                if isinstance(rel_data, list):
                    data[rel.key] = [item.get(seen) if hasattr(item, 'get') else item for item in rel_data]
                else:
                    data[rel.key] = rel_data.get(seen) if hasattr(rel_data, 'get') else rel_data

        return type(self.__class__.__name__ + 'DTO', (), data)()

    def to_dict(self, seen=None) -> Dict[str, Any]:
        """
        Convierte la instancia del modelo a un diccionario.

        :param seen: Conjunto de objetos ya vistos para evitar recursión infinita.
        :return: Diccionario con los datos de la instancia del modelo.
        """
        if seen is None:
            seen = set()

        if self in seen:
            return f"Cyclic reference to {self.__class__.__name__}"

        seen.add(self)

        data = {c.name: getattr(self, c.name) for c in self.__table__.columns}

        # Incluir relaciones
        for rel in self.__mapper__.relationships:
            rel_data = getattr(self, rel.key)
            if rel_data is not None:
                if isinstance(rel_data, list):
                    data[rel.key] = [item.to_dict(seen) if hasattr(item, 'to_dict') else item for item in rel_data]
                else:
                    data[rel.key] = rel_data.to_dict(seen) if hasattr(rel_data, 'to_dict') else rel_data

        return data

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.to_dict()}>"

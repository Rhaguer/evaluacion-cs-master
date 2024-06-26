from abc import ABC, abstractmethod
from tabulate import tabulate

class BaseMenu(ABC):
    
    @abstractmethod
    def get_headers(cls):
        """Método abstracto para obtener los encabezados de la tabla"""
        pass
    
    @abstractmethod
    def extract_data(cls, item):
        """Método abstracto para extraer datos de un elemento"""
        pass
    
    @classmethod
    def display_table(cls, items):
        headers = cls.get_headers()
        if items is None:
            print(f"{headers[0]} no encontrado.")
            return

        if not isinstance(items, list):
            items = [items]

        if items:
            table = [cls.extract_data(item) for item in items]
            print(tabulate(table, headers, tablefmt="pretty"))
        else:
            print(f"No hay {headers[0].lower()}s disponibles.")

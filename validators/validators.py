from .BaseValidator import BaseValidator
from datetime import datetime

class UniqueValidator(BaseValidator):
    def validate(self, value):
        # Lógica para comprobar unicidad
        return value

class StringValidator(BaseValidator):
    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError("Debe ser una cadena de texto")
        return value

class NotEmptyValidator(BaseValidator):
    def validate(self, value):
        if not value.strip():
            raise ValueError("Este campo no puede estar vacío")
        return value

class IntValidator(BaseValidator):
    def validate(self, value):
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Debe ser un número entero")
        return value

class FloatValidator(BaseValidator):
    def validate(self, value):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Debe ser un número decimal")
        return value

class PositiveFloatValidator(BaseValidator):
    def validate(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("Debe ser un número positivo")
        return value

class NonNegativeIntValidator(BaseValidator):
    def validate(self, value):
        value = int(value)
        if value < 0:
            raise ValueError("Debe ser un número no negativo")
        return value
    
class RolesValidator(BaseValidator):
    def __init__(self, valid_roles):
        self.valid_roles = valid_roles

    def validate(self, value):
        rol = value.strip()
        if rol not in self.valid_roles:
            raise ValueError(f"El rol '{rol}' no es válido. Roles válidos: {', '.join(self.valid_roles)}")
        return rol

class DateValidator(BaseValidator):
    def validate(self, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError("La fecha debe tener el formato YYYY-MM-DD")
        return value